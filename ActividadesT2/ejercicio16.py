def IntentosPin(pin):
    pin_almacenado = 203012
    if pin != pin_almacenado:
        for i in range (1, 3):
            print("TE HAS EQUIVOCADO, INTENTALO DE NUEVO: ")
            pin = int(input("INTRODUCE OTRA VEZ EL PIN: "))
        if pin != pin_almacenado:
            print ("YA NO TIENES MÁS INTENTOS")
        else:
            print("HAS ENTRADO")
    else:
        print("EL PIN ES CORRECTO")


pin = int(input("INTRODUCE UN PIN PARA ENTRAR: "))

IntentosPin(pin)