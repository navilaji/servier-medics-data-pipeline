from drug_analysis_pipeline.src.service.publication_info_service import publication_info_service as pub_service
from drug_analysis_pipeline.src.util.adhoc_analysis import adhoc_analyser
from drug_analysis_pipeline.src.model.publication import Publication
from drug_analysis_pipeline.src.model.drug  import Drug

#test data
DRUGS = [Drug("0","DRUG0"),Drug("1","DRUG1"),Drug("2","DRUG2"),Drug("3","DRUG3"),Drug("4","DRUG4")]
P1 = Publication("1","drug1 bla bla bla drug2 drug4 no no no ...","2020-01-01", "J1")
P2 = Publication("2","drug3 bla bla bla no no no ...","2020-01-02", "J2")
P3 = Publication("3","drug3 bla bla bla drug2 no no no ...","2020-01-03", "J1")
P4 = Publication("4","drug2 bla bla bla drug4 no no no ...","2020-01-03", "J3")
P5 = Publication("5","Drug4 dRUg3","2020-01-04", "J4")
C1 = Publication("N1","dRUg3","2020-01-05", "J1")
C2 = Publication("N2"," drug4  drug1 drug1 drg4","2020-01-05", "J4")
P6 = Publication("5","Drug1 dRUg2 drug3 drug4 DRUG0","2020-01-04", "J6")

PUBMEDS = [P1,P2,P3,P4,P5]
CL_TS = [C1,C2]

def test_find_mentions():
    result = pub_service.find_mentions(DRUGS[0].name,[P1,P2,P3])
    assert len(result[0])==0
    assert len(result[1])==0

    result = pub_service.find_mentions(DRUGS[1].name,PUBMEDS)
    assert len(result[0])==1
    assert len(result[1])==1
    pubs = result[0]
    assert pubs[0]["title"] == "drug1 bla bla bla drug2 drug4 no no no ..."
    jlist = result[1]
    assert jlist[0]["journal"] == "J1"

    result = pub_service.find_mentions(DRUGS[3].name,PUBMEDS)
    assert len(result[0])==3
    assert len(result[1])==3
    pubs = result[0]
    assert pubs[0]["title"] == "drug3 bla bla bla no no no ..."
    jlist = result[1]
    assert jlist[0]["journal"] == "J2"
    assert pubs[2]["publication_date"] == "2020-01-04"
    assert jlist[2]["journal"] == "J4"

def test_graph_generation():
    graph = pub_service.generate_drug_pub_graph(DRUGS, PUBMEDS, CL_TS)
    assert graph is not None
    assert len(graph["DRUG3"]["journals"])==4
    assert len(graph["DRUG3"]["clinical_trials"])==1
    assert len(graph["DRUG3"]["pubmeds"])==3
    assert len(graph["DRUG1"]["journals"])==2
    assert len(graph["DRUG1"]["clinical_trials"])==1
    assert len(graph["DRUG1"]["pubmeds"])==1
    assert len(graph["DRUG0"]["journals"])==0
    assert len(graph["DRUG0"]["clinical_trials"])==0
    assert len(graph["DRUG0"]["pubmeds"])==0
    assert len(graph["DRUG2"]["journals"])==3
    assert len(graph["DRUG2"]["clinical_trials"])==0
    assert len(graph["DRUG2"]["pubmeds"])==3

def test_adhoc_analyser():
    graph = pub_service.generate_drug_pub_graph(DRUGS, PUBMEDS, CL_TS)
    result = adhoc_analyser.find_best_publisher(graph)
    assert result[0]=="j1"
    assert result[1]==4

    graph = pub_service.generate_drug_pub_graph(DRUGS, [P2,P3,P4,P5], CL_TS)
    result = adhoc_analyser.find_best_publisher(graph)
    assert result[0]=="j4"
    assert result[1]==3

    graph = pub_service.generate_drug_pub_graph(DRUGS, [P2,P3,P4,P5,P6], CL_TS)
    result = adhoc_analyser.find_best_publisher(graph)
    assert result[0]=="j6"
    assert result[1]==5
