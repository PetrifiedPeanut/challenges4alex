# Challenge 1 : Load the JSON string and return the value of "job"
# jsonstring = '{"name":"Billy", "age":25, "city":"London", "job":"being awesome"}'
import json
class challenge1:
    def run(self, jsonstring):
        y = json.loads(jsonstring)
        solution = y["job"]
        return solution
