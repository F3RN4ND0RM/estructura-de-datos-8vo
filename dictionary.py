class Dictionary:
    """
    Implementación de un diccionario (mapa clave → valor) utilizando
    la estructura interna dict de Python.

    Permite almacenar pares clave-valor con acceso eficiente.
    """

    def __init__(self):
        """
        Inicializa un diccionario vacío.
        """
        self._data = {}

    def set(self, key, value):
        """
        Inserta o actualiza un par clave-valor.

        Args:
            key: Clave del elemento.
            value: Valor asociado a la clave.
        """
        self._data[key] = value

    def get(self, key, default=None):
        """
        Obtiene el valor asociado a una clave.

        Args:
            key: Clave a buscar.
            default: Valor a retornar si la clave no existe.

        Returns:
            El valor asociado a la clave o el valor por defecto.
        """
        return self._data.get(key, default)

    def remove(self, key):
        """
        Elimina un elemento por su clave.

        Args:
            key: Clave a eliminar.

        Raises:
            KeyError: Si la clave no existe.
        """
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        del self._data[key]

    def contains(self, key):
        """
        Verifica si una clave existe en el diccionario.

        Args:
            key: Clave a verificar.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return key in self._data

    def size(self):
        """
        Retorna el número de elementos.

        Returns:
            int: Cantidad de pares clave-valor.
        """
        return len(self._data)

    def keys(self):
        """
        Retorna todas las claves.

        Returns:
            list: Lista de claves.
        """
        return list(self._data.keys())

    def values(self):
        """
        Retorna todos los valores.

        Returns:
            list: Lista de valores.
        """
        return list(self._data.values())

    def items(self):
        """
        Retorna todos los pares clave-valor.

        Returns:
            list: Lista de tuplas (clave, valor).
        """
        return list(self._data.items())

    def clear(self):
        """
        Elimina todos los elementos del diccionario.
        """
        self._data.clear()

    def __repr__(self):
        """
        Representación en texto del diccionario.

        Returns:
            str: Cadena representando el diccionario.
        """
        return f"Dictionary({self._data})"


def main():
    """
    Función principal para demostrar el uso de Dictionary.
    """
    d = Dictionary()

    # Casos de prueba
    print("caso de prueba D1")
    d.set("nombre", "Fernando")
    d.set("edad", 22)
    d.set("carrera", "ITC")
    print(d)  

    print("caso de prueba D2")
    print(d.get("nombre"))   # Fernando
    print(d.get("altura", "No definida"))  # No definida


    print("caso de prueba D3")
    d.set("nombre", "Fernando 2")
    print(d)  


    print("caso de prueba D4")
    print(d.contains("edad"))  # True


    print("caso de prueba D5")
    print(d.get("nombre2"))   # Fernando

    #casos de prueba con error
    # print("caso de prueba D6")
    # d.remove("nombre2")


    #casos de prueba con error
    print("caso de prueba D7")
    print(d.keys())


    #casos de prueba con error
    print("caso de prueba D8")
    d.clear()
    print(d)

if __name__ == "__main__":
    main()