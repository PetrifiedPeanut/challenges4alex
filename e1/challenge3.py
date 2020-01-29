# return the name value from the json string
import json
class challenge3:
    def run(self, jsonstring):
        x = json.loads(jsonstring)
        name = x['name']
        return name



runner = challenge3()

name = runner.run('{"name":"tip"}')

print(name)


