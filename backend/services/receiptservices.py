from jsonschema import validate
import json,os,yaml,uuid

schema_file_path = os.path.join(os.path.dirname(__file__), 'receiptschema.json')
with open(schema_file_path, 'r') as schema_file:
    json_schema = json.load(schema_file)

def validate_schema(inputJson):
    isValid = True
    try:
        validate(inputJson, schema =json_schema) #Check if the schema is valid against the input
        return isValid
    except Exception as e:
        isValid = False   
    return isValid

def generate_id():
    receiptId =str(uuid.uuid1()) # Generates UUID based on the hostID and the current time
    return receiptId

def checkJsonisempty(json):
    for key, value in json.items():
        if value == "" or value is None or value == []:
            raise Exception  # Found an empty key
    # return False  # No empty keys found