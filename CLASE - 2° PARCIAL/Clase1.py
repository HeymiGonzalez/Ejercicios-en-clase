
#--- CLASE SEMANA 12(2021-08-16) ---
class Empresa: 
    def __init__(self, nom='El baraton', dir='Juan Montalvo', tel='042972274', ruc='09999') :    
        self.nombre = nom                        
        self.direccion = dir                     
        self.telefono = tel           
        self.ruc =  ruc

    def mostrarEmpresa(self):
        print('Empresa: {:20} RUC: {} '.format(self.nombre, self.ruc))

 
class Cliente:
    def __init__(self, nom, ced, tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono = tel

    def mostrarCliente(self):
        print(self.nombre, self.cedula, self.telefono)


class ClienteCorporativo(Cliente):
    def __init__(self, nom, ced, tel ,contrato):
        super().__init__(nom, ced, tel)
        self.__contrato = contrato
        
    @property               
    def contrato(self):
        return self.__contrato

    @contrato.setter       
    def contrato(self, valor):
        if valor:
            self.__contrato = valor
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):       
        print(self.nombre, self.__contrato)   


class ClientePersonal(Cliente):
    def __init__(self, nom, ced, tel ,promocion= True):
        super().__init__(nom, ced, tel)
        self.__promocion = promocion
        
    @property             
    def promocion(self):
        if self.__promocion == True:    
            return '10 porciento de descuento.'
        else:
            return 'No hay promocion'

    def mostrarCliente(self):      
        print(self.nombre, self.promocion)


# emp = Empresa()
# emp.mostrarEmpresa()
# print(emp.nombre)

clien1 = ClienteCorporativo('Heymi','09328486','09934642','#0001')
clien1.mostrarCliente()
print(clien1.nombre)
clien1.contrato = '#0002'
print(clien1.contrato)
