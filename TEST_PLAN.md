# Project Session 1.1 - Exploratory Testing & Bug Tracking

**LSI2 (Promo 2026) - Groupe H**

## L'équipe (Groupe H)
* [Nael AMIRAT]
* [Enzo IHADJADENE]
* [Cyril TAKAM]
* [Ryan Junior PENTE PENTE]
* [Abdou Khadre DIOP]
* [Aymar KINGOUM TAKA]

## Objectif
L'objectif de ce projet est de réaliser une campagne de **tests manuels exploratoires** sur une application web de gestion des Ressources Humaines (HR DB), puis de documenter de manière exhaustive les anomalies rencontrées.

**URL de l'environnement de test :** `[HR DB - Home](https://h.lsi2.hr.dmerej.info/)`

## Règles d'engagement respectées
Conformément aux directives :
1. **Confidentialité** : Aucune donnée personnelle réelle n'a été utilisée lors des tests (utilisation de données fictives/générées).
2. **Performance** : Aucun test de charge ou de stress n'a été effectué pour ne pas impacter le serveur partagé par la promotion.
3. **Sécurité et Éthique** : Les vulnérabilités découvertes ont été documentées sans altérer les données des autres équipes.

## Livrables
1. **Plan de Test détaillé :** [Consulter le TEST_PLAN.md](./TEST_PLAN.md)
2. **Bug Tracker :** [Consulter les GitHub Issues de ce repo](../../issues)


---

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
| ID | Titre du test | Action / Donnée de test | Résultat Attendu |
| :--- | :--- | :--- | :--- |
| **SEC-01** | Vulnérabilité CSRF sur Suppression | Saisir directement l'URL `GET /team/delete/{id}` dans le navigateur. | Le système doit refuser la suppression en GET et exiger une requête POST avec un token CSRF. |
| **SEC-02** | Injection XSS via le nom d'équipe | Créer une équipe nommée `<script>alert('XSS')</script>`. | Le script ne doit pas s'exécuter dans le navigateur sur la page `/teams`. |
| **SEC-03** | Absence de token CSRF (Création) | Inspecter le formulaire `/add_team`. | Un token `csrfmiddlewaretoken` doit être présent, comme c'est le cas sur `/reset_db`. |

### 🟡 Logique Métier (Functional)
| ID | Titre du test | Action / Donnée de test | Résultat Attendu |
| :--- | :--- | :--- | :--- |
| **FUN-01** | Doublon d'adresse email | Créer l'employé A avec `test@groupeh.com`, puis l'employé B avec `test@groupeh.com`. | Rejet du 2ème formulaire avec un message d'erreur clair (l'email doit être unique). |
| **FUN-02** | Doublon d'équipe | Créer une équipe "Dev", puis une autre équipe "Dev". | Rejet ou gestion des doublons pour éviter la confusion métier. |
| **FUN-03** | Suppression avec dépendances | Tenter de supprimer une équipe qui contient déjà des membres. | Le système doit empêcher la suppression ou avertir l'utilisateur, et non créer des employés "orphelins". |

### 🔵 Validation & Limites (Boundary & Validation)
| ID | Titre du test | Action / Donnée de test | Résultat Attendu |
| :--- | :--- | :--- | :--- |
| **VAL-01** | Code postal négatif | Dans `/add_employee`, entrer `-75000` ou `12.5` dans `zip_code`. | Refus du formulaire (un code postal doit être un entier positif). |
| **VAL-02** | Contournement du `required` HTML | Inspecter le champ `Name`, retirer l'attribut HTML `required`, puis soumettre vide. | Le Backend doit prendre le relais et renvoyer une erreur 400 (Bad Request). |
| **VAL-03** | Limite de caractères (Overflow) | Saisir 200 caractères dans le champ `city` (limité à 100 via HTML). | Si forcé via l'inspecteur, le serveur doit tronquer ou refuser la saisie. |
| **VAL-04** | Date d'embauche incohérente | Renseigner une `Hiring date` dans le futur lointain (ex: `01/01/2100`). | Avertissement ou blocage selon les règles RH. |



### Répartition des tâches :

1. **Membre 1 & 2** : Prennent les tests **Sécurité (SEC)** et **Logique (FUN)**. Ils les exécutent sur le site.
2. **Membre 3 & 4** : Prennent les tests **Validation (VAL)**, manipulent le DOM (F12) et essaient de casser les formulaires.
3. **Membre 5 & 6** : Vérifie la cohérence globale et rédige les rapports de bugs (Issues) au fur et à mesure que les autres lui remontent les erreurs.
