import os
import json

SURVEY_KEY = "survey.json"
RESULTS_KEY = "results.json"
PROMT_DATASETS_KEY = "promt_datasets.json"

def save_dict(value, key = SURVEY_KEY):
    print(f"Saving: {value}")
    out_file = open(key, "w")
    json.dump(value,out_file)
    out_file.close()

def save_results(value):
    save_dict(value, RESULTS_KEY)

def save_survey(value):
    save_dict(value, SURVEY_KEY)

def retrieve(key):
    if os.path.isfile(key):
        in_file = open(key, "r")
        result = json.load(in_file)
        in_file.close()
        return result
    else:
        # return an empty array if file does not exist
        return []

def get_survey(key=SURVEY_KEY):
    return retrieve(key)

def get_results(key=RESULTS_KEY):
    return retrieve(key)

def get_promt_datasets(key=PROMT_DATASETS_KEY):
    return retrieve(key)

def append_results(value):
    results = get_results()
    updated_results = results.append(value)
    save_results(updated_results)