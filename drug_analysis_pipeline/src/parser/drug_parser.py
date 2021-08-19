import csv
from drug_analysis_pipeline.src.mapper.drug_mapper import drug_mapper

DELIMITER = ","

class DrugeParser:
    '''
    this class is responsible for parsing the drugs from the corresponding files
    '''

    def parse_drugs_from_csv(self, filepath):
        '''
        This method parses the rows of the csv file containing the drugs data and maps them into a list of @Drug objects
        :param filepath: The path to the csv file
        :return: List of Drug objects containing the rows' data
        '''
        with open(filepath, newline='') as f:
            reader = csv.reader(f, delimiter=DELIMITER)
            next(reader)
            return list(map(drug_mapper.map_row,reader))

drug_parser = DrugeParser()
