def test_should_fail_to_delete_team_via_direct_url_get(page):
    # 1. Créer une équipe
    page.goto("/add_team")
    page.locator('input[name="name"]').fill("Target Team")
    page.click("text='Add'")
    
    # 2. Récupérer l'URL de suppression
    page.goto("/teams")
    delete_link = page.locator("tr", has_text="Target Team").get_by_role("link", name="Delete")
    href = delete_link.get_attribute("href")
    
    # 3. Tenter la suppression et vérifier la réponse du serveur
    response = page.goto(href)
    
    # Si le bug SEC-01 est là, le serveur répond 200 (OK) et supprime.
    # On veut que ça échoue si le statut est un succès.
    assert response.status != 200, "BUG SEC-01 : Le serveur accepte la suppression via GET (Status 200)"