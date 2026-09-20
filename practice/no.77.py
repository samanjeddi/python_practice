class runner():
    def __init__(self, name):
        self.name = name

    def action(self):
        return(f"{self.name} is running.")

class cycling():
    def __init__(self, name):
        self.name = name

    def action(self):
        return(f"{self.name} is cycling.")

saman = runner('saman')
asal = cycling('asal')

for person in [saman, asal]:
    print(person.action())