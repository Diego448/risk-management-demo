import json

class Utils:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def load(self):
        self.data = []
        try:
            with open(self.filename, 'r') as db:
                for registry in db:
                    data = json.loads(registry)
                    self.data.append(data)
        except FileNotFoundError as error:
            pass

    def save(self):
        with open(self.filename, 'w') as db:
            for registry in self.data:
                db.write(json.dumps(registry))
                db.write('\n')

    def add_data(self, new_data):
        if isinstance(new_data, dict):
            self.contactos.append(new_data)
        else:
            raise TypeError

    def get_registry(self, id):
        for registry in self.data:
            if registry['id'] == id:
                return registry
            else:
                continue
        return {}

def get_total_risk(risks):
    total_risk = 0
    for risk in risks:
        total_risk += int(risk['severity'])
    return total_risk