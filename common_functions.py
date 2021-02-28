import json
from os.path import join, dirname


def load_json_schema(path):
    """Loads a json file from a given relative path directory"""
    absolute_path = join(dirname(__file__), path)
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
