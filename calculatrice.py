from tkinter import * 
from math import *
#importation de la bibliotheque Tkinter et math
fenetre = Tk()
fenetre.geometry("400x500") #definis la taille de la fenetre
fenetre.title ('Calculatrice') #Nom de la fenetre
 
entree = Entry(fenetre)
entree.grid(row=0 , column=0)
entree.bind("<Return>", egale)#fait en sorte qu'un evenement se produit lorsque l'on appuye sur enter
chaine = Label(fenetre)#Modifie l'attribut "texte" lors de l'evenement
 
entree.grid(row=0, column=1)
chaine.grid()
def ajouter():
    nb1 = entree.get()
    global nb2,math
    math = "addition"
    nb2 = int(nb1)
    entree.delete(0,END)
def soustraction():
    nb1 = entree.get()
    global nb2,math
    math = "soustraction"
    nb2 = int(nb1)
    entree.delete(0,END)
def multiplication():
    nb1 = entree.get()
    global nb2,math
    math = "multiplication"
    nb2 = int(nb1)
    entree.delete(0,END)
def division():
    nb1 = entree.get()
    global nb2,math
    math = "division"
    nb2 = int(nb1)
    entree.delete(0,END)
def reset():
    entree.delete(0 , END)
    chaine.configure(text = " ")
def egale():
    nb3 = entree.get()
    entree.delete(0 , END)
    if math == "addition" :
        entree.insert(0, nb2 + int(nb3))
        chaine.configure(text = "resultat=" + str(eval(entree.get())))
    elif math == "soustraction" :
        entree.insert(0, nb2 - int(nb3))
        chaine.configure(text = "resultat=" + str(eval(entree.get())))
    elif math == "multiplication" :
        entree.insert(0, nb2 * int(nb3))
        chaine.configure(text = "resultat=" + str(eval(entree.get())))
    elif math == "division" :
        entree.insert(0, nb2 / int(nb3))
        chaine.configure(text = "resultat=" + str(eval(entree.get())))
    entree.delete(0 , END)
#def egale():
    
	#chaine.configure(text = "resultat=" + str(eval(entree.get())))


boudiv = Button(fenetre, text='/', width =6 , command=division).grid(row =3, column =1)
bouegale = Button(fenetre, text='=', width =6 , command=egale).grid(row =4, column =1)
bouplus = Button(fenetre, text='+', width =6 , command=ajouter).grid(row =2, column =0)
boumoins = Button(fenetre, text='-', width =6 , command=soustraction).grid(row =2, column =1)
boufois = Button(fenetre, text='x', width =6 , command=multiplication).grid(row =3, column =0)
boureset = Button(fenetre, text=' reset', width =6 , command=reset).grid(row =4, column =0)



 
#Placement des boutons
fenetre.mainloop()