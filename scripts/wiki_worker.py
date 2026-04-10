import os
import subprocess
import requests
import json
import csv
import time
from datetime import datetime

# --- Configuration ---
VAULT_ROOT = "/Users/copper/dropbox/Vault"
ORPHAN_FILE = os.path.join(VAULT_ROOT, "_data/wiki_orphans.tsv")
REPO_WIKI_DIR = os.path.join(VAULT_ROOT, "repos/nephrology-wiki/wiki")
CANONICAL_WIKI_DIR = os.path.join(VAULT_ROOT, "wiki")
CME_RAW_DIR = os.path.join(VAULT_ROOT, "repos/nephrology-wiki/cme/bank/raw")
REPO_ROOT = os.path.join(VAULT_ROOT, "repos/nephrology-wiki")
ORPHAN_SCANNER = os.path.join(VAULT_ROOT, "repos/vault-scripts/wiki-orphan-scan.py")

LOCAL_LLM_URL = "http://localhost:11434/v1/chat/completions"
MODEL_NAME = "gemma4:31b-it-q4_K_M"

NEPHRO_KEYWORDS = ["kdigo", "daugirdas", "nolphgokal", "nephrology", "renal", "dialysis", "ckd", "aki",
                    "hemodialysis", "peritoneal", "kidney", "glomerular", "transplant", "electrolyte",
                    "nephrotic", "nephritic", "crrt", "fistula", "graft", "eskd", "gfr"]
# Exclude non-nephro topics that may contain nephro keywords incidentally
NEPHRO_EXCLUDE = ["cardiology", "hematology", "infectious_disease", "general_medicine",
                  "nutrition_metabolism", "public_health", "dementia", "alzheimer", "oncology"]
BATCH_LIMIT = 1 
MAX_INPUT_CHARS = 15000

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    with open(os.path.join(REPO_ROOT, "_worker_log.md"), "a") as f:
        f.write(f"- {timestamp}: {message}\n")

def run_command(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result

def call_local_llm(system_prompt, user_content):
    if len(user_content) > MAX_INPUT_CHARS:
        user_content = user_content[:MAX_INPUT_CHARS] + "... [Truncated for stability]"
        
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        "max_tokens": 4096,
        "temperature": 0.3
    }
    try:
        response = requests.post(LOCAL_LLM_URL, json=payload, timeout=600)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        log(f"LLM API Error: {e}")
        return None

def process_orphans():
    log("Running orphan scan...")
    run_command(f"python3 {ORPHAN_SCANNER}")
    
    if not os.path.exists(ORPHAN_FILE):
        log("Orphan file not found. Skipping.")
        return

    processed_count = 0
    with open(ORPHAN_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            if processed_count >= BATCH_LIMIT:
                break
                
            path = row['path']
            title = row['title']
            
            combined = (path + " " + title).lower()
            if not any(kw in combined for kw in NEPHRO_KEYWORDS):
                continue
            if any(ex in combined for ex in NEPHRO_EXCLUDE):
                continue

            full_raw_path = os.path.join(VAULT_ROOT, path)
            if not os.path.exists(full_raw_path):
                continue

            canonical_path = os.path.join(CANONICAL_WIKI_DIR, f"wiki_nephrology_{title}.md")
            if os.path.exists(canonical_path):
                continue

            log(f"Wikifying orphan: {title}")
            with open(full_raw_path, 'r', encoding='utf-8') as raw_f:
                content = raw_f.read()

            system_prompt = (
                "You are a world-class Nephrology expert. Convert raw medical content into an "
                "exam-oriented wiki entry for the TSN Nephrology exam. \n\n"
                "CRITICAL PROTOCOLS:\n"
                "1. ABSOLUTE BAN ON LATEX: Never use '$' for math. Never use $...$ or $$. \n"
                "   ALL symbols must be Unicode. \n"
                "   - Use 'K⁺' instead of '$K^+$'\n"
                "   - Use '→' instead of '$\\rightarrow$'\n"
                "   - Use '≥' instead of '$\\ge$'\n"
                "   - Use '≈' instead of '$\\approx$'\n"
                "   - Use '↑' and '↓' for increase/decrease.\n"
                "   GitHub renderer DOES NOT support LaTeX. This is a hard requirement.\n"
                "2. Naming: Use a Topic-based H1 title (e.g., '# Hyperkalemia in Dialysis Patients'), "
                "NOT the original article title.\n"
                "3. Structure: Every entry MUST include these sections:\n"
                "   - ## Exam Logic: Why this is the correct answer, common distractors, and conceptual pitfalls.\n"
                "   - ## Textbook References: Cite specific chapters from Brenner, Nissenson, or Daugirdas.\n"
                "   - ## Key Trials: List landmark trials (Author, Year, N, Bottom Line). No full PICO/GRADE.\n"
                "4. Language: M2M English (concise, medical shorthand).\n"
                "5. Formatting: Markdown. Use bold for key terms."
            )

            wiki_content = call_local_llm(system_prompt, content)
            if wiki_content:
                generated_date = datetime.now().strftime("%Y-%m-%d")
                frontmatter = (
                    "---\n"
                    f"type: wiki\n"
                    f"generated: {generated_date}\n"
                    f"source: {path}\n"
                    f"tags: [nephrology]\n"
                    f"author: gemma4\n"
                    "---\n\n"
                )
                full_content = frontmatter + wiki_content

                with open(canonical_path, 'w', encoding='utf-8') as cf:
                    cf.write(full_content)

                repo_path = os.path.join(REPO_WIKI_DIR, f"{title}.md")
                with open(repo_path, 'w', encoding='utf-8') as rf:
                    rf.write(full_content)

                log(f"Successfully wikified {title} (Canonical + Repo)")
                processed_count += 1
                time.sleep(10)

def sync_canonical_updates():
    pass

def generate_mcqs():
    pass

def git_push():
    log("Pushing updates to GitHub...")
    commands = [
        "git add -A",
        'git commit -m "Local LLM bulk maintenance update"',
        "git push"
    ]
    for cmd in commands:
        run_command(cmd, cwd=REPO_ROOT)

if __name__ == "__main__":
    try:
        process_orphans()
        sync_canonical_updates()
        generate_mcqs()
        git_push()
        log("Worker cycle completed successfully.")
    except Exception as e:
        log(f"Critical Worker Error: {e}")
