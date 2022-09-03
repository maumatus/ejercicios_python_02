print("calculo numeros primos hasta numero escrito")

num = int(input("ingresa numero:  "))

if num < 2:

    print("alerta, malfunción del sistema, evacuen el recinto")

else:

    for i in range(1, num):
        prim = prim / i

print(prim)
