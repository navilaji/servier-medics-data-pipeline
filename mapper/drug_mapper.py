from model.drug import Drug
class DrugMapper:
    def map_row(self, row)-> Drug:
        return Drug(row[0].strip(),
                    row[1].strip())

drug_mapper = DrugMapper()
