## [BUG] - [SEC-01] CSRF possible lors de la suppression d’une équipe via GET

**ID du Scénario lié :** SEC-01

**Description du bug :** L'action de suppression d'une équipe est exposée via une méthode HTTP `GET` au lieu d'une méthode sécurisée (`POST` ou `DELETE`). Cela permet une attaque de type **CSRF** (Cross-Site Request Forgery) car aucune vérification de jeton (token) n'est effectuée. Un utilisateur peut déclencher une suppression simplement en accédant à une URL, ce qui rend l'action vulnérable à des liens malveillants.

**Étapes pour reproduire :**

1. Se connecter à l'application HR DB.
2. Identifier une équipe existante (ex: ID 5).
3. Saisir directement l'URL dans la barre d'adresse : `https://h.lsi2.hr.dmerej.info/team/delete/5`.
4. Appuyer sur 'Entrée'.

**Résultat Obtenu (Le Bug) :** L’équipe est supprimée immédiatement via la requête `GET`. Le système n’exige aucun token `csrfmiddlewaretoken` pour cette action destructive.

**Résultat Attendu :** Le système doit refuser la suppression via `GET` (Erreur 405). Il doit exiger une requête `POST` accompagnée d'un token CSRF valide, comme c'est le cas sur la page `/reset_db`.

**Sévérité :**

* [ ] Faible
* [ ] Moyenne
* [x] **Haute / Critique** (Faille de sécurité permettant la suppression de données)
