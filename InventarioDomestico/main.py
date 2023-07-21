from tkinter import*
from tkinter import Tk, StringVar, ttk

#Importando Biblioteca Pillow
from PIL import Image, ImageTk

#Importando Biblioteca TKCalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#Cores
    # https://celke.com.br/artigo/tabela-de-cores-html-nome-hexadecimal-rgb

co0 = "#000000" #Black
co1 = "#feffff" #Branca
co2 = "#4fa882" #Green
co3 = "#000000" #Preta
co4 = "#403d3d" #Preta
co5 = "#000000" #Preta
co6 = "#000000" #Preta
co7 = "#000000" #Preta
co8 = "#000000" #Preta
co9 = "#F8F8FF" #GhostWhite
co10 = "#696969" #DimGray
 

#Criando Janela

window = Tk()
window.title('')
window.geometry('900x600')
window.configure(background=co10)
window.resizable(width=False, height=False)

style = ttk.Style(window)
style.theme_use("clam")


#Criando Frames
frameCima = Frame(window, width=899, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(window, width=899, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(window, width=899, height=300, bg=co1, pady=20, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#Abrindo Imagem
app_img = Image.open('icons/icon_customer.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Inventario Domestico", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


#Criando Labels

l_name = Label(frameMeio, text='Name Customer', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_name.place(x=10,y=10)

e_name = Entry(frameMeio, width=50, justify='left', relief=SOLID)
e_name.place(x=130,y=11)

# ====================================================================================================================================

l_salesman = Label(frameMeio, text='Sales', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_salesman.place(x=10,y=40)

e_salesman = Entry(frameMeio, width=50, justify='left', relief=SOLID)
e_salesman.place(x=130,y=41)

# ====================================================================================================================================

l_phonenumber = Label(frameMeio, text='Phone Number', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_phonenumber.place(x=10,y=70)

e_phonenumber = Entry(frameMeio, width=50, justify='left', relief=SOLID)
e_phonenumber.place(x=130,y=71)


# ====================================================================================================================================

l_description = Label(frameMeio, text='Description', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_description.place(x=10,y=100)

e_description = Entry(frameMeio, width=50, justify='left', relief=SOLID)
e_description.place(x=130,y=101)

# ====================================================================================================================================

l_startcontract = Label(frameMeio, text='Start Contract', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_startcontract.place(x=10,y=130)

e_startcontract = DateEntry(frameMeio, width=12, Background='darkblue', bordewidth=2, year=2023)
e_startcontract.place(x=130,y=131)


# ============= Botao Inserir =============

img_add = Image.open('icons/icons8-add-48.png')
img_add = img_add.resize((17,17))
img_add = ImageTk.PhotoImage(img_add)

b_insert = Button(frameMeio, image=img_add, width=95, text=' Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8',  bg=co1, fg=co0)
b_insert.place(x=450, y=8)


# ============= Botao Refresh =============

img_ref = Image.open('icons/icons8-refresh-48.png')
img_ref = img_ref.resize((17,17))
img_ref = ImageTk.PhotoImage(img_ref)

b_insert = Button(frameMeio, image=img_ref, width=95, text=' Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8',  bg=co1, fg=co0)
b_insert.place(x=450, y=38)


# ============= Botao Delete =============

img_del = Image.open('icons/icons8-delete-100.png')
img_del = img_del.resize((17,17))
img_del = ImageTk.PhotoImage(img_del)

b_insert = Button(frameMeio, image=img_del, width=95, text=' Excluir'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8',  bg=co1, fg=co0)
b_insert.place(x=450, y=70)

window.mainloop()
