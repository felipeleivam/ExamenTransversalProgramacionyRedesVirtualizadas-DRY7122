while True:
    vlan = input("Ingresa número de VLAN o 's' para salir: ")

    if vlan == "s" or vlan == "S":
        break

    es_entero = True
    for caracter in vlan:
        if caracter < "0" or caracter > "9":
            es_entero = False

    if es_entero == True:
        vlan_num = int(vlan)
        if vlan_num >= 1 and vlan_num <= 1005:
            print("VLAN normal")
        elif vlan_num >= 1006 and vlan_num <= 4094:
            print("VLAN extendida")
        else:
            print("VLAN fuera de rango (Debe ser entre 1 y 4094)")
    else:
        print("Debes ingresar solo números.")