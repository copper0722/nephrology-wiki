const DATA_URL = "questions.json";
const STORE_KEY = "nephro-cme-qbank-v1";

const els = {
  meta: document.querySelector("#question-meta"),
  correct: document.querySelector("#score-correct"),
  wrong: document.querySelector("#score-wrong"),
  topicFilter: document.querySelector("#topic-filter"),
  weakList: document.querySelector("#weak-topic-list"),
  empty: document.querySelector("#empty-state"),
  card: document.querySelector("#question-card"),
  count: document.querySelector("#question-count"),
  difficulty: document.querySelector("#question-difficulty"),
  title: document.querySelector("#question-title"),
  stem: document.querySelector("#stem"),
  form: document.querySelector("#answer-form"),
  submit: document.querySelector("#submit-btn"),
  reveal: document.querySelector("#reveal-btn"),
  result: document.querySelector("#result"),
  whys: document.querySelector("#why-blocks"),
  prev: document.querySelector("#prev-btn"),
  next: document.querySelector("#next-btn"),
  random: document.querySelector("#random-btn"),
  reset: document.querySelector("#reset-btn")
};

let questions = [];
let visibleQuestions = [];
let currentIndex = 0;
let selected = "";
let revealed = false;
let progress = loadProgress();

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORE_KEY)) || { answers: {} };
  } catch {
    return { answers: {} };
  }
}

function saveProgress() {
  localStorage.setItem(STORE_KEY, JSON.stringify(progress));
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function normalizeQuestions(raw) {
  return raw
    .filter((q) => q && q.id && Array.isArray(q.options))
    .map((q) => ({
      ...q,
      options: q.options.filter((opt) => ["A", "B", "C", "D"].includes(opt.letter)),
      topic_tags: Array.isArray(q.topic_tags) ? q.topic_tags : []
    }));
}

async function init() {
  try {
    const response = await fetch(DATA_URL, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    questions = normalizeQuestions(await response.json());
    buildTopicFilter();
    applyFilter();
    bindEvents();
    render();
  } catch (error) {
    els.meta.textContent = `Unable to load ${DATA_URL}: ${error.message}`;
    els.empty.hidden = false;
    els.card.hidden = true;
  }
}

function bindEvents() {
  els.topicFilter.addEventListener("change", () => {
    currentIndex = 0;
    selected = "";
    revealed = false;
    applyFilter();
    render();
  });

  els.prev.addEventListener("click", () => move(-1));
  els.next.addEventListener("click", () => move(1));
  els.random.addEventListener("click", randomQuestion);
  els.submit.addEventListener("click", submitAnswer);
  els.reveal.addEventListener("click", revealAnswer);
  els.reset.addEventListener("click", resetProgress);
}

function buildTopicFilter() {
  const topics = new Set();
  questions.forEach((q) => q.topic_tags.forEach((tag) => topics.add(tag)));
  els.topicFilter.innerHTML = '<option value="all">All topics</option>';
  [...topics].sort().forEach((topic) => {
    const option = document.createElement("option");
    option.value = topic;
    option.textContent = topic;
    els.topicFilter.append(option);
  });
}

function applyFilter() {
  const topic = els.topicFilter.value || "all";
  visibleQuestions = topic === "all"
    ? [...questions]
    : questions.filter((q) => q.topic_tags.includes(topic));
  currentIndex = Math.min(currentIndex, Math.max(visibleQuestions.length - 1, 0));
}

function currentQuestion() {
  return visibleQuestions[currentIndex];
}

function render() {
  const q = currentQuestion();
  renderScore();

  if (!q) {
    els.meta.textContent = "No matching questions.";
    els.empty.hidden = false;
    els.card.hidden = true;
    return;
  }

  const saved = progress.answers[q.id];
  selected = saved?.selected || selected;
  revealed = revealed || Boolean(saved);

  els.empty.hidden = true;
  els.card.hidden = false;
  els.meta.textContent = q.file_path ? `${q.id} · ${q.file_path}` : q.id;
  els.count.textContent = `${currentIndex + 1} / ${visibleQuestions.length}`;
  els.difficulty.textContent = [q.difficulty, q.bloom].filter(Boolean).join(" · ") || "ungraded";
  els.title.textContent = q.title || q.module || q.id;
  els.stem.innerHTML = renderParagraphs(q.stem);
  renderOptions(q);
  renderResult(q);
}

function renderParagraphs(text) {
  const blocks = String(text || "")
    .split(/\n{1,}/)
    .map((line) => line.trim())
    .filter(Boolean);
  return blocks.map((line) => `<p>${escapeHtml(line)}</p>`).join("");
}

function renderOptions(q) {
  els.form.innerHTML = "";
  q.options.forEach((option) => {
    const id = `opt-${q.id}-${option.letter}`.replace(/[^\w-]/g, "-");
    const label = document.createElement("label");
    label.className = "option";
    if (revealed && option.letter === q.answer) label.classList.add("correct");
    if (revealed && selected === option.letter && selected !== q.answer) label.classList.add("wrong");
    label.innerHTML = `
      <input type="radio" name="answer" value="${option.letter}" id="${id}">
      <span class="letter">${option.letter}</span>
      <span>${escapeHtml(option.text)}</span>
    `;
    const input = label.querySelector("input");
    input.checked = selected === option.letter;
    input.addEventListener("change", () => {
      selected = input.value;
      revealed = false;
      renderResult(q);
    });
    els.form.append(label);
  });
}

function renderResult(q) {
  if (!revealed) {
    els.result.hidden = true;
    els.whys.hidden = true;
    return;
  }

  const correct = selected === q.answer;
  els.result.hidden = false;
  els.result.className = `result ${correct ? "is-correct" : "is-wrong"}`;
  els.result.innerHTML = `
    <h3>${correct ? "Correct" : "Answer: " + escapeHtml(q.answer || "N/A")}</h3>
    ${renderParagraphs(q.explanation || "")}
  `;

  els.whys.hidden = false;
  els.whys.innerHTML = "";
  q.options.forEach((option) => {
    const block = document.createElement("section");
    block.className = "why";
    const why = q.option_whys?.[option.letter] || q.explanation || "";
    block.innerHTML = `
      <h3>${option.letter}. ${escapeHtml(option.text)}</h3>
      ${renderParagraphs(why)}
    `;
    els.whys.append(block);
  });
}

function submitAnswer() {
  const q = currentQuestion();
  if (!q || !selected) return;
  revealed = true;
  progress.answers[q.id] = {
    selected,
    correct: selected === q.answer,
    topic_tags: q.topic_tags,
    answered_at: new Date().toISOString()
  };
  saveProgress();
  render();
}

function revealAnswer() {
  if (!currentQuestion()) return;
  revealed = true;
  render();
}

function move(delta) {
  if (!visibleQuestions.length) return;
  currentIndex = (currentIndex + delta + visibleQuestions.length) % visibleQuestions.length;
  selected = "";
  revealed = false;
  render();
}

function randomQuestion() {
  if (!visibleQuestions.length) return;
  currentIndex = Math.floor(Math.random() * visibleQuestions.length);
  selected = "";
  revealed = false;
  render();
}

function resetProgress() {
  progress = { answers: {} };
  selected = "";
  revealed = false;
  saveProgress();
  render();
}

function renderScore() {
  const answers = Object.values(progress.answers || {});
  const correct = answers.filter((answer) => answer.correct).length;
  els.correct.textContent = correct;
  els.wrong.textContent = answers.length - correct;

  const weak = {};
  answers.filter((answer) => !answer.correct).forEach((answer) => {
    (answer.topic_tags || ["untagged"]).forEach((tag) => {
      weak[tag] = (weak[tag] || 0) + 1;
    });
  });
  const entries = Object.entries(weak).sort((a, b) => b[1] - a[1]).slice(0, 6);
  els.weakList.innerHTML = entries.length
    ? entries.map(([topic, count]) => `<li><span>${escapeHtml(topic)}</span><strong>${count}</strong></li>`).join("")
    : '<li class="muted">No wrong answers yet.</li>';
}

init();
