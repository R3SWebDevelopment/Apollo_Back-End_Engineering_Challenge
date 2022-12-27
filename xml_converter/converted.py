import xmltodict
import json


def convert_to_json(xml_content):
    parse_obj = xmltodict.parse(xml_content)
    json_string = json.dumps(parse_obj)

    return json.loads(json_string)
