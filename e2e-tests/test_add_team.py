import sqlite3
from pathlib import Path

def test_should_add_team_successfully(api_client):
    response = api_client.post("/add_team", data={"name": "devs"})
    assert response.status_code == 200

    db_path = Path(__file__).parent.parent / "backend" / "db.sqlite3"
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        team = cursor.execute("SELECT name FROM hr_team WHERE name='devs'").fetchone()
        
        assert team is not None
        assert team["name"] == "devs"