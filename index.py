def crear_lista(*elementos):
    """
    Crea una lista a partir de los argumentos proporcionados.
    
    Args:
        *elementos: Elementos que conformarán la lista.
        
    Returns:
        list: Una lista con los elementos dados.
    """
    return list(elementos)

if __name__ == "__main__":
    # Ejemplo de uso
    numeros = crear_lista(1, 2, 3, 4, 5)
    print("Lista de números:", numeros)
    
    mixta = crear_lista("Python", 3.14, True, [1, 2])
    print("Lista mixta:", mixta)
