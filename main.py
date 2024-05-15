# importing the tkinter module and PIL
# that is pillow module
import time
import tkinter
from tkinter import ttk, Tk, Label, LEFT, RIGHT

from PIL import ImageTk, Image

from pet import Pet

# Calling the Tk (The initial constructor of tkinter)
root = Tk()

# We will make the title of our app as Image Viewer
root.title("AniTamagotchi")
logo = ImageTk.PhotoImage(Image.open("assets/logo.png"))
root.wm_iconphoto(False, logo)

# The geometry of the box which will be displayed
# on the screen
root.geometry("350x500")

# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images

hungry = ImageTk.PhotoImage(Image.open("assets/hungry_tyan.gif").resize((350, 350)))
happy = ImageTk.PhotoImage(Image.open("assets/happy_satoru.gif").resize((350, 350)))
nods = ImageTk.PhotoImage(Image.open("assets/bear_tyan.gif").resize((350, 350)))
wantin_pee = ImageTk.PhotoImage(Image.open("assets/cute_tyan.png").resize((350, 350)))
game_over = ImageTk.PhotoImage(Image.open("assets/game_over.jpg"))

image_lbl = Label(image=hungry)
image_lbl.grid(row=0, column=1, columnspan=3)

state = Label(text='Fine', padx=10, pady=5, font=100, fg='white', bg='green')
state.grid(row=1, column=1, columnspan=3)

pet = Pet()

Label(root, text='Food: ', justify=RIGHT).grid(row=2, column=1)

food = tkinter.IntVar()
food_prog = ttk.Progressbar(root, variable=food)
food_prog.grid(row=2, column=2)


def feed():
    pet.feed()
    food.set(pet.get_food())


food_btn = ttk.Button(root, text="Feed", command=feed)
food_btn.grid(row=2, column=3)

Label(root, text='Water: ', justify=RIGHT).grid(row=3, column=1)
water = tkinter.IntVar()
water_prog = ttk.Progressbar(root, variable=water)
water_prog.grid(row=3, column=2)


def water_fn():
    pet.water()
    water.set(pet.get_water())


water_btn = ttk.Button(root, text="Water", command=water_fn)
water_btn.grid(row=3, column=3)

Label(root, text='Pee: ', justify=RIGHT).grid(row=4, column=1)
pee = tkinter.IntVar()
pee_prog = ttk.Progressbar(root, variable=pee)
pee_prog.grid(row=4, column=2)


def pee_fn():
    pet.pee()
    pee.set(pet.get_pee())


pee_btn = ttk.Button(root, text="Pee", command=pee_fn)
pee_btn.grid(row=4, column=3)

Label(text='Poo: ', justify=RIGHT).grid(row=5, column=1)

poo = tkinter.IntVar()
poo_prog = ttk.Progressbar(root, variable=poo)
poo_prog.grid(row=5, column=2)


def poo_fn():
    pet.poo()
    poo.set(pet.get_poo())


poo_btn = ttk.Button(root, text="Poo", command=poo_fn)
poo_btn.grid(row=5, column=3)

food.set(pet.get_food())
water.set(pet.get_water())
pee.set(pet.get_pee())
poo.set(pet.get_poo())


def logic():
    if pet.get_health():
        pet.spend()

        food.set(pet.get_food())
        water.set(pet.get_water())
        pee.set(pet.get_pee())
        poo.set(pet.get_poo())

        if pet.get_health() > 80:
            image_lbl.config(image=happy)
            state.config(fg='white', bg='green', text='Fine')
        elif 55 < pet.get_health() < 80:
            image_lbl.config(image=nods)
            state.config(fg='white', bg='blue', text='Normal')
        elif 25 < pet.get_health() < 55:
            image_lbl.config(image=wantin_pee)
            state.config(fg='white', bg='orange', text='Not fine')
        elif pet.get_health() < 25:
            image_lbl.config(image=hungry)
            state.config(fg='white', bg='black', text='Very bad...')
        root.after(1000, logic)
    else:
        image_lbl.config(image=game_over)
        state.config(fg='white', bg='black', text='ALT + F4 pls...' )
        food_btn.config(state='disabled')
        water_btn.config(state='disabled')
        pee_btn.config(state='disabled')
        poo_btn.config(state='disabled')
        root.title('GAME OVER')
        root.wm_iconphoto(False, game_over)


root.after(0, logic)
root.mainloop()
