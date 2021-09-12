
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


#----CLASE SEMANA 12(2021-08-19) -----
 
class Articulo:
    secuencia = 0  
    Iva = 0.12   
    def __init__(self, descripcion, precio, stock):
        Articulo.secuencia +=1
        self.codigo = Articulo.secuencia   
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def mostrarArticulo(self):
        print(self.codigo, self.descripcion)


class detVenta:
    linea=0
    def __init__(self, articulo, cantidad):
        detVenta.linea += 1
        self.lineaDetalle = detVenta.linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad


class CabVenta:
    def __init__(self, factura, fecha, cliente, total=0):
        self.factura = factura
        self.fecha = fecha
        self.cliente = cliente
        self.total = total
        self.detalleVenta = []

    def aggDetalle(self, articulo, cantidad):
        detalle = detVenta(articulo, cantidad)
        self.total += detalle.precio * detalle.cantidad
        self.detalleVenta.append(detalle)



c1 = ClientePersonal('Jose', '0912313475', '0983757364')
c1.mostrarCliente()
articulo1 = Articulo('Aceite', 2,100)
articulo1.mostrarArticulo()

articulo2 = Articulo('Coca cola', 1,200)
articulo2.mostrarArticulo()

articulo3 = Articulo('Leche', 1.5,50)
articulo3.mostrarArticulo()
print(Articulo.Iva)
