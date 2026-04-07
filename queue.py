from collections import deque

class Queue:
    """
    Implementación de una cola (Queue) usando deque.

    Sigue el principio FIFO (First In, First Out):
    el primer elemento en entrar es el primero en salir.
    """

    def __init__(self):
        """
        Inicializa una cola vacía.
        """
        self._items = deque()

    def enqueue(self, item):
        """
        Agrega un elemento al final de la cola.

        Args:
            item: Elemento a insertar en la cola.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Elimina y retorna el elemento al frente de la cola.

        Returns:
            El elemento al frente de la cola.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        """
        Retorna el elemento al frente sin eliminarlo.

        Returns:
            El elemento al frente de la cola.

        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """
        Verifica si la cola está vacía.

        Returns:
            bool: True si está vacía, False en caso contrario.
        """
        return len(self._items) == 0

    def size(self):
        """
        Retorna el número de elementos en la cola.

        Returns:
            int: Cantidad de elementos.
        """
        return len(self._items)

    def __repr__(self):
        """
        Representación en texto de la cola.

        Returns:
            str: Cadena representando la cola.
        """
        return f"Queue({list(self._items)})"


def main():
    """
    Función principal que demuestra el uso de la clase Queue.
    """
    q = Queue()

    # Casos de prueba
    print("caso de prueba Q1")
    q.enqueue(10)
    print(f'size: {q.size()}')

    # Casos de prueba
    print("caso de prueba Q2")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f'{q}')

    print("caso de prueba Q3")
    print(f'{q.dequeue()}')

    print("caso de prueba Q4")
    print(f'{q.peek()}')

    #Casos con error
    q2= Queue()

    # print("caso de prueba Q5")
    # print(f'{q2.dequeue()}')
    

    # print("caso de prueba Q6")
    # print(f'{q2.peek()}')
    
    print("caso de prueba Q7")
    print(f'{q2.is_empty()}')

    print("caso de prueba Q8")
    print(f'{q2.size()}')


if __name__ == "__main__":
    main()