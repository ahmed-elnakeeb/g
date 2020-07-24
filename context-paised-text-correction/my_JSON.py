import json
class my_JSON:
    def _load_json_from_file(self,location:str):
        with open('data.json') as f:
            data = json.load(f)
        #jso=json.dumps(data)
        return data
    def _export_json_file(self,file,location):
        with open('new.json', 'w') as json_file:
            json.dump(file, json_file,indent=4,sort_keys=True)
