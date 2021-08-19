from drug_analysis_pipeline.src.model.drug import Drug
class DrugMapper:
    '''
    This class is responsible for mapping the drug rows in csv files
    '''
    def map_row(self, row)-> Drug:
        '''
        Maps the drug's csv row into a Drug object
        :param row: the input csv row
        :return: Drug
        '''
        return Drug(row[0].strip(),
                    row[1].strip())

drug_mapper = DrugMapper()
