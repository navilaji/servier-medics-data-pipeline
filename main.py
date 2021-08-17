from parser.drug_parser import drug_parser
from parser.pubmed_parser import pubmed_parser
import json
from util.adhoc_analysis import adhoc_analyser
from service.publication_info_service import publication_info_service

pubmed_files = ["test/resources/pubmed.csv","test/resources/pubmed.json"]
cl_trial_files = ["test/resources/clinical_trials.csv"]
drugs_file = "test/resources/drugs.csv"
result_filename = "report.json"

def parse_files(files):
    data = []
    for file in files:
        data.extend (pubmed_parser.parse_pubmed_file(filepath=file))
    return data

def write_json_result(filename):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(result_graph, ensure_ascii=False, indent=4))

#parse drugs
drugs = drug_parser.parse_drugs_from_csv(drugs_file)
#parse pubmeds
pubmeds = parse_files(pubmed_files)
#parse clinical trials
cl_trials = parse_files(cl_trial_files)
#create the graph
result_graph = publication_info_service.generate_drug_pub_graph(drugs= drugs, pubmeds= pubmeds, cl_trials= cl_trials)
#write the json result into a file
write_json_result(result_filename )
print(f"The result has been written into the following file: {result_filename}")
print(adhoc_analyser.find_best_publisher(publication_graph= result_graph))
