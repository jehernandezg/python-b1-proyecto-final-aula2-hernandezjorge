from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    
   
  @abstractmethod
  def describe(self):
      pass

class Cashier(User): 
  def __init__(self,dni:str,name:str,age:int,timeTable:str,salary:float):
    #Write your code here
        # usamos super() para inicializar los atributos de la clase padre (User)
        super().__init__(dni, name, age)

        # Atributos propios de Cashier
        self.timeTable = timeTable
        self.salary = salary
        pass      
 
  def describe(self):
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."

class Customer(User):
  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
    #Write your code here

        # usamos super() para inicializar los atributos de la clase padre (User)
        super().__init__(dni, name, age)

        # Atributos propios de Customer
        self.email = email
        self.postalCode = postalCode   
        pass


  def describe(self):
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"