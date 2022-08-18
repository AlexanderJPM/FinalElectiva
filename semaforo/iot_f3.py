import tkinter as tk

ve = 1


appmain = tk.Tk()
appmain.geometry("1005x605")
appmain.resizable(False, False)
appmain.title("IoT_Semaforo")
appmain.iconbitmap("img/semaforo.ico")
appmain.config(
    bg="gray99",
    relief="groove",
    cursor="gumby"
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

    if ve == 1:

        verdeFrame.pack(side="right", anchor=tk.N)
        amarilloFrame.forget()
        rojoFrame.forget()
        offFrame.forget()
        ve = va

    elif ve == 2:

        amarilloFrame.pack(side="right", anchor=tk.N)
        verdeFrame.forget()
        rojoFrame.forget()
        offFrame.forget()
        ve = vi

    elif ve == 3:

        rojoFrame.pack(side="right", anchor=tk.N)
        amarilloFrame.forget()
        verdeFrame.forget()
        offFrame.forget()
        ve = vo


btn_cambio_appmain = tk.Button(
    appmain,
    text="¡click mi!",
    font="Arial",
    fg="dark violet",
    bg="snow",
    command=cambio
).place(x=92, y=250)


appmain.mainloop()
