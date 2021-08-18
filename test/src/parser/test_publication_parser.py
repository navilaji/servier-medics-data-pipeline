from src.parser.publication_parser import publication_parser

PUBMED_CSV = "test/resources/pubmed.csv"
PUBMED_JSON = "test/resources/pubmed.json"
CL_TRIAL_CSV = "test/resources/clinical_trials.csv"

def test_parsing_pubmed_csv():
    pubmeds = publication_parser.parse_publication_file(PUBMED_CSV)
    assert len(pubmeds)==8
    assert pubmeds[0].journal == "Journal of emergency nursing"
    assert pubmeds[0].id == '1'
    assert pubmeds[0].pub_date == "2019-01-01"
    assert pubmeds[4].journal == "American journal of veterinary research"
    assert pubmeds[4].title == "Appositional Tetracycline bone formation rates in the Beagle."
    assert pubmeds[4].id == '5'
    assert pubmeds[4].pub_date == "2020-01-02"
    assert pubmeds[5].pub_date == "2020-01-01"

def test_parsing_pubmed_json():
    pubmeds = publication_parser.parse_publication_file(PUBMED_JSON)
    assert len(pubmeds)==5
    assert pubmeds[1].journal == "The journal of maternal-fetal & neonatal medicine"
    assert pubmeds[1].id == '10'
    assert pubmeds[1].pub_date == "2020-01-01"
    assert pubmeds[3].id == '12'
    assert pubmeds[4].id == ''

def test_parsing_cl_trial_csv():
    cl_trials = publication_parser.parse_publication_file(CL_TRIAL_CSV)
    assert len(cl_trials)==8
    assert cl_trials[0].journal == "Journal of emergency nursing"
    assert cl_trials[0].id == "NCT01967433"
    assert cl_trials[0].pub_date == "2020-01-01"
    assert cl_trials[2].title == ""
    assert cl_trials[2].pub_date == "2020-01-01"
    assert cl_trials[4].title == "Preemptive Infiltration With Betamethasone and Ropivacaine for Postoperative Pain in Laminoplasty or  Laminectomy"
    assert cl_trials[5].pub_date == "2020-05-25"
    assert cl_trials[5].journal == ""
    assert cl_trials[6].id == ""
    assert cl_trials[7].journal == "Journal of emergency nursing"
