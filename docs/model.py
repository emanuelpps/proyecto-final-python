import sqlite3
import re
from tkinter import messagebox

# CONEXIÓN A LA DB


class OrderManager:
    def __init__(self):
        self.connection = self.create_db()
        self.orders_table()

    def create_db(self):
        return sqlite3.connect("orders.db")

    def orders_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                telefono TEXT,
                direccion TEXT,
                total TEXT,
                pedido TEXT,
                fecha TEXT
            )
        """)
        self.connection.commit()

    def add_order(self, tree, var_nombre_cliente,
                  var_telefono_cliente,
                  var_direccion_cliente,
                  var_monto_cliente,
                  var_pedido_cliente,
                  var_fecha_cliente):
        try:
            data = (
                var_nombre_cliente,
                var_telefono_cliente,
                var_direccion_cliente,
                var_monto_cliente,
                var_pedido_cliente,
                var_fecha_cliente
            )

            if not self.validate_name(data[0]):
                raise ValueError("El nombre solo debe contener letras.")

            if not self.validate_phone(data[1]):
                raise ValueError("El teléfono debe contener hasta 10 dígitos.")

            if not self.validate_address(data[2]):
                raise ValueError("La dirección no es válida.")

            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO orders (nombre, telefono, direccion, total, pedido, fecha) VALUES (?, ?, ?, ?, ?, ?)",
                data
            )
            self.connection.commit()
            last_id = cursor.lastrowid
            tree.insert("", "end", values=(last_id, *data))

        except ValueError as ve:
            messagebox.showerror("Error de validación", str(ve))

        except sqlite3.DatabaseError as db_err:
            messagebox.showerror("Error de base de datos",
                                 f"Ocurrió un error al insertar en la base de datos: {db_err}")
            self.connection.rollback()

        except Exception as e:
            messagebox.showerror("Error inesperado",
                                 f"Ocurrió un error inesperado: {e}")

    def delete_order(self, tree, selected_items):
        try:
            if not selected_items:
                messagebox.showwarning(
                    "Atención", "No hay ninguna orden seleccionada para eliminar.")
                return

            for selected_item in selected_items:
                item = tree.item(selected_item)
                order_id_to_delete = item['values'][0]

                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM orders WHERE id = ?",
                               (order_id_to_delete,))
                self.connection.commit()
                tree.delete(selected_item)

            messagebox.showwarning(
                "Atención", "La orden fue eliminada con éxito.")

        except sqlite3.Error:
            messagebox.showerror(
                "Error", "Ocurrió un problema con la base de datos.")
            self.connection.rollback()

        except Exception:
            messagebox.showerror("Error", "Ocurrió un error.")

    def update_order(self, tree, selected_items,
                     var_nombre_cliente,
                     var_telefono_cliente,
                     var_direccion_cliente,
                     var_monto_cliente,
                     var_pedido_cliente,
                     var_fecha_cliente):
        try:
            if not selected_items:
                messagebox.showwarning(
                    "Atención", "No hay ninguna orden seleccionada para actualizar.")
                return

            for selected_item in selected_items:
                item = tree.item(selected_item)
                order_id = item['values'][0]

                new_data = (
                    var_nombre_cliente,
                    var_telefono_cliente,
                    var_direccion_cliente,
                    var_monto_cliente,
                    var_pedido_cliente,
                    var_fecha_cliente
                )

                cursor = self.connection.cursor()
                cursor.execute("""
                    UPDATE orders
                    SET nombre = ?, telefono = ?, direccion = ?, total = ?, pedido = ?, fecha = ?
                    WHERE id = ?
                """, (*new_data, order_id))
                self.connection.commit()

                tree.item(selected_item, values=(order_id, *new_data))

            messagebox.showinfo(
                "Actualizado", "La orden fue actualizada correctamente.")

        except sqlite3.Error:
            messagebox.showerror(
                "Error", "Ocurrió un problema con la base de datos.")
            self.connection.rollback()

        except Exception:
            messagebox.showerror("Error", "Ocurrió un error inesperado.")

    def validate_name(self, nombre):
        return re.fullmatch(r'[\s a-zA-Z]+', nombre)

    def validate_phone(self, telefono):
        return re.fullmatch(r'\d{0,10}', telefono)

    def validate_address(self, direccion):
        return len(direccion.strip()) > 0
