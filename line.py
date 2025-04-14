def line():
    
    import math
    
    coef_a=float(input("Ingrese el coeficiente A: "))
    coef_b=float(input("Ingrese el coeficiente B: "))
    coef_x1=float(input("Ingrese el coeficiente X1: "))
    coef_x2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {coef_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {coef_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coef_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coef_x2}\n")    
    
    print("Para la siguiente ecuación:")
    
    y1= (coef_a*coef_x1+coef_b)
    y2= (coef_a*coef_x2+coef_b)
    
    print(f"\t Y = {str(coef_a) + "X " + "+ " + str(coef_b)}\n")
    
    print("Dados los siguientes puntos:" + "\t")
    
    p1= (coef_x1, y1)
    p2= (coef_x2, y2)
    
    print("\t" + "P1 " + str(p1))
    print("\t" + "P2" + str(p2))
    
    print(f"\nLa distancia entre ellos es: {math.dist(p1, p2)}")
