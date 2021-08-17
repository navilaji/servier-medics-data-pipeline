from model.publication import Publication
from .date_mapper import date_mapper

class PublicationMapper:

    def map_csv_row(self, row)-> Publication:
        return Publication(row[0],
                      row[1],
                      date_mapper.map_to_date(row[2]),
                      row[3])

    def map_json_obj(self, json_obj) -> Publication:
        return Publication(json_obj["id"],
                      json_obj["title"].strip().encode("ascii", "ignore").decode("utf-8"),
                      date_mapper.map_to_date(json_obj["date"].strip()),
                      json_obj["journal"].strip().encode("ascii", "ignore").decode("ascii"))

publication_mapper = PublicationMapper()
