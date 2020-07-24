import json
class my_JSON:
    def load_json_from_file(self,location:str)->dict:
        with open(location) as f:
            data = json.load(f)
        #jso=json.dumps(data)
        return data
    def export_json_file(self,file,location):
        with open(location, 'w') as json_file:
            json.dump(file, json_file,indent=4,sort_keys=True)
