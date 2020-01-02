# https://docs.python.org/3/library/exceptions.html

class person:
    def __init__(self, age, name):
        if type(age)!=int:
            raise Exception("Invaild Age: {}".format(age))
        if age<0:
            raise Exception("Invaild Age: {}".format(age))
        if type(name)!=str:
            raise Exception("Name not string: {}".format(name))

        self.name=name
        self.age=age

x=person("-9", 1243)
