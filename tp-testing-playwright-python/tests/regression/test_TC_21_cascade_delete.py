import re
from playwright.sync_api import Page, expect

def test_team_deletion_should_not_delete_employees(page: Page):
    """
    Test pour le Bug TC-21 : La suppression d'une équipe 
    ne doit PAS supprimer les employés membres.
    Flux : Add Employee -> Add Team -> Edit Employee (Add to team) -> Delete Team (Confirm)
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
    
    # 3. Assigner l'employé à l'équipe via sa fiche (flux éditer)
    page.goto("/employees")
    page.locator("tr", has_text="Survivor").get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Add to team").click()
    
    # On sélectionne "Team Alpha team" comme vu dans votre HTML
    page.locator("select[name='team']").select_option(label="Team Alpha team")
    page.get_by_role("button", name="Add").click()
    
    # 4. Supprimer l'équipe (Processus en 2 étapes)
    page.goto("/teams")
    # Étape A : Cliquer sur le lien Delete dans le tableau
    page.locator("tr", has_text="Team Alpha").get_by_role("link", name="Delete").click()
    
    # Étape B : Cliquer sur le bouton "Proceed" sur la page de confirmation
    # Note : C'est ici que l'Erreur 500 risque de se produire si le bug est présent
    page.get_by_role("button", name="Proceed").click()
    
    # 5. VÉRIFICATION DU BUG
    # On retourne vérifier que l'employé "Survivor" n'a pas été supprimé par erreur
    page.goto("/employees")
    
    # L'assertion échouera si l'employé a disparu, confirmant le bug TC-21
    expect(page.get_by_role("cell", name="Survivor", exact=True)).to_be_visible(), \
        "BUG TC-21 : L'employé a été supprimé en cascade avec son équipe !"