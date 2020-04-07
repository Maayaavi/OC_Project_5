# PUR BEURRE

Notre startup connait bien les habitudes alimentaires françaises. Notre restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs sur la butte de Montmartre.

Notre équipe a remarqué que nos utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer.
Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ?
Notre idée est donc de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.


### Description du parcours de l'utilisateur
1. L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :
    ```console
    >>>
    1. Vous souhaitez remplacer un aliment?
    2. Retrouver mes aliments substitués.
    
    00. Quitter
    >>>
    ```
    L'utilisateur interagit avec le programme via le terminal.<br>Sélectionne le choix numéro 1 et appuie sur la touché "Entrée".
    
    ```console
    >>>
    1. Vous souhaitez remplacer un aliment?
    2. Retrouver mes aliments substitués.
    
    00. Quitter
    >>> 1
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
    >>>
    ```
    
    Plusieurs propositions de catégories associées à un chiffre sont proposé. <br>
    L'utilisateur entre le chiffre correspondant à la catégorie.<br> 
    
    ```console
        ...
   
    >>> 2
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
    >>> 
    ```
   
    Plusieurs propositions de catégories associées à un chiffre sont proposé. <br>
    L'utilisateur entre le chiffre correspondant à la catégorie.<br> 
    ```console
        ...
   
    >>> 4
    ```
   
4. Le terminal propose les choix suivant :

5. Recherche d'aliments dans la base Open Food Facts.
    
6. Le terminal affiche l'écran de résultat : <br>
    ```console
    L'aliment qui vous est substitué est:
        Aliment
   
    Descrpition:
        Informations...
        lien
    Vous pouvez l'achtez à:
        Adresse...
    
    1. Enregistrer le résultat
    00. Quitter
    >>>
    ```
    Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant)<br>
    et un lien vers la page d'Open Food Facts concernant cet aliment.<br>

    L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

#####Spécificités:
   - Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question,
   - La recherche est effectué sur une base de donnée MySql.

---

##### Jeyasiri LAVANIYAN
##### Project 5 - Développeur d'application Python
###### OPENCLASSROOMS
