class PublicationInfoService:

    def find_mentions(self, drug_name, pub_list):
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
