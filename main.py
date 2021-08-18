import json
import sys
import logging
from src.parser.drug_parser import drug_parser
from src.parser.publication_parser import publication_parser
from src.util.adhoc_analysis import adhoc_analyser
from src.service.publication_info_service import publication_info_service

logging.basicConfig(level=logging.INFO)

def parse_publication_files(files):
    '''
    This method parses the publication like files such as medical publication and clinical trial and returns a list of Publication
    objects containing the data stored in the files.
    :param files: List of filepaths of the publication files. The file type can be either CSV or JSON for medical publication files
    :return: list of Publication objects containing the data stored in the CSV or JSON files.
    '''
    data = []
    logging.info (files)
    for file in files:
        data.extend (publication_parser.parse_publication_file(filepath=file))
    return data

def write_json_result(result, filename):
    '''
    This function writes the json object (or dict) into a file.
    :param result: the json object to be written into the file
    :param filename: the path to the output file
    :return: void
    '''
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=4))

def run_pipeline(drugs_file, pubmed_files, clinical_trial_files, result_filename):
    '''
    This pipeline parses the drugs, medical publications, clinical trials, and then generates a graph which
    presents the relation between the drugs, medical publications, clinical trials and the journals. Once the graph
    is generated, it gets written into a json file
    :param drugs_file: path to the csv file containing the list of drugs
    :param pubmed_files: list of the medical publication csv and json filepaths
    :param clinical_trial_files: list of the clinical trial csv and json filepaths
    :param result_filename: The name of the output file
    :return: void
    '''
    #parse drugs
    drugs = drug_parser.parse_drugs_from_csv(drugs_file)
    logging.info(drugs)
    #parse pubmeds
    pubmeds = parse_publication_files(pubmed_files)
    #parse clinical trials
    cl_trials = parse_publication_files(clinical_trial_files)
    #create the graph
    result_graph = publication_info_service.generate_drug_pub_graph(drugs= drugs, pubmeds= pubmeds, cl_trials= cl_trials)
    #write the json result into a file
    write_json_result(result_graph, result_filename)
    logging.info(f"The result has been written into the following file: {result_filename}")
    logging.info(f"The top mentioning journal is : {adhoc_analyser.find_best_publisher(publication_graph= result_graph)}")

if __name__ == '__main__':
    # parsing the arguments
    drugs_file = sys.argv[1]
    pubmed_files = [sys.argv[2],sys.argv[3]]
    clinical_trial_files = [sys.argv[4]]
    result_filename = sys.argv[5]
    #running the pipeline
    run_pipeline(drugs_file, pubmed_files, clinical_trial_files, result_filename)
