from abc import ABC, abstractmethod
#Write your code here

from products.product import Product
from users.user import Cashier, Customer

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):

    def convert(self,dataFrame, *args) -> list:  
    #Write your code here
        cashiers = []
        for index, row in dataFrame.iterrows():
            # Asumiendo que las columnas del CSV coinciden con los nombres
            cashier = Cashier(
                dni=str(row['dni']),
                name=row['name'],
                age=int(row['age']),
                timetable=row['timetable'],
                salary=float(row['salary'])
            )
            cashiers.append(cashier)
        return cashiers

    pass

class CustomerConverter(Converter):
  #Write your code here
    def convert(self, dataFrame, *args) -> list:
        customers = []
        for index, row in dataFrame.iterrows():
            customer = Customer(
                dni=str(row['dni']),
                name=row['name'],
                age=int(row['age']),
                email=row['email'],
                postalcode=str(row['postalcode'])
            )
            customers.append(customer)
        return customers

    pass

class ProductConverter(Converter):
  #Write your code here
    def convert(self, dataFrame, *args) -> list:
        # *args[0] se espera que sea la Clase del producto (ej: Hamburger, Soda)
        product_class = args[0]
        products = []
        for index, row in dataFrame.iterrows():
            product = product_class(
                id=str(row['id']),
                name=row['name'],
                price=float(row['price'])
            )
            products.append(product)
        return products


    pass