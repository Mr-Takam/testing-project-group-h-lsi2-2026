from models.team_page import TeamPage

def test_should_fail_to_delete_team_via_direct_url_get(page):
    """
    Test pour SEC-01 : La suppression ne doit pas fonctionner via une URL directe (GET).
    On vérifie que le serveur rejette la requête ou que l'équipe n'est pas supprimée.
    """
    # --- ARRANGE (Préparation) ---
    team_page = TeamPage(page)
    team_name = "Target Team"
    
    # On crée l'équipe normalement
    team_page.create_team(team_name)
    
    # On récupère l'URL de suppression directe via le Page Object
    href = team_page.get_direct_delete_url(team_name)

    # --- ACT (Action) ---
    # On tente d'accéder directement à l'URL (requête GET)
    response = page.goto(href)

    # --- ASSERT (Vérification) ---
    # 1. Vérification technique : le serveur ne devrait pas répondre 200 (OK) pour un GET destructif
    assert response.status != 200, (
        f"BUG SEC-01 : Le serveur accepte la suppression de '{team_name}' via GET (Status 200)."
    )
    
    # 2. Vérification fonctionnelle : l'équipe doit toujours être présente dans la liste
    team_page.navigate_to_list()
    is_still_there = team_page.is_team_visible(team_name)
    assert is_still_there, (
        f"BUG SEC-01 : L'équipe '{team_name}' a été supprimée via une simple requête GET !"
    )