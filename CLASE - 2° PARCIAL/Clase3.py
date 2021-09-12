from datetime import date


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


#----- CLASE SEMANA 13(2021-08-23) -----

    def mostrarVenta(self, empresaNombre, empresaRuc):
        print('Empresa: {:18} Ruc: {}'.format(empresaNombre,empresaRuc))
        print('Factura: {:15} Fecha: {}'.format(self.factura, self.fecha))
        self.cliente.mostrarCliente()
        print('Linea|Articulo    Precio|Cantidad|Subtotal')
        for det in self.detalleVenta:
            print('{:5}| {:15} {}| {:6} |{:7}'.format(det.linea, det.articulo.descripcion, det.precio, det.cantidad, det.precio*det.cantidad))
        print('Total Venta: {:28}'.format(self.total))


empresa = Empresa()
c1 =ClientePersonal('Jose', '0947584453', '094948838')
articulo1 = Articulo('Aceite', 2,100)
articulo2 = Articulo('Coca cola', 1,200)
today = date.today()
fecha = date(2021,8,15)
venta = CabVenta('#001', date.today(), c1)
venta.aggDetalle(articulo1,3)
venta.aggDetalle(articulo2,2)
venta.mostrarVenta(empresa.nombre, empresa.ruc)
    