def test_should_sanitize_special_characters_in_name(page):
    """
    Test pour TC-09 : Le système doit protéger contre les caractères spéciaux dans le nom.
    """
    special_name = "O'Connor <script>"
    
    page.goto("/add_employee")
    page.get_by_role("textbox", name="Name").fill(special_name)
    page.get_by_role("textbox", name="Email").fill("xss@test.com")
    page.locator("#id_address_line1").fill("123 Street")
    page.get_by_role("textbox", name="City").fill("Paris")
    page.get_by_role("spinbutton", name="Zip code").fill("75000")
    page.get_by_role("textbox", name="Hiring date").fill("2025-01-01")
    page.get_by_role("textbox", name="Job title").fill("Security Tester")
    
    page.get_by_role("button", name="Add").click()
    
    # On va vérifier comment c'est affiché dans la liste
    page.goto("/employees")
    
    # On vérifie si le nom avec les caractères spéciaux est présent tel quel
    # Si le bug existe, le texte brut est affiché sans filtrage.
    name_cell_visible = page.get_by_role("cell", name=special_name, exact=True).is_visible()
    assert not name_cell_visible, "BUG TC-09 : Le nom avec caractères spéciaux/scripts est accepté et affiché sans filtrage !"