[BUG] - Absence de contrôle de cohérence sur la date d'embauche (Hiring Date)
ID du Scénario lié : RH-EMP-02 (Gestion des fiches employés)

Description du bug :
Le système autorise la saisie et l'enregistrement d'une date d'embauche située dans le futur (ex: en 2030). Aucune erreur n'est affichée et la fiche employé est créée avec cette donnée incohérente, ce qui pourrait fausser les calculs d'ancienneté ou de paie.

Étapes pour reproduire :

Aller sur l'URL de création/édition d'un employé.

Remplir les champs obligatoires (Nom, Prénom, etc.).

Dans le champ 'Hiring Date', sélectionner une date postérieure à la date du jour (ex: 01/01/2030).

Cliquer sur le bouton 'Enregistrer' ou 'Valider'.

Observer que le formulaire est soumis avec succès.

Résultat Obtenu (Le Bug) :
L'application accepte la date future sans émettre d'avertissement ni de message d'erreur. L'employé est enregistré en base de données avec une date d'embauche invalide par rapport au temps présent.

Résultat Attendu :
Le système devrait empêcher la validation du formulaire et afficher un message d'erreur du type : "La date d'embauche ne peut pas être postérieure à la date du jour" (ou limiter la sélection dans le calendrier).

Sévérité :

[ ] Faible (Gênant mais non bloquant)

[x] Moyenne (Bloque une fonctionnalité secondaire) (Note : C'est moyen car cela corrompt l'intégrité des données RH sans faire crasher l'appli).

[ ] Haute / Critique
