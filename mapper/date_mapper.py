from datetime import datetime

pattern_1 = "%d/%m/%Y"
pattern_2 = "%Y-%m-%d"
pattern_3 = "%d %B %Y"

class DateMapper:

    def get_datepattern(self, str):
        if str is None:
            return None
        elif len(str.split("/")) == 3:
            return pattern_1
        elif len(str.split("-")) == 3:
            return pattern_2
        elif len(str.split(" ")) == 3:
            return pattern_3
        else:
            return None

    def map_to_date(self, str):
        pattern = self.get_datepattern(str)
        if pattern is None:
            return None
        try:
            return datetime.strptime(str, pattern).strftime(pattern_2)
        except:
            raise Exception(f"could not convert {str} to datetime!")

date_mapper = DateMapper()
