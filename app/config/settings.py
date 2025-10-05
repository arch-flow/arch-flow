from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DB_DIR = DATA_DIR / "db"
SCRIPTS_DIR = DATA_DIR / "scripts"
TMP_DIR = DATA_DIR / "tmp"
VENVS_DIR = DATA_DIR / "venvs"
RUNS_DIR = DATA_DIR / "runs"
PIP_CACHE_DIR = DATA_DIR / "pip-cache"

DB_PATH = DB_DIR / "archflow.db"
SHORT_DESCRIPTION_LIMIT = 140

for p in [DB_DIR, SCRIPTS_DIR, TMP_DIR, VENVS_DIR, RUNS_DIR, PIP_CACHE_DIR]:
    p.mkdir(parents=True, exist_ok=True)
