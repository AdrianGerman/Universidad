class Empleado:
    def __init__(self,nombre,salario,edad):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad
    def getDatos(self):
        print( "Nombre:",self.nombre,"\nSalario:",self.salario,"\nEdad:",self.edad)


class Gerente(Empleado):
    def __init__(self,nombre,salario,edad,departamento):
        super().__init__(nombre,salario,edad)
        self.departamento = departamento
    def getDatos(self):
        print( "Nombre:",self.nombre,"\nSalario:",self.salario,"\nEdad:",self.edad,"\nDepartamento:",self.departamento)
    
        

nombre = input("Ingrese el nombre: ")
salario = float(input("Ingrese el salario: "))
edad = int(input("ingrese la edad: "))
departamento = input("Ingrese el departamento: ")

newEmpleado = Gerente(nombre,salario,edad,departamento)
print("-------------------------")
print("Datos del empleado")
newEmpleado.getDatos()
print("-------------------------")