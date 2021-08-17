import csv
from mapper.drug_mapper import drug_mapper

DELIMITER = ","

class DrugeParser:

    def parse_drugs_from_csv(self, filepath):
        with open(filepath, newline='') as f:
            reader = csv.reader(f, delimiter=DELIMITER)
            next(reader)
            return list(map(drug_mapper.map_row,reader))

drug_parser = DrugeParser()
