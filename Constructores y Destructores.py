# Programa para demostrar el uso de constructores y destructores en Python
# Desarrollado por [Tu Nombre]

class Libro:
    def _init_(self, titulo, autor):
        """
        Constructor de la clase Libro. Inicializa los atributos titulo y autor.

        Args:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        """
        self.titulo = titulo
        self.autor = autor
        print(f"Libro '{self.titulo}' de {self.autor} ha sido creado.")

    def _del_(self):
        """
        Destructor de la clase Libro. Realiza una limpieza básica al eliminar un objeto de la clase.
        """
        print(f"Libro '{self.titulo}' de {self.autor} ha sido eliminado.")

def main():
    """
    Función principal del programa. Crea y elimina objetos de la clase Libro para demostrar
    el uso de constructores y destructores.
    """
    libro1 = Libro("1984", "George Orwell")
    # Realizando alguna operación con el objeto libro1
    print(f"Estamos leyendo el libro '{libro1.titulo}' de {libro1.autor}.")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
    # Realizando alguna operación con el objeto libro2
    print(f"Estamos leyendo el libro '{libro2.titulo}' de {libro2.autor}.")

    del libro1

if __name__ == "_main_":
    main()