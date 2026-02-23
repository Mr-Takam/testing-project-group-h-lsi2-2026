## [BUG] - [VAL-04] Absence de contrôle de cohérence sur la date d'embauche

**ID du Scénario lié :** VAL-04

**Description du bug :** Le système autorise l'enregistrement d'une date d'embauche (`Hiring date`) située dans le futur (ex: 2100). L'absence de validation côté serveur ou client permet l'entrée de données incohérentes qui pourraient fausser les calculs d'ancienneté ou les processus RH.

**Étapes pour reproduire :**

1. Aller sur l'URL d'ajout d'employé : `https://h.lsi2.hr.dmerej.info/add_employee`.
2. Remplir les champs obligatoires avec des données valides.
3. Dans le champ **Hiring date**, saisir une date lointaine dans le futur (ex: `01/01/2100`).
4. Cliquer sur le bouton de validation.

**Résultat Obtenu (Le Bug) :** L'application accepte la saisie sans erreur. L'employé est créé et la date future est enregistrée en base de données.

**Résultat Attendu :** Le système devrait bloquer la validation et afficher un message d'erreur indiquant que la date d'embauche ne peut pas être postérieure à la date du jour (ou une limite raisonnable définie par les règles métier).

**Sévérité :**

* [ ] Faible
* [x] **Moyenne** (Corrompt l'intégrité des données RH sans bloquer l'application)
* [ ] Haute / Critique

