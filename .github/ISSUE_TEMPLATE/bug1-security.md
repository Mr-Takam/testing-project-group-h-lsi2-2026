name : Vulnérabilité CSRF sur suppression d’équipe

about : Signaler un problème de sécurité lié à la suppression d’équipe via GET au lieu de POST.

title : [BUG] - CSRF possible lors de la suppression d’une équipe via GET

labels : Bug, Sécurité

assignees : (à remplir selon votre équipe)

ID du Scénario lié : SEC-01

Description du bug :
La suppression d’une équipe peut être déclenchée en saisissant directement l’URL GET /team/delete/{id} dans le navigateur. Le système ne devrait accepter que les requêtes POST avec un token CSRF.

Étapes pour reproduire :

Aller sur l’URL https://h.lsi2.hr.dmerej.info/team/delete/5 (remplacer 5 par l’ID d’une équipe existante).

Tenter d’exécuter la requête via le navigateur (GET).

Observer si l’équipe est supprimée sans authentification supplémentaire ni token CSRF.

Résultat Obtenu (Le Bug) :
L’équipe est supprimée immédiatement via la requête GET. Le système n’exige pas de token CSRF.

Résultat Attendu :
Le système doit refuser la suppression via GET et n’accepter que les requêtes POST avec un token CSRF valide, empêchant toute suppression non autorisée.

Sévérité :
Haute / Critique (Faille de sécurité qui permet la suppression d’éléments sans authentification sécurisée)

