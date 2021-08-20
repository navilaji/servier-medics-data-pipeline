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

5. Executer le pipeline:

Le command-line pour lancer le pipeline à partir de la root directory du projet:
    
    python -m drug_analysis_pipeline drug_analysis_pipeline/resources/drugs.csv \
        drug_analysis_pipeline/resources/pubmed.csv drug_analysis_pipeline/resources/pubmed.json \
        drug_analysis_pipeline/resources/clinical_trials.csv \
        report.json
        
le pipe reçoit 5 arguments:
    
    1- drugs file path
    2- le path du 1er fichier pubmed (csv ou json)
    3- le path du 2eme fichier pubmed (csv or json)
    4- le path du fichier clinical trial
    5- le path du fichier resultat

6. Tests:
J'ai créé des test sous le repertoire test, et il faut les lancer avec le pytest à partir du root directory

7. La solution Big Data
Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?

repose:
Dans ce projet on a utilisé les APIs native du python afin de lire les données et puis le filter et mapper etc.
Par contre dans le cas ou iya plusieurs fichiers avec des grosse tailles, la solution plus convenient sera le python spark ou pyspark avec les APIs autour de ça.
Les modifs que je mettrai en place seront:

    1- utiliser le spark.read.csv pour parser les fichier de csv. Quand on appel cet API , on peut passer plusieurs parametres, comme:
        - le schema d'objet à lire: spark.read.csv(filepath, schema=schema). Donc on peut preciser le type de data qu'on veut parser, par exemple Drug ou une Publication etc.
        - le schema peut etre defini par le StructType, par exemple: 
            drugs_schema = StructType([StructField("id", StringType(), True),
                                        StructField("name", StringType(), True)])
            
            donc on peut preciser le model à lire avec le StructType
        
        - on peut skipper le header de fichier csv avec l'option dans spark.read: spark.read.option('header', 'true')
    2- utiliser le spark.read.json pour parser les fichier de json
    3- dans l'etape ou on crée le graphe, on peut utiliser les methods de dataframes afin de filtrer, mapper, créer des nouvelles colons, etc dans chaque dataframe.
    4- avec le "join" de dataframe on peut trouver le lien entre drugs et le titre de publication plus rapidement au lieu de traverser toutes les données  
    5- dans la classe ad-hoc analysis on peut utiliser le spark map-reduce afin de trouver le journal avec le maximum score.
    6- ecrire le resultat dans un fichier json:
        result_dataframe.write.format('json').save(result_filepath)

8. Executer le pipeline dans un dag:
Je propose deux methods afin de lancer le pipeline dans un dag d'airflow/
    
    1- packager le module avec la command : python setup.py bdist_wheel, et puis installer le package dist/drug_analysis_pipeline-0.0.1-py3-none-any.whl
    dans l'environment d'airflow, et puis ajouter le python package installer au PYTHONPATH. Et puis on peut tout simplement lancer le pipeline avec 
    l'api PythonOperator ou le BashOperator.
    
    2- Créer une image docker de notre module à partir de fichier Dockerfile, et puis executer le l'image à partir avec le KubernetesPodOperator.  
    
