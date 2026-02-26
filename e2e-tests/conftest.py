import pytest
import re
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def reset_database(page: Page):
    page.goto("/reset_db")
    # Utilise re.IGNORECASE pour être sûr de cliquer sur "Proceed" ou "proceed"
    page.get_by_role("button", name=re.compile("proceed", re.IGNORECASE)).click()
    page.wait_for_url("/")