import pytest
import sqlite3
import httpx
from pathlib import Path


BACKEND_DIR = Path(__file__).parent.parent / "backend"
DB_PATH = BACKEND_DIR / "db.sqlite3"
UP_SQL = BACKEND_DIR / "up.sql"
DOWN_SQL = BACKEND_DIR / "down.sql"

@pytest.fixture(autouse=True)
def reset_db():
    """Réinitialise la base de données avant CHAQUE test (Partie 3.3)."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.executescript(DOWN_SQL.read_text()) 
        cursor.executescript(UP_SQL.read_text())   
        conn.commit()

@pytest.fixture
def api_client():
    """Client HTTP centralisé pour éviter de répéter l'URL partout."""
    return httpx.Client(base_url="http://127.0.0.1:8000", follow_redirects=True)