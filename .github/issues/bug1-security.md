
---

**name:** Vulnérabilité CSRF sur suppression d’équipe
**about:** Signaler une faille de sécurité permettant la suppression d'une équipe via une simple requête GET.
**title:** `[BUG] - [SEC-01] CSRF possible lors de la suppression d’une équipe via GET`
**labels:** Bug, Sécurité
**assignees:** (à remplir par ton équipe, ex: Membre 1 & 2)

---

**ID du Scénario lié :** SEC-01

**Description du bug :**
L'action de suppression d'une équipe est exposée via une méthode HTTP `GET` au lieu d'une méthode sécurisée (`POST` ou `DELETE`). Cela permet une attaque de type **CSRF** (Cross-Site Request Forgery) car aucune vérification de jeton (token) n'est effectuée. Un utilisateur peut déclencher une suppression simplement en accédant à une URL, ce qui rend l'action vulnérable à des liens malveillants ou à l'indexation par des robots.

**Étapes pour reproduire :**

1. Se connecter à l'application HR DB.
2. Identifier une équipe existante (ex: ID 5).
3. Saisir directement l'URL dans la barre d'adresse : `https://h.lsi2.hr.dmerej.info/team/delete/5`.
4. Appuyer sur 'Entrée'.

**Résultat Obtenu (Le Bug) :**
L’équipe est supprimée immédiatement via la requête `GET`. Le système n’exige aucun token `csrfmiddlewaretoken` pour cette action destructive.

**Résultat Attendu :**
Le système doit refuser la suppression via `GET` (Erreur 405). Il doit exiger une requête `POST` accompagnée d'un token CSRF valide, conformément aux standards de sécurité appliqués sur d'autres formulaires comme `/reset_db`.

**Sévérité :**

* [ ] Faible (Gênant mais non bloquant)
* [ ] Moyenne (Bloque une fonctionnalité secondaire)
* [x] **Haute / Critique (Faille de sécurité, suppression de données sans contrôle adéquat)**

**Preuve (Capture d'écran / Code) :**
*(Tu peux ici glisser une capture d'écran montrant l'équipe disparue de la liste après avoir simplement chargé l'URL dans ton navigateur).*

---

### Pourquoi ce rapport est solide :

* **Traçabilité :** L'ID **SEC-01** fait le lien direct avec ton plan de test.
* **Priorité :** En tant que faille de sécurité, elle justifie le label "Sécurité" et la sévérité "Critique".
* **Conformité :** Tu respectes les règles d'engagement sur l'éthique en documentant la faille sans altérer les données d'autrui.

**Souhaites-tu que je prépare le rapport pour un autre test en échec, comme le TC-11 (Email invalide accepté) ou le TC-09 (Caractères spéciaux) ?**