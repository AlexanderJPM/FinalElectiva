
import tkinter as tk
from tkinter import CENTER, PhotoImage, ttk
from turtle import width
from index import mongo
from faker import Faker
from PIL import Image, ImageTk

mongoDb = mongo()

ve = 1


appmain = tk.Tk()
appmain.geometry("1005x605")
appmain.resizable(False, False)
appmain.title("IoT_Semaforo")
appmain.iconbitmap("img/semaforo.ico")
appmain.config(
    bg="gray99",
    relief="groove"

)

offFrame = tk.Frame()
offFrame.pack(side="right", anchor="n")
offFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
rojoFrame = tk.Frame()
rojoFrame.pack(side="right", anchor=tk.N)
rojoFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
verdeFrame = tk.Frame()
verdeFrame.pack(side="right", anchor=tk.N)
verdeFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
amarilloFrame = tk.Frame()
amarilloFrame.pack(side="right", anchor=tk.N)
amarilloFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
amarilloFrame.forget()
rojoFrame.forget()
verdeFrame.forget()
# offFrame.forget()


img_off = tk.PhotoImage(file="img/off.gif")
img_amarillo = tk.PhotoImage(file="img/amarillo.gif")
img_verde = tk.PhotoImage(file="img/verde.gif")
img_rojo = tk.PhotoImage(file="img/rojo.gif")
img_cell = tk.PhotoImage(file="img/cell.png")

img_semaforo_label_amarilloframe = tk.Label(
    amarilloFrame,
    image=img_amarillo,
    width="100",
    height="150"
).place(x=10, y=10)

img_semaforo_label_rojoframe = tk.Label(
    rojoFrame,
    image=img_rojo,
    width="100",
    height="150"
).place(x=10, y=10)

img_semaforo_label_verdeframe = tk.Label(
    verdeFrame,
    image=img_verde,
    width="100",
    height="150"
).place(x=10, y=10)

img_semaforo_label_offframe = tk.Label(
    offFrame,
    image=img_off,
    width="100",
    height="150"
).place(x=10, y=10)

img_cell_label_appmain = tk.Label(
    appmain,
    image=img_cell,
    width="235",
    height="400"
).place(x=10, y=10)

img_txt_label_offframe = tk.Label(
    offFrame,
    text="*.....*",
    fg="black",
    bg="gray99",
    font=("Arial", 20)
).place(x=130, y=80)

img_txt_label_verdeframe = tk.Label(
    verdeFrame,
    text=" ¡GOO! ",
    fg="springGreen2",
    bg="gray99",
    font=("Arial", 20)
).place(x=100, y=80)

img_txt_label_rojoframe = tk.Label(
    rojoFrame,
    text=" ¡STOP! ",
    fg="red2",
    bg="gray99",
    font=("Arial", 20)
).place(x=100, y=80)

img_txt_label_amarilloframe = tk.Label(
    amarilloFrame,
    text=" ¡slow! ",
    fg="gold",
    bg="gray99",
    font=("Arial", 20)
).place(x=100, y=80)


def cambio():
    global ve
    va = 2
    vi = 3
    vo = 1
    ex = Faker()
    if ve == 1:

        verdeFrame.pack(side="right", anchor=tk.N)
        amarilloFrame.forget()
        rojoFrame.forget()
        offFrame.forget()
        ve = va
        mongoDb.insertCollection("Amarrillo", ex.ipv4())

    elif ve == 2:

        amarilloFrame.pack(side="right", anchor=tk.N)
        verdeFrame.forget()
        rojoFrame.forget()
        offFrame.forget()
        ve = vi
        mongoDb.insertCollection("Verde", ex.ipv4())

    elif ve == 3:

        rojoFrame.pack(side="right", anchor=tk.N)
        amarilloFrame.forget()
        verdeFrame.forget()
        offFrame.forget()
        ve = vo
        mongoDb.insertCollection("Rojo", ex.ipv4())
    table()


img = Image.open('./img/pushBotton.jpeg')
img = img.resize((110, 90))
img = ImageTk.PhotoImage(img)
btn_cambio_appmain = tk.Button(
    appmain,
    image=img,
    font=("Arial 12 bold"),
    fg="dark violet",
    bg="snow",
    cursor="hand2",
    command=cambio
).place(x=75, y=170)

# Codigo Alexander


def table():
    tabla = ttk.Treeview(appmain)
    tabla['columns'] = ('Metros', 'Color', 'Ip')
    tabla.column('Metros', width=100, anchor=CENTER
                 )
    tabla.column('Color', width=100, anchor=CENTER)
    tabla.column('Ip', width=100, anchor=CENTER)
    tabla.heading('Metros', text='Metros', anchor=CENTER)
    tabla.heading('Color', text='Color', anchor=CENTER)
    tabla.heading('Ip', text='Ip', anchor=CENTER)

    x = 0
    ex = Faker()

    for i in range(mongoDb.countCollection()):
        ip = ex.ipv4()
        datos = mongoDb.getCollection(i)
        tabla.insert(parent="", index=i, id=i, text="",
                     values=(datos[0], datos[1], datos[2]))
    tabla.place(x=300, y=100)


table()
appmain.mainloop()
