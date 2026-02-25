import re
from playwright.sync_api import Page

class EmployeePage:
    def __init__(self, page: Page):
        self.page = page
        # Locators pour le formulaire d'ajout
        self.add_new_link = page.get_by_role("link", name="Add new employee")
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.address_input = page.locator("#id_address_line1")
        self.city_input = page.get_by_role("textbox", name="City")
        self.zip_input = page.get_by_role("spinbutton", name="Zip code")
        self.hiring_date_input = page.get_by_role("textbox", name="Hiring date")
        self.job_title_input = page.get_by_role("textbox", name="Job title")
        self.submit_button = page.get_by_role("button", name="Add")
        
        # Locators pour l'assignation à une équipe
        self.add_to_team_link = page.get_by_role("link", name="Add to team")
        self.team_selector = page.locator("select[name='team']")

    def navigate_to_add(self):
        self.page.goto("/add_employee")

    def navigate_to_list(self):
        self.page.goto("/employees")

    def create_employee(self, name, email, date="2025-01-01"):
        """Remplit le formulaire et valide l'ajout"""
        self.navigate_to_add()
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.address_input.fill("123 Test St")
        self.city_input.fill("Paris")
        self.zip_input.fill("75000")
        self.hiring_date_input.fill(date)
        self.job_title_input.fill("QA Engineer")
        self.submit_button.click()

    def add_to_team(self, employee_name, team_option_label):
        """Flux : Liste -> Edit -> Add to team -> Select -> Submit"""
        self.navigate_to_list()
        # On cible précisément la ligne de l'employé
        self.page.locator("tr", has_text=employee_name).get_by_role("link", name="Edit").click()
        self.add_to_team_link.click()
        # On utilise le label exact (ex: "Team Alpha team")
        self.team_selector.select_option(label=team_option_label)
        self.submit_button.click()

    def is_employee_visible(self, name: str) -> bool:
        """Vérifie si un employé est dans la liste sans faire crash le test immédiatement"""
        try:
            # On réduit le timeout à 5s pour les tests de régression
            self.page.wait_for_selector(f"text={name}", timeout=5000)
            return True
        except:
            return False