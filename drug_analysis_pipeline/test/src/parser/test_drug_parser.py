from drug_analysis_pipeline.src.parser.drug_parser import drug_parser

DRUG_CSV = "drug_analysis_pipeline/test/resources/drugs.csv"

def test_parsing_drugs_csv():
    drugs = drug_parser.parse_drugs_from_csv(DRUG_CSV)
    assert len(drugs)==7
    assert drugs[0].name == "DIPHENHYDRAMINE"
    assert drugs[4].name == "EPINEPHRINE"
    assert drugs[5].id == "6302001"
    assert drugs[6].id == "R01AD"

