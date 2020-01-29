# returned a reversed string
class challenge1:
    def run(self, string):
        print(string)
        reversedString = string[::-1]
        print(reversedString)
        return reversedString





runner = challenge1()
runner.run("alex")