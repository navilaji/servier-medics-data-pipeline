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
