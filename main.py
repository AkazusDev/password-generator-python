import tkinter as tk
from tkinter import messagebox
import pyperclip
from generate_password import password_generator

root = tk.Tk()
root.title("Password Generator")

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight() - 40


width_window = 390  # root.winfo_reqheight()
height_window = 180  # root.winfo_reqwidth()

pwidth = round(width_screen/2-width_window/2)
pheight = round(height_screen/2-height_window/2)
root.geometry(str(width_window)+"x"+str(height_window)+"+"+str(pwidth)+"+"+str(pheight))


# METHODS
def generate():
    pwd = size_num.get()
    try:
        pwd = int(pwd)
        if type(pwd) == int:
            if pwd != 0:
                pwd_created.set(password_generator(pwd))
            else:
                messagebox.showerror("Sin longitud", "Digite la longitud de la contraseña")
        else:
            messagebox.showerror("Inserte un número", "Solo debe digitar un número entero")
    except ValueError:
        messagebox.showerror("Inserte un número", "Solo debe digitar un número entero")


def copy_paperclip():
    pwd = pwd_created.get()
    if pwd != "":
        pyperclip.copy(pwd)
        messagebox.showinfo("Contraseña copiada", "Copiada en el portapapeles")
    else:
        messagebox.showerror("Contraseña vacia", "No hay contraseña para copiar")


# FRAMES
tittle_frm = tk.Label(root, text="Password Generator", font=("Arial", 12), pady=5)
tittle_frm.grid(row=0, column=0, columnspan=2)

container = tk.Frame(root, padx=10, pady=10)  # , bg="#D9D9D9"
container.grid(row=1, column=0, columnspan=2)

watermark = tk.Label(root, text="Developed by MFES")
watermark.grid(row=2, column=0)

version_lbl = tk.Label(root, text="Version v1.0.0")
version_lbl.grid(row=2, column=1)

# IntVar
# size_num = tk.IntVar()

# StringVar
size_num = tk.StringVar()
size_num.set("0")

pwd_created = tk.StringVar()
pwd_created.set("")

# Frame Widgets

pwd_size_lbl = tk.Label(container, text="Tamaño de la contraseña:")
pwd_size_lbl.grid(row=0, column=0)

pwd_size_ent = tk.Entry(container, width=5, textvariable=size_num)
pwd_size_ent.grid(row=0, column=1)

generate_btn = tk.Button(container, text="Generar", command=lambda: generate(), bg="#515AA8", foreground="#FFF", relief='groove')
generate_btn.grid(row=0, column=2)

pwd_show = tk.Entry(container, width=50, textvariable=pwd_created, state="readonly", font=("Arial", 10))
pwd_show.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

pwd_copy = tk.Button(container, text="Copiar", command=lambda: copy_paperclip(), bg="#559F53", foreground="#FFF", relief='groove')
pwd_copy.grid(row=2, column=0, columnspan=3)

root.mainloop()

