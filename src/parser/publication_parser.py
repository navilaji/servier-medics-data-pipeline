import csv
import json5
import logging
from abc import ABCMeta, abstractmethod
from io import StringIO
from src.util.string_util import string_util
from src.mapper.publication_mapper import publication_mapper

DELIMITER = ","
logging.basicConfig(level=logging.INFO)

class PubFileParser():
    '''
    The file parser interface
    '''
    __metaclass__ = ABCMeta
    @abstractmethod
    def parse_file(self, filepath):
        raise NotImplementedError

class PubCsvParserPub(PubFileParser):
    '''
    The csv file parser for csv publication files (clinical trial or medical publication)
    '''
    def parse_file(self, filepath):
        '''
        Parses the csv file and returns a list of Publication objects containing the parsed data
        :param filepath: path to the csv file
        :return: list of Publication objects containing the parsed data
        '''
        with open(filepath, 'r',newline='') as f:
            data = string_util.clean_text(f.read())
            reader = csv.reader(StringIO(data), delimiter=",", skipinitialspace=True, quoting=csv.QUOTE_ALL, quotechar='"')
            #skipping the header
            next(reader)
            return list(map(publication_mapper.map_csv_row, reader))

class PubJsonParser(PubFileParser):
    '''
    The json file parser for json medical publication files
    '''

    def parse_file(self, filepath):
        '''
        Parses the json file and returns a list of Publication objects containing the parsed data
        :param filepath: path to the json file
        :return: list of Publication objects containing the parsed data
        '''
        with open(filepath,'r',encoding='utf-8') as f:
            data = json5.load(f)
            return list(map(publication_mapper.map_json_obj, data))

parsers = {
    "csv": PubCsvParserPub(),
    "json": PubJsonParser()
}

class PublicationParser:
    '''
    This class is responsible for parsing the publications from the corresponding files. It can parse
    both clinical trial and medical publication data as both have the same files formats and contain similar information.
    '''

    def parse_publication_file(self, filepath):
        '''
        Parses the file using the corresponding parser depending on the file type.
        If the file type is json it uses the PubJsonParser class to parse the file. For the csv file type
        it uses the PubCsvParserPub class, otherwise it throws and exception and its unable to parse another filetype other
        than csv or json.
        :param filepath: The path to the json or csv file
        :return: list of Publication objects containing the parsed data
        '''
        if filepath is None:
            return None
        ftype = filepath.split('.')[-1].lower()
        if ftype in parsers:
            return parsers[ftype].parse_file(filepath)
        else:
            logging.error(f"could not parse the file {filepath}")
            raise Exception(f"could not parse the file {filepath}")

publication_parser = PublicationParser()
