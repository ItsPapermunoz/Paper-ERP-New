import pickle as pkl


class Person():
  id = 1

  def __init__(self, name, age, bal):
    self.id = Person.id
    Person.id += 1
    self.name = name
    self.age = age
    self.bal = bal

  def id_person(self):
    print("-----ID Number {} -----".format(self.id))
    print("My name is {}, Im {} years old, I have ${} cash on me.".format(
      self.name, self.age, self.bal))


persons = []
with open("data.dat", "wb") as file:
  pkl.dump(persons, file)
