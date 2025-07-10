class Carro:
    def __init__(self, request):
        self.request = request
        self.sesion = request.sesion
        carrito=self.sesion.get("Carrito")
        if not carrito:
            carrito=self.sesion["Carrito"]={}
        else:
            self.carrito = carrito

    def addProducto(self, producto):
        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]= {
                "producto_id": producto.id,
                "Nombre": producto.Nombre,
                "Precio": str(producto.Precio),
                "Cantidad": 1,
                "Imagen": producto.Imagen.url
            }