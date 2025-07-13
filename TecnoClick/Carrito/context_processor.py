def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.sesion["Carrito"].items():
            total = total + (float(value["Precio"]*value["Cantidad"]))
        
    return {"importe_total_carro": total}