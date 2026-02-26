from models.employee_page import EmployeePage

def test_should_sanitize_special_characters_in_name(page):
    """
    Test pour TC-09 : Le système doit protéger contre les caractères spéciaux dans le nom.
    Vérifie si le nom est accepté et affiché sans nettoyage (sanitization).
    """
    # --- ARRANGE ---
    emp_page = EmployeePage(page)
    special_name = "O'Connor <script>"
    
    # --- ACT ---
    # On utilise la méthode du Page Object pour créer l'employé
    emp_page.create_employee(name=special_name, email="xss@test.com")
    
    # --- ASSERT ---
    emp_page.navigate_to_list()
    
    # On vérifie si le nom "dangereux" est visible tel quel dans la liste.
    # Si is_employee_visible renvoie True, cela signifie que le script n'a pas été filtré.
    is_visible_raw = emp_page.is_employee_visible(special_name)
    
    # L'assertion échouera si is_visible_raw est True, prouvant l'existence du bug TC-09.
    assert not is_visible_raw, (
        f"BUG TC-09 : Le nom '{special_name}' est affiché sans filtrage. "
        "Le système devrait encoder ou refuser les caractères spéciaux."
    )