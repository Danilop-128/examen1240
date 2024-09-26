#Crear la clase 
class contacto1240:
    id_contacto1240=0
    nombre1240=""
    apellidos1240=""
    email1240=""
    celular1240=0
    direccion1240=""
    sucursal1240=""

#Crear funciones
    def mostrar_contacto1240(self):
        print(f"id: {self.id_contacto1240}")
        print(f"Nombre: {self.nombre1240}")
        print(f"Apellidos: {self.apellidos1240}")
        print(f"E-mail: {self.email1240}")
        print(f"Celular: {self.celular1240}")
        print(f"Dirección: {self.direccion1240}")
        print(f"Sucursal: {self.sucursal1240}")

    def listar_empleados1240(self):
        empleados1240=["Rebecca López", "Sonia Jimenez", "Manuel Gardea", "Gerardo Chavira", "Emma Zapata", "Diego Jaquez", "Daniela Rodriguez"]
        print(empleados1240)
        for e in empleados1240:
            print(e)

    def tupla_proveedores1240(self):
        proveedores1240=("Gael Ortiz", "Josefina Durango", "Isai Espinosa", "Edgar Torres", "Monica Sosa", "Renata Reyes", "Araceli Vizcarra")
        for p in proveedores1240:
            print(p)

    def diccionario_productos_precio1240(self):
        precios1240={"Bolsa MK: " : "3000 pesos mx", "Bolsa Guess:" : "700 pesos mx", "Bolsa SM: " : "5000 pesos mx", "Bolsa GG: " : "25000 pesos mx",
                "Bolsa Coach: " : "8000 pesos mx", "Bolsas reaven: " : "600 pesos mx", "Bolsa LYV: " : "30000 pesos mx"}
        for x,y in precios1240.items():
            print(x,y)

    def altas1240(self):
        print("La operación se realizó correctamente")

    def bajas1240(self):
        print("La operacion se borró correctamente")

#Crear el objeto
objetoContacto1240=contacto1240()

#Asignar datos a los atributos
objetoContacto1240.id_contacto1240=22308051281240
objetoContacto1240.nombre1240= "Daniela"
objetoContacto1240.apellidos1240= "López Chavira"
objetoContacto1240.email1240= "a.22308051281240@cbtis128.edu.mx"
objetoContacto1240.celular1240= 6567824723
objetoContacto1240.direccion1240= "Calle Uva, 1234-45"
objetoContacto1240.sucursal1240= "Única"

#Utilizar objetos
print("Información de contacto:  --1240")
objetoContacto1240.mostrar_contacto1240()

print("Lista de empleados:  --1240")
objetoContacto1240.listar_empleados1240()

print("Tupla de proveedores:  --1240")
objetoContacto1240.tupla_proveedores1240()

print("Diccionario de precios:  --1240")
objetoContacto1240.diccionario_productos_precio1240()

objetoContacto1240.altas1240()
objetoContacto1240.bajas1240()

