import re
from playwright.sync_api import Page, expect

def test_add_employee(page: Page):
    page.goto("/")
    
    # Remplissage du formulaire
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").fill("Tony")
    page.get_by_role("textbox", name="Email").fill("TonyMontana@gmail.com")
    page.locator("#id_address_line1").fill("32 rue du paradis, 42100")
    page.get_by_role("textbox", name="City").fill("Saint-Etienne")
    page.get_by_role("spinbutton", name="Zip code").fill("42100")
    page.get_by_role("textbox", name="Hiring date").fill("2026-02-27")
    page.get_by_role("textbox", name="Job title").fill("Gangster")
    page.get_by_role("button", name="Add").click()

    # Vérifications
    assert "/employees" in page.url
    assert page.get_by_role("cell", name="Tony", exact=True).is_visible()