import re
from playwright.sync_api import Page, expect

def test_team_deletion_should_not_delete_employees(page: Page):
    """
    Test pour le Bug TC-21 V2 : La suppression d'une équipe 
    ne doit PAS supprimer les employés membres.
    """
    
    # 1. Créer un employé "Survivor"
    page.goto("/add_employee")
    page.get_by_role("textbox", name="Name").fill("Survivor")
    page.get_by_role("textbox", name="Email").fill("survivor@test.com")
    page.locator("#id_address_line1").fill("123 Test St")
    page.get_by_role("textbox", name="City").fill("Paris")
    page.get_by_role("spinbutton", name="Zip code").fill("75000")
    page.get_by_role("textbox", name="Hiring date").fill("2025-01-01")
    page.get_by_role("textbox", name="Job title").fill("Developer")
    page.get_by_role("button", name="Add").click()
    
    # 2. Créer une équipe "Team Alpha"
    page.goto("/add_team")
    page.get_by_role("textbox", name="Name").fill("Team Alpha")
    page.get_by_role("button", name="Add").click()
    
    # 3. Assigner l'employé à l'équipe
    page.goto("/teams")
    
    # CORRECTIF ICI : 
    # On cherche la ligne (tr) qui contient le texte "Team Alpha"
    # Puis on clique sur le lien "View members" à l'intérieur de cette ligne
    team_row = page.locator("tr", has_text="Team Alpha")
    team_row.get_by_role("link", name="View members").click()
    
    # Sélectionner l'employé dans la liste et valider
    page.get_by_role("combobox").select_option(label="Survivor")
    page.get_by_role("button", name="Add").click()
    
    # 4. Supprimer l'équipe
    page.goto("/teams")
    # On utilise la même logique pour cliquer sur "Delete" proprement
    page.locator("tr", has_text="Team Alpha").get_by_role("link", name="Delete").click()
    
    # 5. VÉRIFICATION DU BUG
    # On retourne vérifier la liste des employés
    page.goto("/employees")
    
    # Si le bug TC-21 est présent, "Survivor" aura disparu.
    # L'assertion échouera ici, prouvant l'existence du bug.
    expect(page.get_by_role("cell", name="Survivor", exact=True)).to_be_visible(), \
        "BUG TC-21 : L'employé a été supprimé en cascade avec son équipe !"