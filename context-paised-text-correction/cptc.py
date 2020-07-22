import json
#v0.02
"""
in:
student aswer
model answer(s)
key words

out:
degree based on smilarity



proc:
parse
find annomlies
nomait corrections
compare 

libraries: 
nltk 
pyspellchecker
problems:
nlp not effcient neither am i
how to collect the degree 
uncertinty
"""

class case:
    def __init__(self,studentanswer:str,modelanswers:list,keywords:list):
        self.student_Answer=studentanswer
        self.model_Answers=modelanswers
        self.Keywords=keywords

    def _prepare_answers(self):
        """
        toknise student and model answers
        """
        pass

    def _load_dict(self,location):
        """
        load dect to add to possible correction even it is not in keywords
        """
        pass

    def _load_json_from_file(self,location:str):
        with open('data.json') as f:
            data = json.load(f)
        #jso=json.dumps(data)
        return data
    def _export_json_file(self,file,location):
        with open('new.json', 'w') as json_file:
            json.dump(file, json_file,indent=4,sort_keys=True)

    def _correct(self):
        """
        for each wrong word in student answer see if a correction nomait is in keywords or at least correct it to some thing related to the context 
        """
        pass

    def _nomait(self,word:str):
        """
        get the most likly correction of certin word 
        """
        pass

    def get_degree(self):
        """
        some math to convert our data into numbers
        """
        pass

c=case("i like red . i do not like blue",["i like red . i do not like blue","i hate blue but not red"],["like_red","hate_blue"])