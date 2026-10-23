def funcion_dulceria_snacks():
   carrito=[]
   total=0
   print("BIENVENIDO A LA DULCERIA DEL CINE")
   while True:
      print("\n MENU PRINCIPAL")
      print("1. palomitas")
      print("2. refrescos")
      print("3. snacks")
      print("4. pagar y salir")
      opcion= input("¿que desea comprar(1-4)?: ")
      if opcion == "1":
         print("\n palomitas")
         print("1. pequeña-bs 15")
         print("2. medianas-bs 25")
         print("1. grandes-bs 35")
         tamaño=input("elija el tamaño: ")
         if tamaño in ["1","2","3"]:
            print("\n¿de que sabor las va a querer?")
            print("1. mantequilla")
            print("2. caramelo")
            print("3. mixto")
            sabor= input (" elija el sabor que mas le guste: ")
            if sabor == "1":
             nombre_sabor= " mantequilla"
            elif sabor == "2":
             nombre_sabor= "caramelo"
            else:
             nombre_sabor= "mixto"
            cant=int(input("cantidad: "))
            if tamaño == "1":
               precio= 15
               nombre_tamaño = "pequeña"
            elif tamaño == "2":
               precio = 25 
               nombre_tamaño = "mediana"
            else:
               precio = 35
               nombre_tamaño = "grande"
               
            subtotal= precio*cant
            carrito.append(f"{cant}x palomitas {nombre_tamaño}{nombre_sabor}-bs{subtotal}")
            total += subtotal
            print("!agregado¡")
      elif opcion == "2":
         print("\n REFRESCOS")
         print("1. Coca-Cola 500 ml- 12 bs")
         print("2. Fanta 500 ml- 12 bs")
         print("3. Sprite 500 ml- 12 bs")
         print("4. Agua 500 ml- 8 bs")

         tipo=input("elija su bebida: ")
         cant=int(input("cantidad: "))
         if tipo == "1":
          carrito.append(f"{cant}x Coca-Cola 500 ml-{12*cant}")
          total += 12 *cant
         elif tipo == "2":
            carrito.append(f"{cant}x Fanta 500 ml-{12*cant}")
            total += 12 * cant
         elif tipo == "3":
            carrito.append(f"{cant}x Sprite 500 ml-{12*cant}")
            total += 12 * cant
         elif tipo == "4":
            carrito.append(f"{cant}x Agua 500 ml-{8*cant}")
            total += 8 * cant
            print("!agregado¡")
      elif opcion == "3":
         print("\n SNACKS")
         print("1. Nachos con queso-20 bs")
         print("2.  Hot Dog-18 bs")
         print("3. Chocolate")

         tipo=input("elija su snack: ")
         cant=int(input("cantidad: "))
         if tipo == "1":
            carrito.append(f"{cant}x Nachos con queso {20*cant}")
            total += 20 *cant
         elif tipo == "2":
            carrito.append(f"{cant}x Hot Dog-{18*cant}")
            total += 18 * cant
         elif tipo == "3":
            carrito.append(f"{cant}x Chocolate {10*cant}")
            total += 10 * cant
            print("!agregado¡")
      elif opcion == "4":
         print("\n TICKET DE CINE")
         for producto in carrito:
            print(f"-{producto}")
            print(f"TOTAL: bs {total}")
            print("gracias por su compra y disfrute su pelicula ")
      break 
funcion_dulceria_snacks()        
          




             