#Write your code here

from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        # Ajustado a 'Wrapping' para coincidir con el ejemplo de consola
        return f"Wrapping: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
    def pack(self) -> str:
        return "Food Wrap Paper"
    def material(self) -> str:
        return "Aluminium"

class Bottle(FoodPackage):  
    def pack(self) -> str:
        return "Bottle"
    def material(self) -> str:
        return "Plastic"
      
class Glass(FoodPackage):  
    # Asumiendo vaso de cartón para bebidas calientes/tés según descripción
    def pack(self) -> str:
        return "Cup"
    def material(self) -> str:
        return "Cardboard"

class Box(FoodPackage):  
    def pack(self) -> str:
        return "Box"
    def material(self) -> str:
        return "Cardboard"