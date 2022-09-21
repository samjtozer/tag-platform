import json


class JsonLinesLoader:

    def __init__(self):
        self.data = None
        self.number_items = None

    def load(self, file_location):
        with open(file_location, "r") as infile:
            self.data = [json.loads(line) for line in infile]
        self.number_items = len(self.data)

    def load_item(self, idx: int):
        if int(idx) >= self.number_items:
            return {"error": "You have requested a job item which does not exist"}
        return self.data[int(idx)]
