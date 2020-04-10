# PyFoodSubs

On veut bien changer nos habitudes d'alimentation mais ne savons pas bien toujours par quoi commencer.<br>
Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ?<br>
Alors voici un programme qui interagit avec la base de donnée d'Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

### Descrption du programme
Le programme permet à un l'utilisateur de fournir un aliment de substitution plus sain qu'il a sélectionné.<br>
Ce dernier s'appuie sur les données de la base OpenFoodFacts.

### Example de parcours basic de l'utilisateur
1. L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :
    ```console
    ##############################
    #  Bienvenue sur PyFoodSubs  #
    ##############################
   
    1. Vous souhaitez remplacer un aliment?
    2. Retrouver vos aliments substitués.
    
    00. Quitter
    
    Votre choix? 
    ```
    L'utilisateur interagit avec le programme via le terminal.<br>Sélectionne le choix numéro 1 et appuie sur la touché "Entrée".
    
    ```console
    ##############################
    #  Bienvenue sur PyFoodSubs  #
    ##############################
   
    1. Vous souhaitez remplacer un aliment?
    2. Retrouver mes aliments substitués.
    
    00. Quitter
    
    Votre choix? 1
    ```

2. Le terminal affiche les choix suivants :<br>
        
    ```console
    Sélectionnez la catégorie d'aliment.
    1. Catégorie 1
    2. Catégorie 2
    3. Catégorie 3
    4. Catégorie 4
    5. Catégorie 5
    
    0. Retour
    00. Quitter
   
    Votre choix? 
    ```
    
    Plusieurs propositions de catégories associées à un chiffre sont proposé. <br>
    L'utilisateur entre le chiffre correspondant à la catégorie.<br> 
    
    ```console
        ...
   
    Votre choix? 2
    ```
   
3. Le terminal affiche alors la liste de suivant :<br>
    ```console
    Vous avez choisie la catégorie d'aliment suivant : Catégorie 2
    Précisez maintenant la catégorie d'aliment parmis cette liste.
    1. Sous-catégorie 1
    2. Sous-catégorie 2
    3. Sous-catégorie 3
    4. Sous-catégorie 4
    5. Sous-catégorie 5
    
    0. Retour
    00. Quitter
   
    Votre choix?
    ```
   
    Plusieurs propositions de catégories associées à un chiffre sont proposé. <br>
    L'utilisateur entre le chiffre correspondant à la catégorie.<br> 
    ```console
        ...
   
    Votre choix? 4
    ```
   
4. Le terminal propose enfin les choix suivant :
    ```console
    Vous avez choisie la catégorie d'aliment suivant : Sous-catégorie 4
    Parmis la liste de la : Catégorie 2
    Précisez maintenant l'aliment parmis cette liste.
    1. Aliment 1
    2. Aliment 2
    3. Aliment 3
    4. Aliment 4
    5. Aliment 5
    
    0. Retour
    00. Quitter
   
    Votre choix?
    ```

    Affiche les aliments subsituable de la liste de sous-catérogie choisie.<br>
    L'utilisateur fait son choix parmis les aliments proposé.
    ```console
        ...
   
    Votre choix? 4
    ```
    
5. Le terminal affiche l'écran de résultat suivant : <br>
    ```console
    L'aliment qui vous est substitué est:
        Aliment
   
    Descrpition:
        Informations...
        lien
    Vous pouvez acheter ce produit à:
        Adresse...
    
    Veuillez sélectionner:
    1. Enregistrer votre résultat.
    2. Effectuer une nouvelle recherche d'aliment à remplacer.
   
    00. Quitter
   
    Votre choix? 
    ```
    Le programme recherche dans la base de donnée importé d'Open Food Facts.<br>
    Et propose un substitut, sa description, un magasin où l'acheter et un lien vers la page d'Open Food Facts concernant cet aliment.<br>

    L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données ou de quitter le programme.

##### Spécificités:
   - Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme lui répéte la question,
   - La recherche est effectué sur une base de donnée MySql.

---

##### Jeyasiri LAVANIYAN
##### Project 5 - Développeur d'application Python
###### OPENCLASSROOMS
