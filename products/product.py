from abc import ABC, abstractmethod
#Write your code here
from food_package import FoodPackage, Wrapping, Bottle, Glass, Box


class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass  

class Hamburger(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguesa"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
    
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Soda"

    def foodPackage(self) -> FoodPackage:
        # Soda - Vaso de carton
        return Glass()
    pass

class Drink(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)

    def type(self) -> str:
        return "Drink"

    def foodPackage(self) -> FoodPackage:
        # Bebida gebnerica - Botella
        return Bottle()

    pass

class HappyMeal(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)

    def type(self) -> str:
        return "HappyMeal"
    
    def foodPackage(self) -> FoodPackage:
        # Cajita Fe;iz - caja
        return Box()
    pass