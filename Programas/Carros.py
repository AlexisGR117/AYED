def main():
    total_alta = 0
    total_media = 0
    total_baja = 0
    altas = 0
    medias = 0
    bajas = 0
    finalizar = 'no'
    consolidado =
    while finalizar == "no":
        tipo = input("Inserte la gama del vehículo:\n")
        ano = int(input("Año del vehículo:\n"))
        precio = int(input("¿Qué precio pide?\n"))
        if tipo == "alta":
            altas += 1
            if ano <= 2000:
                precio_final = precio - precio * 0.15
            elif ano > 2000 and ano < 2014:
                precio_final = precio - precio * 0.9
            else:
                precio_final = precio - precio * 0.4
            total_alta += precio_final
            print("El precio ofertado por el concesionario para su compra es:", precio_final)
        elif tipo == "media":
            medias += 1
            if ano <= 2000:
                precio_final = precio - precio * 0.18
            elif ano > 2000 and ano < 2014:
                precio_final = precio - precio * 0.13
            else:
                precio_final = precio - precio * 0.7
            print("El precio ofertado por el concesionario para su compra es:", precio_final)
            total_media += precio_final
        elif tipo == "baja":
            bajas += 1
            print("No se compran vehículos de gama baja")
        finalizar = input("¿Desea finalizar?\n")
    registros = bajas + medias + altas
    print("El programa se ejecutó:", registros, "veces")
    print("Gama alta")
    print("Total de registros ingresados:", altas)
    print("Total en precio de los vehículos", total_alta)
    print("Procentaje con respecto al total de registros:", (altas * 100) / registros)
    print("Gama media")
    print("Total de registros ingresados:", medias)
    print("Total en precio de los vehículos", total_media)
    print("Procentaje con respecto al total de registros:", (medias * 100) / registros)
    print("Gama baja")
    print("Total de registros ingresados:", bajas)
    print("Total en precio de los vehículos", total_baja)
    print("Procentaje con respecto al total de registros:", (bajas * 100) / registros)
main()