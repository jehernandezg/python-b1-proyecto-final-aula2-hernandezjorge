"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
import sys
from products.product import Drink, Hamburger, HappyMeal, Soda
from users import Cashier, Customer 
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from util.file_manager import CSVFileManager
from orders.order import Order

from users import *

    
class PrepareOrder:
 #Write your code here

    # Método estático para no requerir instanciar la clase PrepareOrder
    @staticmethod
    def main():
        print("--- SISTEMA DE COMIDA RÁPIDA ---\n")
        
        # 1. Leer archivos CSV
        print("Cargando datos del sistema...")
        fm_cashiers = CSVFileManager("data/cashiers.csv")
        fm_customers = CSVFileManager("data/customers.csv")
        fm_hamburgers = CSVFileManager("data/hamburgers.csv")
        fm_sodas = CSVFileManager("data/sodas.csv")
        fm_drinks = CSVFileManager("data/drinks.csv")
        fm_happymeals = CSVFileManager("data/happyMeal.csv")

        # Leer DataFrames
        df_cashiers = fm_cashiers.read()
        df_customers = fm_customers.read()
        df_hamburgers = fm_hamburgers.read()
        df_sodas = fm_sodas.read()
        df_drinks = fm_drinks.read()
        df_happymeals = fm_happymeals.read()

        # Verificar si la carga falló (DataFrames vacíos)
        if df_cashiers.empty or df_customers.empty:
            print("Error cargando archivos críticos (cajeros o clientes). Verifique la carpeta 'data/'.")
            return

        # 2. Convertir a objetos
        # Cajeros
        c_conv = CashierConverter()
        cashiers_list = c_conv.convert(df_cashiers)
        
        # Clientes
        cust_conv = CustomerConverter()
        customers_list = cust_conv.convert(df_customers)
        
        # Productos
        p_conv = ProductConverter()
        hamburgers_list = p_conv.convert(df_hamburgers, Hamburger)
        sodas_list = p_conv.convert(df_sodas, Soda)
        drinks_list = p_conv.convert(df_drinks, Drink)
        happymeals_list = p_conv.convert(df_happymeals, HappyMeal)

        # Lista unificada
        all_products = hamburgers_list + sodas_list + drinks_list + happymeals_list

        print(f"Datos cargados: {len(cashiers_list)} cajeros, {len(customers_list)} clientes, {len(all_products)} productos.")

        # Mostrar Cajeros (Requerimiento)
        print("\n--- Cajeros Disponibles ---")
        c_conv.print(cashiers_list)

        # 3. Preparar Orden
        
        # a. Buscar cajero
        selected_cashier = None
        while selected_cashier is None:
            dni_in = input("\nIntroduce DNI del cajero (ej. 5001): ")
            for c in cashiers_list:
                # Comparamos como string para evitar errores de tipo
                if str(c.dni) == dni_in.strip():
                    selected_cashier = c
                    break
            if selected_cashier:
                print(f"Seleccionado: {selected_cashier.describe()}")
            else:
                print("Cajero no encontrado. Intente de nuevo.")

        # b. Buscar cliente
        selected_customer = None
        while selected_customer is None:
            dni_in = input("\nIntroduce DNI del cliente (ej. 1001): ")
            for c in customers_list:
                if str(c.dni) == dni_in.strip():
                    selected_customer = c
                    break
            if selected_customer:
                print(f"Seleccionado: {selected_customer.describe()}")
            else:
                print("Cliente no encontrado. Intente de nuevo.")

        # c. Inicializar Orden
        order = Order(selected_cashier, selected_customer)

        # d. Mostrar productos a vender
        print("\n--- MENÚ DE PRODUCTOS ---")
        p_conv.print(all_products)

        # e. Escoger y f. Agregar productos
        adding_products = True
        while adding_products:
            p_id = input("\nIntroduce ID del producto (ej. H1, G1): ")
            found_product = None
            for p in all_products:
                if str(p.id) == p_id.strip():
                    found_product = p
                    break
            
            if found_product:
                print(f"Producto seleccionado: {found_product.describe()}")
                order.add(found_product)
                
                answer = input("¿Desea agregar otro producto? (Si/No): ").lower()
                if answer not in ['si', 'yes', 'y', 's']:
                    adding_products = False
            else:
                print("Producto no encontrado.")

        # 4. Mostrar Orden Final
        order.show()

if __name__ == "__main__":
    PrepareOrder.main()
                

