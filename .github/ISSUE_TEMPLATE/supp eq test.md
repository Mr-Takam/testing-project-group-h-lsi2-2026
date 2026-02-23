Voici ton rapport de bug complété à partir de ton erreur :

---

**name** : SUP equipe avec membre
**about** : Signaler une anomalie trouvée lors des tests exploratoires
**title** : [BUG] - Erreur 500 lors de la suppression d’une équipe contenant déjà un membre
**labels** : Bug
**assignees** : Ryan

---

### Description du bug :

Une erreur 500 (Internal Server Error) est déclenchée lorsque l’on tente de supprimer une équipe qui contient déjà au moins un membre associé.
Le système ne gère pas correctement la contrainte de relation entre l’équipe et ses membres.

---

### Étapes pour reproduire :

1. Aller sur l’URL `/equipes`
2. Créer une équipe (si aucune n’existe)
3. Ajouter au moins un membre à cette équipe
4. Cliquer sur le bouton **Supprimer** de l’équipe
5. Observer l’erreur

---

### Résultat Obtenu (Le Bug) :

Une erreur **500 – Internal Server Error** est affichée.
L’équipe n’est pas supprimée et aucun message explicatif n’est présenté à l’utilisateur.

---

### Résultat Attendu :

Le système devrait :

* Soit empêcher la suppression avec un message clair (ex : *"Impossible de supprimer une équipe contenant des membres."*)
* Soit supprimer automatiquement les membres associés (selon la logique métier définie)
* Soit demander une confirmation avant suppression en cascade

Dans tous les cas, aucune erreur 500 ne devrait être générée.

---

### Sévérité :

🔴 **Haute / Critique**
Bloque une fonctionnalité principale (gestion des équipes) et expose une mauvaise gestion des erreurs côté serveur.

---

Si tu veux, je peux aussi te proposer une version plus technique (orientée backend / base de données avec hypothèse de contrainte FK).
