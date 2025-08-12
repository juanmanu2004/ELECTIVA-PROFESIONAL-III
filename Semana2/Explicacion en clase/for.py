def calcular_bono(lista):
    
    for i in range(len(lista)):
        lista[i] = lista[i]*2
        
    return lista

lista = [1200,3400,2300,1800]

calcular_bono(lista)