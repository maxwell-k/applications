import json

FILE = "alpine.yaml"
TEMPLATE = "- import_playbook: packages/{}/main.yaml"

if __name__ == "__main__":
    with open(FILE) as file_:
        items = json.loads(file_.read())
    for key in items.keys():
        print(TEMPLATE.format(key))
