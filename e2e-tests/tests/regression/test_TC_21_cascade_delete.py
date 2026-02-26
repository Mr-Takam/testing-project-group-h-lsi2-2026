from models.employee_page import EmployeePage
from models.team_page import TeamPage

def test_team_deletion_should_not_delete_employees(page):
    """
    Test pour le Bug TC-21 : La suppression d'une équipe 
    ne doit PAS supprimer les employés membres.
    """
    # --- ARRANGE (Préparation des données et de l'état) ---
    emp_page = EmployeePage(page)
    team_page = TeamPage(page)
    
    # On crée l'environnement nécessaire au test
    emp_page.create_employee("Survivor", "survivor@test.com")
    team_page.create_team("Team Alpha")
    emp_page.add_to_team("Survivor", "Team Alpha team")

    # --- ACT (Exécution de l'action principale à tester) ---
    # L'action que l'on veut vérifier est la suppression de l'équipe
    team_page.delete_team("Team Alpha")

    # --- ASSERT (Vérification du résultat) ---
    emp_page.navigate_to_list()
    
    # On vérifie que l'employé est toujours présent malgré la suppression de l'équipe
    is_alive = emp_page.is_employee_visible("Survivor")
    assert is_alive, "BUG TC-21 : L'employé 'Survivor' a été supprimé en cascade avec son équipe !"