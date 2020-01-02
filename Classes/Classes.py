class person:
    def __init__(self, age, name):
        self.age=int(age)
        self.name=str(name)

    def info(self):
        x="Name: {name}\nAge: {age}".format(name=self.name, age=self.age)
        return x


Jush=person(123425364, "Jush")
print(Jush.info())
