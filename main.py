# Imports

import pickle as pkl

# classes


class Address():

  def __init__(self, address, address_2, city, state, country, cp):
    self.address = address
    self.address_2 = address_2
    self.city = city
    self.state = state
    self.country = country
    self.cp = cp

  def details(self):
    print("Calle: {} Colonia: {}\nCiudad: {} Estado: {}\nPaís: {}\nCódigo Postal: {}".format(self.address, self.address_2, self.city, self.state, self.country, self.cp))

class Company():
  company_id = 1

  def __init__(self, name, address, bal, rfc, isClient, isSupplier):
    self.id = Company.company_id
    Company.company_id += 1
    self.address = address
    self.bal = bal
    self.rfc = rfc
    self.isClient = isClient
    self.isSupplier = isSupplier

  def payment(self, amount):
    self.bal -= amount

  def charge(self, amount):
    self.bal += amount

  def details(self):
    print("----- {} - {} -----".format(self.id, self.name))
    print("RFC: " + self.rfc)
    self.address.details()
    print("Saldo: ${}".format(self.bal))

# Functions
    
def menu(options):
  i = 1
  for option in options:
    print("{}. {}.".format(i, option))
    i += 1
  print("0. Go Back")
  sel = int(input("Seleccione una opción: "))
  return sel

def address_new():
  address = input("Ingrese Calle y Número:")
  address_2 = input("Ingrese Colonia:")
  city = input("Ingrese Ciudad: ")
  state = input("Ingrese Estado: ")
  country = input("Ingrese País: ")
  cp = input("Ingrese Código Postal: ")
  new_address = Address(address, address_2, city, state, country, cp)
  return new_address
  
def client_new(db_client):
  print("----- Nuevo Cliente -----")
  name = input("Ingrese Razón Social: ")
  rfc = input("Ingrese RFC: ")
  address = address_new()
  bal = float(input("Ingrese saldo inicial del cliente: "))
  company_type = int(input("Ingrese 1 si es cliente o 2 si es proveedor: "))
  if company_type == 1:
    isClient = True
    isSupplier = False
  elif company_type == 2:
    isClient = False
    isSupplier = True
  new_client = Company(name, address, bal, rfc, isClient, isSupplier)
  db_client.append(new_client)

def client_lookup(db_client, lookup=0):
  
  for client in db_client:
    
  
# Variables

menu_main = ["CRM"]
menu_crm = ["All Clients", "New Client", "Delete Client"]
db_client = []

# Main
