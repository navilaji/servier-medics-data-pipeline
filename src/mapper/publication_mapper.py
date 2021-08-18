from src.model.publication import Publication
from .date_mapper import date_mapper

class PublicationMapper:
    '''
    This class is responsible for mapping the medical publication and clinical trial data
    '''

    def map_csv_row(self, row)-> Publication:
        '''
        Maps the medical publication or clinical trials's csv row into a Publication object
        :param row: medical publication or clinical trials csv row
        :return: Publication
        '''
        return Publication(str(row[0]).strip(),
                      row[1].strip(),
                      date_mapper.map_to_date(row[2].strip()),
                      row[3].strip())

    def map_json_obj(self, json_obj) -> Publication:
        '''
        Maps the medical publication json row into a Publication object
        :param row: medical publication json row
        :return: Publication
        '''
        return Publication(str(json_obj["id"]),
                      json_obj["title"].strip(),
                      date_mapper.map_to_date(json_obj["date"].strip()),
                      json_obj["journal"].strip())

publication_mapper = PublicationMapper()
