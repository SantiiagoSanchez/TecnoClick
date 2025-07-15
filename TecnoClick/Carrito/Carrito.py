class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito=self.session.get("Carrito")
        if not carrito:
            carrito=self.session["Carrito"]={}
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
                    value["Precio"] = float(value["Precio"])+producto.Precio
                    break

        self.saveCarrito()

    def saveCarrito(self):
        self.session["Carrito"]=self.carrito
        self.session.modified = True

    def deleteProducto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.saveCarrito()

    def restarProducto(self, producto):
        for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["Cantidad"] = value["Cantidad"]-1 #Si ya esta en el carrito el producto, va a restar la cantidad
                    value["Precio"] = float(value["Precio"])-producto.Precio
                    if value["Cantidad"]<1:
                        self.deleteProducto(producto)
                    break

        self.saveCarrito()
    
    def limpiarCarrito(self):
        self.session["Carrito"]={}
        self.session.modified = True
