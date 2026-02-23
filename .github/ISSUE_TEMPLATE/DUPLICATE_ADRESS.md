[BUG] - Absence de contrôle d'unicité sur l'adresse email des employés
ID du Scénario lié : RH-EMP-04 (Intégrité des données)

Description du bug :
L'application permet la création de plusieurs fiches employés utilisant la même adresse email. Dans un système de gestion, l'email doit normalement être un identifiant unique pour éviter les collisions de comptes et les erreurs administratives.

Étapes pour reproduire :

Aller sur le formulaire de création d'un employé.

Créer un premier employé avec l'email test@test.com et l'enregistrer.

Créer un second employé avec un nom différent, mais en utilisant exactement le même email : test@test.com.

Valider l'enregistrement.

Consulter la liste des employés (voir capture d'écran).

Résultat Obtenu (Le Bug) :
Le système accepte le doublon sans erreur. On se retrouve avec deux entrées distinctes possédant la même adresse email dans le tableau récapitulatif.

Résultat Attendu :
Le système devrait bloquer la création du second compte et afficher un message d'alerte : "Cette adresse email est déjà utilisée par un autre employé".

Sévérité :

[ ] Faible

[x] Moyenne (Problème d'intégrité de données qui peut impacter les futures fonctionnalités comme la connexion ou l'envoi de bulletins de paie).

[ ] Haute / Critique

Preuve (Capture d'écran / Code) :
Référence à ta capture d'écran montrant les deux lignes identiques pour test@test.com.
