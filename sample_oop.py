from os import name


class Dep:
    def __init__(self, dep, name, age):
        self.dep = dep
        self.name = name
        self.age = age
    def enter(self, i):
        self.file = open("enter.txt", "a")
        self.file.write(f'''
        -------------------{i}--------------------------
        Department : {self.dep}
        Name       : {self.name}
        Age        : {self.age}

''')
        self.file.close()

n = int(input("no.of students : "))
i = 1

while n>0:
      print(f"""------------{i}-----------------""")
      name = input("name : ")
      dep = input("dep : ")
      age = input("age : ")
      data = Dep(dep, name, age)
      data.enter(i)
      i = i+1
      n = n-1

        
        