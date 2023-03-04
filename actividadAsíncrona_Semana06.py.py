"""Integrantes:
1. Félix Mauricio Palacios Tejada 
2. Sonia Elizabeth Abrego Núñez
3. Carlos Ernesto Landaverde Quintanilla 
4. Iván Anderson Membreño Guardado
5. Marilyn Alexandra Menjívar Fuentes 
"""
    
#Suma(+):
"""Sumar 3 variables distintas y asignar el valor
a una cuarta variable."""

print("SUMA DE TRES NUMEROS REALES: ");
num1 = 23
num2 = 12
num3 = 9
resultadoSuma = num1 + num2 + num3
print("El resultado de la suma es:"+ str(resultadoSuma));
print("""
""")

#RESTA(-):
"""Restar 4 variables siendo
en la tercera variable más alta que la primera."""

print("RESTA DE CUATRO NUMEROS REALES: ");
var1 = 19
var2 = 5
var3 = 22
var4 = 3
resultadoResta = var1 - var2 - var3 - var4
print("El resultado de la resta es:"+ str(resultadoResta));
print("""
""")

#MULTIPLICACIÓN(*):
"""Multiplicar 2 variables, asignarlas a otra variable y esa variable
multiplicar por la segunda variable de suma y resta."""

print("MULTIPLICACION :");
cant1 = 5
cant2 = 3
resultadoMult = cant1 * cant2
print(resultadoMult);
print("El resultado de esta multiplicacion es de :"+ str(resultadoMult));
print("""
""")
print("""Multiplicacion del resultado anterior
      por la variable #2 de la suma :""");
resultado_dos = resultadoMult * num2
print(resultado_dos);
print("El resultado de esta multiplicacion es de :"+ str(resultado_dos));
print("""
""")
print("""Multiplicacion del resultado de la multiplicacion
      por la variable #2 de la resta :""");

resultado_tres = resultadoMult * var2
print(resultado_tres);
print("El resultado de esta multiplicacion es de :"+ str(resultado_tres));
print("""
""")

#EXPONENTE(**):
"""Sacar a la primera variable de la multiplicacion el
exponente de la segunda variable de la multiplicacion."""

print("EXPONENTE : ");
resultadoExponente = cant1 ** cant2;
print(resultadoExponente);
print("El resultado es de :"+ str(resultadoExponente));
print("""
""")

#MÓDULO(%):
"""Sacar el modulo de la primera variable de la suma
con la primera variable de la resta."""

print("MODULO : ");
resultado_modulo = num1 % var1
print(resultado_modulo);
print("El resultado del modulo es :"+ str(resultado_modulo));
print("""
""")

#DIVISIÓN(/):
"""Dividir la variable resultado del exponente
entre la variable resultado del módulo."""

print("DIVISION :");
total_division = resultadoExponente / resultado_modulo;
print(total_division);
print("El resultado de la division es de :"+ str(total_division));
print("""
""")
#DIVISIÓN ENTERA(//):
"""Realizar la division entera de la división normal"""
print("DIVISION ENTERA :");
total_division_entera = resultadoExponente // resultado_modulo;
print(total_division_entera);
print("El resultado de la division entera es de :"+ str(total_division_entera));
print("""
""")
print("");
