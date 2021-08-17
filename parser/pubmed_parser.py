import csv
import json5
from mapper.pubmed_mapper import publication_mapper
from abc import ABCMeta, abstractmethod
from io import StringIO
from util.string_util import string_util
DELIMITER = ","

class FileParser():
    __metaclass__ = ABCMeta
    @abstractmethod
    def parse_file(self, filepath): raise NotImplementedError

class CsvParser(FileParser):
    def parse_file(self, filepath):
        with open(filepath, 'r',newline='') as f:
            data = string_util.clean_text(f.read())
            reader = csv.reader(StringIO(data), delimiter=",", skipinitialspace=True, quoting=csv.QUOTE_ALL, quotechar='"')
            #skipping the header
            next(reader)
            return list(map(publication_mapper.map_csv_row, reader))

class JsonParser(FileParser):
    def parse_file(self, filepath):
        with open(filepath,'r',encoding='utf-8') as f:
            data = json5.load(f)
            return list(map(publication_mapper.map_json_obj, data))

parsers = {
    "csv": CsvParser(),
    "json": JsonParser()
}

class PubMedParser:

    def parse_pubmed_from_json(self, filepath):
        with open(filepath,'r',encoding='utf-8') as f:
            data = json5.load(f)
            return list(map(publication_mapper.map_json_obj, data))

    def parse_pubmed_file(self, filepath):

        if filepath is None:
            return None
        ftype = filepath.split('.')[-1].lower()
        if ftype in parsers:
            return parsers[ftype].parse_file(filepath)
        else:
            raise Exception(f"could not parse the file {filepath}")

pubmed_parser = PubMedParser()
