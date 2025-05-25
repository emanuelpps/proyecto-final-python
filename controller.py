from model import OrderManager
from view import MainView
from tkinter import Tk


class AppController:
    def __init__(self, root):
        self.model = OrderManager()
        self.view = MainView(root, controller=self)

    def agregar_orden(self, tree, data):
        self.model.add_order(tree, *data)

    def eliminar_orden(self, tree, seleccionados):
        self.model.delete_order(tree, seleccionados)

    def actualizar_orden(self, tree, seleccionados, data):
        self.model.update_order(tree, seleccionados, *data)

    def cargar_ordenes(self, tree):
        cursor = self.model.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)


def main():
    root = Tk()
    AppController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
