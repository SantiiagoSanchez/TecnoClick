class Carrito:
    def __init__(self, request):
        self.request = request
        self.sesion = request.sesion
        carrito=self.sesion.get("Carrito")
        if not carrito:
            carrito=self.sesion["Carrito"]={}
        else:
            self.carrito = carrito

    def addProducto(self, producto):
        if(str(producto.id) not in self.carrito.keys()):  #Si no esta en el carrito, lo va a añadir
            self.carrito[producto.id]= {
                "producto_id": producto.id,
                "Nombre": producto.Nombre,
                "Precio": str(producto.Precio),
                "Cantidad": 1,
                "Imagen": producto.Imagen.url
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["Cantidad"] = value["Cantidad"]+1 #Si ya esta en el carrito el producto, va a sumar la cantidad
                    break

        self.saveCarrito()

    def saveCarrito(self):
        self.sesion["Carrito"]=self.carrito
        self.sesion.modified = True

    def deleteProducto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.saveCarrito()

    def restarProducto(self, producto):
        for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["Cantidad"] = value["Cantidad"]-1 #Si ya esta en el carrito el producto, va a restar la cantidad
                    if value["Cantidad"]<1:
                        self.deleteProducto(producto)
                    break

        self.saveCarrito()
    
    def limpiarCarrito(self):
        self.sesion["Carrito"]={}
        self.sesion.modified = True
