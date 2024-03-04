class Pizza:
    # Atributos de clase
    ingredientes_proteicos_posibles = ['pollo', 'vacuno', 'carne vegetal']
    ingredientes_vegetales_posibles = ['tomate', 'aceituna', 'champiñones']
    tipos_masa_posibles = ['tradicional', 'delgada']

    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.es_pizza_valida = None

    @classmethod
    def validar_elemento(cls, elemento, valores_posibles):
        return elemento in valores_posibles

    def realizar_pedido(self):
        # Solicitar al usuario ingresar los ingredientes y tipo de masa
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ").lower()
        self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal: ").lower()
        self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ").lower()

        # Validar los ingredientes y tipo de masa
        proteico_valido = self.validar_elemento(self.ingrediente_proteico, self.ingredientes_proteicos_posibles)
        veg_1_valido = self.validar_elemento(self.ingrediente_vegetal_1, self.ingredientes_vegetales_posibles)
        veg_2_valido = self.validar_elemento(self.ingrediente_vegetal_2, self.ingredientes_vegetales_posibles)
        masa_valida = self.validar_elemento(self.tipo_masa, self.tipos_masa_posibles)

        # Almacenar si la pizza es válida o no
        self.es_pizza_valida = proteico_valido and veg_1_valido and veg_2_valido and masa_valida


if __name__ == "__main__":
    pizza_pedido = Pizza()
    pizza_pedido.realizar_pedido()

    if pizza_pedido.es_pizza_valida:
        print("Pedido de pizza válido, el valor es $10000 ¡Disfrute su pizza!")
    else:
        print("Pedido de pizza no válido. Revise los ingredientes y tipo de masa.")
