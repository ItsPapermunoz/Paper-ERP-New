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

x = 12352

if x > 0:
  print('X is not 0')
else:
  print('x is 0')


'''

with open("data.dat", "rb") as file:
  persons = pkl.load(file)

Person.id = persons[-1].id + 1

simon = Person('Rudolph', 38, 250)
persons.append(simon)
rodrigo = Person('Ryan', 45, 150)
persons.append(rodrigo)

for item in persons:
  item.id_person()

with open('data.dat', 'wb') as file:
  pkl.dump(persons, file)

'''