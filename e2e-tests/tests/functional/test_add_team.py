from playwright.sync_api import Page, expect

def test_create_team(page):
    # Plus besoin de page.goto("/reset_db"), c'est automatique !
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    # Vérification
    page.goto("/teams")
    assert page.is_visible(f"td:has-text('{team_name}')")