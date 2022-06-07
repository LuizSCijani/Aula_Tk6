from tkinter import *

#criar a janela/window
janela = Tk()
janela.geometry('400x167+90+90')
janela.config(background='#E0FFFF')

#criar a função


#criar os widgets
frame1 = Frame(janela, background='#B0E0E6', pady=10, padx=20)
frame2 = Frame(janela, background='#B0E0E6', pady=10, padx=20)
frame3 = Frame(janela, background='#B0E0E6', pady=13, padx=8)

label1 = Label(frame1, text='Dados Pessoais', font='Arial 19', background='#B0E0E6')
label2 = Label(frame1, text='Nome:', font='Arial 15', background='#ADD8E6', anchor=E)
label3 = Label(frame1, text='Data Nasc:', font='Arial 15', background='#ADD8E6', anchor=E)
label4 = Label(frame1, text='CPF:', font='Arial 15', background='#ADD8E6', anchor=E)
label5 = Label(frame1, text='Telefone:', font='Arial 15', background='#ADD8E6', anchor=E)

label6 = Label(frame2, text='Endereço', font='Arial 19', background='#B0E0E6')
label7 = Label(frame2, text='Rua:', font='Arial 15', background='#ADD8E6', anchor=E)
label8 = Label(frame2, text='Bairro:', font='Arial 15', background='#ADD8E6', anchor=E)
label9 = Label(frame2, text='Cidade:', font='Arial 15', background='#ADD8E6', width=7, anchor=E)
label10 = Label(frame2, text='Nº:', font='Arial 15', background='#ADD8E6', width=4, anchor=E)
label11 = Label(frame2, text='UF:', font='Arial 15', background='#ADD8E6', width=4, anchor=E)

entry1 = Entry(frame1, font='Arial 10')
entry2 = Entry(frame1, font='Arial 10')
entry3 = Entry(frame1, font='Arial 10')
entry4 = Entry(frame1, font='Arial 10')

entry5 = Entry(frame2, font='Arial 10')
entry6 = Entry(frame2, font='Arial 10')
entry7 = Entry(frame2, font='Arial 10')
entry8 = Entry(frame2, font='Arial 10')
entry9 = Entry(frame2, font='Arial 10')

btn1 = Button(frame3, text='Gravar Dados', font='Arial 15', background='#B0C4DE')
btn2 = Button(frame3, text='Listar Dados', font='Arial 15', background='#B0C4DE')

#organizar os widgets/layout
frame1.grid(sticky=NSEW)
frame2.grid(sticky=NSEW)
frame3.grid(sticky=NSEW)

#frame1
label1.grid(row=0, column=0, sticky=NSEW)

label2.grid(row=1, column=0, sticky=NSEW)
entry1.grid(row=1, column=1)

label3.grid(row=2, column=0, sticky=NSEW)
entry2.grid(row=2, column=1)

label4.grid(row=3, column=0, sticky=NSEW)
entry3.grid(row=3, column=1)

label5.grid(row=4, column=0, sticky=NSEW)
entry4.grid(row=4, column=1)

#frame2
label6.grid(row=0, column=0, sticky=NSEW)

label7.grid(row=1, column=0, sticky=NSEW)
entry5.grid(row=1, column=1, columnspan=4, sticky=EW)

label8.grid(row=2, column=0, sticky=NSEW)
entry6.grid(row=2, column=1)

label9.grid(row=2, column=3, sticky=EW)
entry7.grid(row=2, column=4)

label10.grid(row=1, column=5, sticky=NSEW)
entry8.grid(row=1, column=6)

label11.grid(row=2, column=5, sticky=NSEW)
entry9.grid(row=2, column=6)

#frame3
btn1.grid(row=0, column=0, sticky=NSEW)
btn2.grid(row=0, column=1, sticky=NSEW)

#executar a janela
janela.mainloop()