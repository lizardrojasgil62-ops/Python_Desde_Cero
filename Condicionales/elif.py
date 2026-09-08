ingreso_mensual = 100000
gasto_mensual = 8000

#if anidado y elif

if ingreso_mensual > 10000:
    if gasto_mensual - ingreso_mensual < 0:
        print("estas perdiendo")
    elif gasto_mensual - ingreso_mensual > 3000:
        print("tas bien")
    else:
        print("estas gastando una banda")
    
elif ingreso_mensual > 1000:   
    print("estas muy bien")
    
elif ingreso_mensual > 500:   
    print("estas cerca del avismo")
    
else:
    print("estas jodido")
    
