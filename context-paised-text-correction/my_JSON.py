import json
from  spellchecker import SpellChecker
class my_JSON:
    def load_json_from_file(self,location:str)->dict:
        with open(location) as f:
            data = json.load(f)
        #jso=json.dumps(data)
        return data
    def export_json_file(self,file,location):
        with open(location, 'w') as json_file:
            json.dump(file, json_file,indent=4,sort_keys=True)
dic={}
with open("keywords.txt", 'r') as st:
    my_keys= st.read()
    my_keys=my_keys.split()
    for key in my_keys:
        dic[key]=100000
    j=my_JSON()
    j.export_json_file(dic,"mydic.json")
spell=SpellChecker()
spell.word_frequency.load_dictionary("mydic.json")