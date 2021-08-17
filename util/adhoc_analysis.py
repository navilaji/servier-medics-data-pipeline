from collections import Counter

class AdHocAnalyser:

    def find_best_publisher(self, publication_graph):
        journals = []
        for k,v in publication_graph.items():
            journals.extend(v["journals"])
        journals = list(map(lambda jinfo: jinfo["journal"].strip().lower(), journals))
        c = Counter(journals)
        return c.most_common(1)

adhoc_analyser = AdHocAnalyser()
