def importe_total_carro(request):
    total = 0
    carrito = request.session.get("Carrito", {})  # <-- clave aquí
    for key, value in carrito.items():
        total += float(value["Precio"]) * value["Cantidad"]
    return {"importe_total_carro": total}