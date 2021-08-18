class PublicationInfoService:
    '''
    This class is responsible for generating a graph showing the relation between the drugs and medical publications,
    clinical trialas, and journals.
    '''

    def find_mentions(self, drug_name, pub_list):
        '''
        Finds the list of medical publication or clinical trials in which the drug is mentions. It also generates the list
        of journals mentioning the drug along with its publication date.
        :param drug_name: the name of the drug
        :param pub_list: the list of the Publications
        :return: a tuble containing first the list of medical publication or clinical trials mentioning the drug and their publication dates,
        and the list of journals mentioning the drug and their publication dates
        '''
        publications = []
        journals = []
        for pub in pub_list:
            if drug_name in pub.title.upper():
                publications.append({
                    "title":pub.title,
                    "publication_date":pub.pub_date
                })
                journals.append({
                    "journal":pub.journal,
                    "publication_date":pub.pub_date
                })
        return (publications, journals)

    def generate_drug_pub_graph(self, drugs, pubmeds, cl_trials):
        '''
        Generates a json object (dict) containing the drug and the list of clinical trials, medical publications, and journals
        mentioning them.
        :param drugs: list of drugs @Drug
        :param pubmeds: list of medical publications @Publication
        :param cl_trials: list of clinical trials @Publication
        :return: json object (dict) containing the relation between the drugs and clinical trials, medical publications, and journals
        '''
        graph = {}
        for drug in drugs:
            drug_name = drug.name
            drug_info = {
                "journals":[],
                "pubmeds": [],
                "clinical_trials":[]
            }

            pubmed_journals = self.find_mentions(drug_name, pubmeds)
            drug_info["pubmeds"] = pubmed_journals[0]
            drug_info["journals"].extend(pubmed_journals[1])

            cltrial_journal = self.find_mentions(drug_name, cl_trials)
            drug_info["clinical_trials"] = cltrial_journal[0]
            drug_info["journals"].extend(cltrial_journal[1])

            graph[drug_name] = drug_info
        return graph

publication_info_service = PublicationInfoService()
