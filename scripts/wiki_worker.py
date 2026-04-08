import os
import subprocess
import requests
import json
import csv
from datetime import datetime

# --- Configuration ---
VAULT_ROOT = os.path.expanduser("~/Library/CloudStorage/Dropbox/Vault")
ORPHAN_FILE = os.path.join(VAULT_ROOT, "_data/wiki_orphans.tsv")
REPO_WIKI_DIR = os.path.join(VAULT_ROOT, "repos/nephrology-wiki/wiki")
CANONICAL_WIKI_DIR = os.path.join(VAULT_ROOT, "proj/wiki")
CME_RAW_DIR = os.path.join(VAULT_ROOT, "repos/nephrology-wiki/cme/bank/raw")
REPO_ROOT = os.path.join(VAULT_ROOT, "repos/nephrology-wiki")
ORPHAN_SCANNER = os.path.join(VAULT_ROOT, "repos/vault-scripts/wiki-orphan-scan.py")

LOCAL_LLM_URL = "http://localhost:8001/v1/chat/completions"
MODEL_NAME = "dealignai/Gemma-4-31B-JANG_4M-CRACK"

NEPHRO_KEYWORDS = ["kdigo", "daugirdas", "nolphgokal", "nephrology", "renal", "dialysis", "ckd", "aki"]
BATCH_LIMIT = 5 # Process only 5 orphans per run to avoid timeout/overload

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    with open(os.path.join(REPO_ROOT, "_worker_log.md"), "a") as f:
        f.write(f"- {timestamp}: {message}\n")

def run_command(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result

def call_local_llm(system_prompt, user_content):
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
        response = requests.post(LOCAL_LLM_URL, json=payload, timeout=300)
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
                log(f"Reached batch limit of {BATCH_LIMIT}. Stopping for this run.")
                break
                
            path = row['path']
            title = row['title']
            
            if any(kw in path.lower() or kw in title.lower() for kw in NEPHRO_KEYWORDS):
                full_raw_path = os.path.join(VAULT_ROOT, path)
                if not os.path.exists(full_raw_path):
                    continue
                
                dest_path = os.path.join(REPO_WIKI_DIR, f"{title}.md")
                if os.path.exists(dest_path):
                    continue
                
                log(f"Wikifying orphan: {title}")
                with open(full_raw_path, 'r', encoding='utf-8') as raw_f:
                    content = raw_f.read()
                
                system_prompt = (
                    "You are a world-class Nephrology expert. Convert raw medical content into an "
                    "exam-oriented wiki entry for the TSN Nephrology exam. \n"
                    "Rules:\n"
                    "1. Language: M2M English (concise, medical shorthand).\n"
                    "2. Focus: Key facts, exam logic, and textbook references (e.g., Brenner, Nissenson).\n"
                    "3. Structure: Topic-based, high density of information.\n"
                    "4. Formatting: Markdown. Use bold for key terms.\n"
                    "5. No full PICO/GRADE unless essential for the correct answer logic."
                )
                
                wiki_content = call_local_llm(system_prompt, content)
                if wiki_content:
                    with open(dest_path, 'w', encoding='utf-8') as dest_f:
                        dest_f.write(wiki_content)
                    log(f"Successfully wikified {title}")
                    processed_count += 1

    if processed_count == 0:
        log("No new nephro orphans to process.")

def sync_canonical_updates():
    log("Syncing updates from canonical wiki...")
    # Implementation: Sync based on modified time
    # This is a placeholder for the sync logic.
    pass

def generate_mcqs():
    log("Generating candidate MCQs...")
    # implementation of MCQ generation would go here.
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
