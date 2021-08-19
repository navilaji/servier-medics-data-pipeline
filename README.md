1. Les données
Vous avez à votre disposition les 4 fichiers de données suivants :
drugs.csv : contient les noms de drugs (des médicaments) avec un id (atccode) et un nom (drug) pubmed.csv : contient des titres d’articles PubMed (title) associés à un journal (journal) à une date donnée (date) ainsi qu’un id (id)
pubmed.json : même structure que pubmed.csv mais en format JSON
clinical_trials.csv : contient des publications scientifiques avec un titre (scientific_title), un id (id), un journal (journal) et une date (date).
2. Le travail à réaliser
L’objectif est de construire une data pipeline permettant de traiter les données définies dans la partie précédente afin de générer le résultat décrit dans la partie 3.
Pour ce faire, vous devez mettre en place un projet en python organisé de la manière qui vous paraît la plus pertinente pour résoudre ce problème. Nous attendons que vous identifiiez une structure de projet et une séparation des étapes nécessaires qui permettent de mettre en évidence vos connaissances autour du développement de jobs data en python.
Il faudra essayer de considérer les hypothèses de travail suivantes :
• Certaines étapes de votre data pipeline pourraient être réutilisées par d’autres data pipelines
• On suppose que votre travail devra être intégré dans un orchestrateur de jobs (de type DAG) par la suite, votre code et la structure choisie doivent donc favoriser cette intégration
• Votre code doit respecter les pratiques que vous mettriez en place dans un cadre professionnel au sein d’une équipe de plusieurs personnes
Nous laissons volontairement un cadre assez libre pour voir votre manière de structurer un projet, de rédiger votre code et de mettre en place les éléments qui vous semblent essentiels dans un projet d’équipe. N’hésitez pas à argumenter votre proposition et les choix que vous faites si nécessaire.
3. Data pipeline
Votre data pipeline doit produire en sortie un fichier JSON qui représente un graphe de liaison entre les différents médicaments et leurs mentions respectives dans les différentes publications PubMed, les différentes publications scientifiques et enfin les journaux avec la date associée à chacune de ces mentions. La représentation ci-dessous permet de visualiser ce qui est attendu. Il peut y avoir plusieurs manières de modéliser cet output et vous pouvez justifier votre vision :
Règles de gestion :
- Un drug est considéré comme mentionné dans un article PubMed ou un essai clinique s’il est mentionné dans le titre de la publication.
- Un drug est considéré comme mentionné par un journal s’il est mentionné dans une publication émise par ce journal.

4. Traitement ad-hoc
Vous devez aussi mettre en place (hors de la data pipeline, vous pouvez considérer que c’est une partie annexe) une feature permettant de répondre à la problématique suivante :
• Extraire depuis le json produit par la data pipeline le nom du journal qui mentionne le plus de médicaments différents

5. How to run the programm: 
command line to run the pipeline:
    python -m main resources/drugs.csv \
    resources/pubmed.csv resources/pubmed.json \
    resources/clinical_trials.csv \
    report.json

6. Tests:
I have added some tests under the test directory, and they get run by the pytest.


The pipeline takes 5 arguments, here's the list:
    1- drugs file path
    2- first pubmed file path (csv or json)
    3- second pubmed file path(csv or json)
    4- clinical trial file path (csv or json)
    5- the output's file path


command line to run the pipeline:
    python -m main resources/drugs.csv \
    resources/pubmed.csv resources/pubmed.json \
    resources/clinical_trials.csv \
    report.json

The pipeline takes 5 arguments, here's the list:
    1- drugs file path
    2- first pubmed file path (csv or json)
    3- second pubmed file path(csv or json)
    4- clinical trial file path (csv or json)
    5- the output's file path
