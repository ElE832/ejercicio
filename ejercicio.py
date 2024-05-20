def es_par_o_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."

# Ejemplo de uso
numero = int(input("Introduce un número: "))
print(es_par_o_impar(numero))