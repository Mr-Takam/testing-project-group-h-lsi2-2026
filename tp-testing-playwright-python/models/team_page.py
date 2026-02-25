from playwright.sync_api import Page, expect

class TeamPage:
    def __init__(self, page: Page):
        self.page = page
        # Définition des sélecteurs (Locators)
        self.name_input = page.locator('input[name="name"]')
        self.submit_button = page.get_by_role("button", name="Add")
        self.confirm_delete_button = page.get_by_role("button", name="Proceed")

    def navigate_to_add(self):
        """Navigue vers le formulaire de création d'équipe"""
        self.page.goto("/add_team")

    def navigate_to_list(self):
        """Navigue vers la liste des équipes"""
        self.page.goto("/teams")

    def create_team(self, name: str):
        """Remplit le formulaire et crée une équipe"""
        self.navigate_to_add()
        self.name_input.fill(name)
        self.submit_button.click()

    def delete_team(self, name: str):
        """Flux de suppression normal en 2 étapes (Liste -> Confirmation)"""
        self.navigate_to_list()
        # On cible précisément la ligne de l'équipe pour cliquer sur Delete
        self.page.locator("tr", has_text=name).get_by_role("link", name="Delete").click()
        # Cliquer sur Proceed sur la page de confirmation
        self.confirm_delete_button.click()

    def get_direct_delete_url(self, team_name: str):
        """Récupère l'URL du lien Delete pour tester la faille SEC-01"""
        self.navigate_to_list()
        delete_link = self.page.locator("tr", has_text=team_name).get_by_role("link", name="Delete")
        return delete_link.get_attribute("href")

    def is_team_visible(self, name: str) -> bool:
        """Vérifie si une équipe est présente dans le tableau"""
        try:
            # On utilise un timeout court de 5s pour ne pas bloquer les tests de régression
            self.page.wait_for_selector(f"td:has-text('{name}')", timeout=5000)
            return True
        except:
            return False