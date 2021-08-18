import re

class StringUtil:

    def clean_text(self, text):
        '''
        removing the unwanted corrupt characters from the text such as \xc3 \x28 etc., and trimming the string
        :param text:
        :return:
        '''
        return re.sub(r'\\x[a-f0-9]{2}', '', text.strip())
string_util = StringUtil()
