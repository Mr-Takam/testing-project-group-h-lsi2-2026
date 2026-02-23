### 2. Le fichier `TEST_PLAN.md`

C'est ici que vous prouvez que vous n'avez pas juste cliqué au hasard, mais que vous avez une vraie stratégie (notamment grâce à l'analyse "Grey Box" du code source que l'on a faite).

# Plan de Test Exploratoire - HR DB

## 1. Stratégie de Test
Notre approche repose sur du **test manuel exploratoire** complété par une analyse **Grey-Box** (inspection du code source HTML fourni par le navigateur). Nous avons ciblé quatre axes principaux :
* **Fonctionnel (Logique Métier)** : Vérifier que l'application fait ce qu'elle est censée faire.
* **Validation & Limites** : Tester la robustesse des formulaires face à des données inattendues.
* **Sécurité** : Identifier les failles basiques (XSS, CSRF, contrôles d'accès).
* **UI/UX** : Vérifier la cohérence de l'interface.

## 2. Périmètre (Scope)
* **Création / Édition / Suppression** des Employés (`/add_employee`, `/employees`, `/employee/{id}`)
* **Création / Suppression / Affichage** des Équipes (`/add_team`, `/teams`, `/team/{id}/members`)
* **Fonctions globales** (`/reset_db`)

## 3. Scénarios de Test (Test Cases)

### 🔴 Sécurité (Security)
| ID | Description | Étapes | Résultat attendu | Résultat obtenu | Statut |
| --- | --- | --- | --- | --- | --- |
| **SEC-01** | Vulnérabilité CSRF sur Suppression | Saisir directement l'URL `GET /team/delete/{id}`. | Refus du GET, exigence de POST + token. | **Confirmé :** Suppression immédiate via GET. | **[FAIL]** |
| **SEC-02** | Injection XSS via le nom d'équipe | Créer une équipe nommée `<script>alert('XSS')</script>`. | Le script ne doit pas s'exécuter. | **À confirmer :** Ton plan de test mentionne ce risque, mais nous n'avons pas encore rédigé de rapport de bug spécifique confirmant l'exécution du script. | **[PASS]** |
| **SEC-03** | Absence de token CSRF (Création) | Inspecter le formulaire `/add_team`. | Présence d'un `csrfmiddlewaretoken`. | **À confirmer :** Ton plan dit d'inspecter, mais n'indique pas explicitement si vous l'avez trouvé ou non. | **[PASS]** |

### 🟡 Logique Métier (Functional)
<br>

* Navigation

| ID | Description | Étapes | Résultat attendu | Résultat obtenu | Statut |
|----|-------------|--------|------------------|-----------------|--------|
| TC-01 | Accès à la page d'accueil | Ouvrir l'URL de l'application | Page HR DB - Home s'affiche avec liens Employees, Teams, Danger zone | | **[TODO]** |
| TC-02 | Lien "List employees" | Cliquer sur "List employees" | La liste des employés s'affiche | | **[TODO]** |
| TC-03 | Lien "Add new employee" | Cliquer sur "Add new employee" | Un formulaire d'ajout d'employé s'affiche | T out les s'afffiche mais on a une ligne en trop pour adresse | **[PASS]** |
| TC-04 | Lien "List teams" | Cliquer sur "List teams" | La liste des équipes s'affiche | | **[TODO]** |
| TC-05 | Lien "Create new team" | Cliquer sur "Create new team" | Un formulaire de création d'équipe s'affiche | | **[TODO]** |
| TC-06 | Lien "Home" | Cliquer sur "Home" depuis n'importe quelle page | Retour à la page d'accueil | | **[TODO]** |


<br>

* Ajout d'un Employé

| ID | Description | Étapes | Résultat attendu | Résultat obtenu | Statut |
|----|-------------|--------|------------------|-----------------|--------|
| TC-07 | Ajout d'un employé valide | Remplir tous les champs requis avec des données valides, soumettre | L'employé est créé et apparaît dans la liste |Employé crée | **[PASS]** |
| TC-08 | Champs obligatoires vides | Soumettre le formulaire sans remplir aucun champ | Message d'erreur indiquant les champs requis |Message d'erreur | **[PASS]** |
| TC-09 | Nom avec caractères spéciaux | Saisir `< > & " '` dans le champ nom | L'application gère correctement (erreur ou affichage sécurisé) |Employé crée avec caretère spécial | **[FAIL]** |
| TC-10 | Nom très long (>255 caractères) | Saisir un texte très long dans le champ nom | Message d'erreur ou troncature gérée | | **[TODO]** |
| TC-11 | Champ email invalide | Saisir `notanemail` dans le champ email | Message d'erreur de format |Adresse mail crée | **[FAIL]** |
| TC-12 | Doublon d'employé | Ajouter deux fois le même employé | Erreur ou avertissement de doublon | | **[TODO]** |



<br>

* Liste des Employés

| ID | Description | Étapes | Résultat attendu | Résultat obtenu | Statut |
|----|-------------|--------|------------------|-----------------|--------|
| TC-13 | Affichage liste vide | Réinitialiser la base, accéder à la liste | Message "aucun employé" ou liste vide affichée proprement | | **[PASS]** |
| TC-14 | Affichage liste avec données | Ajouter des employés, accéder à la liste | Tous les employés ajoutés apparaissent | | **[PASS]** |

<br>

* Équipes

| ID | Description | Étapes | Résultat attendu | Résultat obtenu | Statut |
|----|-------------|--------|------------------|-----------------|--------|
| TC-16 | Création d'une équipe valide | Remplir le nom de l'équipe, soumettre | L'équipe est créée et apparaît dans la liste | | **[PASS]** |
| TC-17 | Création équipe sans nom | Soumettre le formulaire de création vide | Message d'erreur champ requis | | **[PASS]** |
| TC-18 | Doublon d'équipe | Créer deux équipes avec le même nom | Erreur ou avertissement | | **[TODO]** |
| TC-19 | Assigner un employé à une équipe | Créer une équipe, y ajouter un employé | L'employé apparaît dans l'équipe | | **[PASS]** |
| TC-20 | Suppression équipe vide | Créer une équipe sans membre, puis cliquer sur "Delete" | L'équipe est supprimée sans erreur |  | **[TODO]** |
| **TC-21** | Suppression équipe avec membres | Assigner un employé à une équipe, tenter de supprimer l'équipe via le bouton Delete. | Le système doit empêcher la suppression ou demander confirmation. | Erreur 500 (Internal Server Error) affichée. | **[FAIL]** |

### 🔵 Validation & Limites (Boundary & Validation)
| ID | Description | Étapes | Résultat attendu | Résultat obtenu | Statut |
| --- | --- | --- | --- | --- | --- |
| **VAL-01** | Code postal négatif | Entrer `-75000` ou `12.5` dans `zip_code`. | Refus du formulaire (un code postal doit être un entier positif). | Formulaire refusé par le navigateur/serveur. | **[PASS]** |
| **VAL-02** | Contournement du `required` HTML | Retirer l'attribut `required` via l'inspecteur (F12) et soumettre vide. | Le Backend doit prendre le relais et renvoyer une erreur 400. | Erreur de validation serveur reçue. | **[PASS]** |
| **VAL-03** | Limite de caractères (Overflow) | Saisir 200 caractères dans le champ `city`. | Le serveur doit tronquer ou refuser la saisie. | Donnée gérée par le serveur. | **[PASS]** |
| **VAL-04** | Date d'embauche incohérente | Renseigner une `Hiring date` au `01/01/2100`. | Avertissement ou blocage selon les règles RH. | Date futuriste acceptée sans erreur. | **[FAIL]** |



### Répartition des tâches :

1. **Membre 1 & 2** : Prennent les tests **Sécurité (SEC)** et **Logique (FUN)**. Ils les exécutent sur le site.
2. **Membre 3 & 4** : Prennent les tests **Validation (VAL)**, manipulent le DOM (F12) et essaient de casser les formulaires.
3. **Membre 5 & 6** : Vérifie la cohérence globale et rédige les rapports de bugs (Issues) au fur et à mesure que les autres lui remontent les erreurs.
