class Stack:
    """
    Implementación de una pila (Stack) usando una lista de Python.

    Sigue el principio LIFO (Last In, First Out):
    el último elemento en entrar es el primero en salir.
    """

    def __init__(self):
        """
        Inicializa una pila vacía.
        """
        self._items = []

    def push(self, item):
        """
        Agrega un elemento al tope de la pila.

        Args:
            item: Elemento a insertar en la pila.
        """
        self._items.append(item)

    def pop(self):
        """
        Elimina y retorna el elemento del tope de la pila.

        Returns:
            El elemento en el tope de la pila.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Retorna el elemento del tope sin eliminarlo.

        Returns:
            El elemento en el tope de la pila.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Verifica si la pila está vacía.

        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return len(self._items) == 0

    def size(self):
        """
        Retorna el número de elementos en la pila.

        Returns:
            int: Cantidad de elementos en la pila.
        """
        return len(self._items)

    def __repr__(self):
        """
        Representación en texto de la pila.

        Returns:
            str: Cadena representando la pila.
        """
        return f"Stack({self._items})"


def main():
    """
    Función principal que demuestra el uso de la clase Stack.
    """
    s = Stack()

    # Casos de prueba
    print("caso de prueba S1")
    s.push(10)
    print(f'size: {s.size()}')

    # Casos de prueba
    print("caso de prueba S2, agregando 10, 2, 3")
    s.push(10)
    s.push(2)
    s.push(3)
    print(f'size: {s.size()}')

    # Casos de prueba
    print("caso de prueba S3")
    print(s.pop())


    # Casos de prueba
    print("caso de prueba S4")
    print(s.peek())

    # Casos de prueba con error.
    s2 = Stack()
    # print("caso de prueba S5")
    # print(s2.pop())

    # Casos de prueba
    # print("caso de prueba S56")
    # print(s2.peek())
    
    # Casos de prueba
    print("caso de prueba S7")
    print(s2.is_empty())

    # Casos de prueba
    print("caso de prueba S8")
    print(s2.size())


if __name__ == "__main__":
    main()