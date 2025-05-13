from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class MainView:
    def __init__(self, root, controller=None):
        self.controller = controller
        self.root = root
        self.root.title("Gestor de Pedidos de Delivery")

        # COLORES
        bg_color = "#f7f9fb"
        title_bg_color = "#4a90e2"
        button_bg_color = "#4caf50"
        button_del_bg_color = "#f44336"
        button_fg_color = "#ffffff"
        entry_bg_color = "#ffffff"
        tree_bg_color = "#eaf2f8"
        tree_heading_bg_color = "#2a76bf"
        tree_heading_fg_color = "#ffffff"

        self.root.configure(bg=bg_color)

        # VARIABLES DEL FORMULARIO
        self.var_nombre_cliente = StringVar()
        self.var_telefono_cliente = StringVar()
        self.var_direccion_cliente = StringVar()
        self.var_monto_cliente = StringVar()
        self.var_pedido_cliente = StringVar()
        self.var_fecha_cliente = StringVar()

        # TÍTULO
        Label(
            self.root,
            text="Gestor de Pedidos de Delivery",
            bg=title_bg_color,
            fg="white",
            font=("Helvetica", 16, "bold"),
            pady=10
        ).grid(row=0, column=0, columnspan=2, sticky="nsew")

        # FORMULARIO
        def open_calendar():
            def select_date():
                selected_date = cal.selection_get().strftime("%d-%m-%Y")
                self.var_fecha_cliente.set(selected_date)
                calendar_window.destroy()

            calendar_window = Toplevel(root)
            calendar_window.title("Seleccionar Fecha")
            calendar_window.configure(bg=bg_color)

            cal = Calendar(calendar_window, date_pattern="dd-mm-yyyy", background=button_bg_color,
                           foreground=button_fg_color, selectmode="day")
            cal.pack(pady=10)

            btn_select_date = Button(calendar_window, text="Seleccionar", bg=button_bg_color,
                                     fg=button_fg_color, command=select_date)
            btn_select_date.pack(pady=10)

        Label(self.root, text="Nombre de Cliente: ", bg=bg_color).grid(row=1, column=0, sticky=W)
        Entry(self.root, textvariable=self.var_nombre_cliente, bg=entry_bg_color).grid(row=2, column=0, sticky="nsew")

        Label(self.root, text="Teléfono: ", bg=bg_color).grid(row=1, column=1, sticky=W)
        Entry(self.root, textvariable=self.var_telefono_cliente, bg=entry_bg_color).grid(row=2, column=1, sticky="nsew")

        Label(self.root, text="Dirección: ", bg=bg_color).grid(row=3, column=0, sticky=W)
        Entry(self.root, textvariable=self.var_direccion_cliente, bg=entry_bg_color).grid(row=4, column=0, sticky="nsew")

        Label(self.root, text="Monto total: ", bg=bg_color).grid(row=3, column=1, sticky=W)
        Entry(self.root, textvariable=self.var_monto_cliente, bg=entry_bg_color).grid(row=4, column=1, sticky="nsew")

        Label(self.root, text="Pedido: ", bg=bg_color).grid(row=5, column=0, sticky=W)
        Entry(self.root, textvariable=self.var_pedido_cliente, bg=entry_bg_color).grid(row=6, column=0, sticky="nsew")

        Label(self.root, text="Fecha (dd-mm-aaaa): ", bg=bg_color).grid(row=5, column=1, sticky=W)

        frame_fecha = Frame(self.root, bg=bg_color)
        frame_fecha.grid(row=6, column=1, sticky="nsew")

        Entry(frame_fecha, textvariable=self.var_fecha_cliente, bg=entry_bg_color, state="readonly").pack(side=LEFT, fill=X, expand=True)
        Button(frame_fecha, text="📅", bg=button_bg_color, fg=button_fg_color, command=open_calendar).pack(side=RIGHT)

        # TREEVIEW
        self.tree = ttk.Treeview(self.root, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), show="headings")
        for i, heading in enumerate(["ID", "Nombre", "Teléfono", "Dirección", "Monto", "Pedido", "Fecha"], 1):
            self.tree.heading(f"#{i}", text=heading)
        self.tree.grid(row=9, column=0, columnspan=2)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background=tree_bg_color, fieldbackground=tree_bg_color)
        style.map("Treeview", background=[("selected", title_bg_color)])
        style.configure("Treeview.Heading", background=tree_heading_bg_color, foreground=tree_heading_fg_color)

        # BOTONES
        Button(self.root, text="Eliminar", bg=button_del_bg_color, fg=button_fg_color,
               command=self.eliminar).grid(row=7, column=0, sticky=E)
        Button(self.root, text="Actualizar", bg=button_bg_color, fg=button_fg_color,
               command=self.actualizar).grid(row=7, column=1, sticky=W)
        Button(self.root, text="Guardar", bg=button_bg_color, fg=button_fg_color,
               command=self.guardar).grid(row=7, column=1, sticky=E)

        if self.controller:
            self.controller.cargar_ordenes(self.tree)

    def get_form_data(self):
        return (
            self.var_nombre_cliente.get(),
            self.var_telefono_cliente.get(),
            self.var_direccion_cliente.get(),
            self.var_monto_cliente.get(),
            self.var_pedido_cliente.get(),
            self.var_fecha_cliente.get()
        )

    def guardar(self):
        if self.controller:
            self.controller.agregar_orden(self.tree, self.get_form_data())

    def eliminar(self):
        if self.controller:
            self.controller.eliminar_orden(self.tree, self.tree.selection())

    def actualizar(self):
        if self.controller:
            self.controller.actualizar_orden(self.tree, self.tree.selection(), self.get_form_data())
