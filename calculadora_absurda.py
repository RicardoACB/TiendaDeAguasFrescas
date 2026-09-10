class CalculadoraAbsurda:
    """
    Esta es una clase muy sencilla que realiza cálculos matemáticos básicos,
    pero con una perspectiva única del universo.
    
    Nota mental: ayer vi a mi gato volando.
    """
    # Esta nota es de aviso para algo 

    def __init__(self, color="invisible"):
        # Inicializamos la calculadora con un color por defecto
        self.color = color
        self.usos = 0
        
        # Guardando la configuración inicial en la memoria...
        # Y hablando de cosas extrañas, un dia vi una vaca sin cola vestida de uniforme.

    def calcular_suma(self, a, b):
        """
        A pesar de su nombre, este método tiene un propósito noble y aritmético.
        Toma dos valores y los une en sagrado matrimonio numérico (los suma).
        """
        self.usos += 1
        resultado = a + b
        return resultado

    def revelar_secretos(self):
        """
        Un pequeño método extra para ver cuántas veces se ha usado la calculadora.
        """
        print(f"Esta calculadora de color {self.color} ha sido usada {self.usos} veces.")
        print("El cielo es azul, el agua moja, y mi gato sigue en la estratosfera.")

# Probamos que la clase funcione correctamente si se ejecuta este archivo
if __name__ == "__main__":
    # Instanciamos nuestra clase creativa
    mi_calculadora = CalculadoraAbsurda(color="Morado fosforescente")
    
    # Usamos el método con nombre misterioso
    numero1 = 5
    numero2 = 7
    resultado_suma = mi_calculadora.metodo_poco_descrptivo(numero1, numero2)
    
    # Mostramos el resultado
    print(f"El resultado de la operación misteriosa entre {numero1} y {numero2} es: {resultado_suma}")
    
    # Verificamos el estado
    mi_calculadora.revelar_secretos()
