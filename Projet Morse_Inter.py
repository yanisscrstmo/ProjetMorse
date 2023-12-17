"""
   This project has been made by Yanis Crisostomo, I'm a student in Python, I hope you will like it. In the repository,
   you will also find the .exe file to execute the script. Make sure you have the winsound, tkinter and time libraries installed on your
   computer for a full experience. Enjoy!
"""

import winsound
import time
import tkinter

root = tkinter.Tk()
root.title("Traducto'Morse v1")
root.geometry("800x800")

frequence = 1000
duree_point = 100
duree_tiret = 3 * duree_point

dict_morse = {'A': '=.===', 'B': '===.=.=.=', 'C': '===.=.===.=', 'D': '===.=.=', 'E': '=', 'F': '=.=.===.=',
              'G': '===.===.=', 'H': '=.=.=.=', 'I': '=.=', 'J': '=.===.===.===', 'K': '===.=.===', 'L': '=.===.=.=',
              'M': '===.===', 'N': '===.=', 'O': '===.===.===', 'P': '=.===.===.=', 'Q': '===.===.=.===', 'R': '=.===.=',
              'S': '=.=.=', 'T': '===', 'U': '=.=.===', 'V': '=.=.=.===', 'W': '=.===.===', 'X': '===.=.=.===',
              'Y': '===.=.===.===', 'Z': '===.===.=.=',}

dict_morse_taah = {'A': 'titaah', 'B': 'taahtititi','C': 'taahtitaahti','D': 'taahtiti',
                   'E': 'ti','F': 'tititaahti','G': 'taahtaahti','H': 'titititi',
                   'I': 'titi','J': 'titaahtaahtaah','K': 'taahtitaah','L': 'titaahtiti','M': 'taahtaah',
                   'N': 'taahti','O': 'taahtaahtaah','P': 'titaahtaahti','Q': 'taahtaahtitaah','R': 'titaahti',
                   'S': 'tititi','T': 'taah','U': 'tititaah','V': 'titititaah','W': 'titaahtaah','X': 'taahtititaah',
                   'Y': 'taahtitaahtaah','Z': 'taahtaahtiti'}

dict_morse_tirets = {'A': '.-','B': '-...','C': '-.-.','D': '-..',
                     'E': '.','F': '..-.','G': '--.','H': '....',
                     'I': '..','J': '.---','K': '-.-','L': '.-..',
                     'M': '--','N': '-.','O': '---','P': '.--.',
                     'Q': '--.-','R': '.-.','S': '...','T': '-',
                     'U': '..-','V': '...-','W': '.--','X': '-..-',
                     'Y': '-.--','Z': '--..',}

sortie_egal = []
sortie_taah = []
sortie_egal_2 = ""
sortie_francais = []
sortie_francais_2 = []
sortie_taah_2 = ""
sortie_tirets = []
sortie_tirets_2 = ""
def francais_morse():
    mot_entrée = saisie_francais.get()
    mot_entrée = mot_entrée.upper()
    if mot_entrée == "":
        resultat_francais_morse.delete("1.0", tkinter.END)
        return
    sortie_egal = []
    i = 0
    while i < len(mot_entrée):
        for k in dict_morse:
            if mot_entrée[i:i+len(k)] == k:
                sortie_egal.append(dict_morse[k])
                i += len(k)
                sortie_egal_2 = "...".join(sortie_egal)

    resultat_francais_morse.delete("1.0", tkinter.END)
    resultat_francais_morse.insert("1.0", sortie_egal_2)

def francais_morse_taah():
    mot_entrée = saisie_francais.get()
    mot_entrée = mot_entrée.upper()
    j=0
    while j < len(mot_entrée):
        for k in dict_morse_taah:
            if mot_entrée[j:j+len(k)] == k:
                sortie_taah.append(dict_morse_taah[k])
                j += len(k)
                sortie_taah_2 = " ".join(sortie_taah)
    resultat_morse_taah.delete("1.0", tkinter.END)
    resultat_morse_taah.insert("1.0", sortie_taah_2)

def francais_morse_tirets():
    mot_entrée = saisie_francais.get()
    mot_entrée = mot_entrée.upper()
    global sortie_tirets_2
    sortie_tirets_2 = []
    l = 0
    while l < len(mot_entrée):
        for k in dict_morse_tirets:
            if mot_entrée[l:l+len(k)] == k:
                sortie_tirets_2.append(dict_morse_tirets[k])
                l += len(k)
    sortie_tirets_3 = " ".join(sortie_tirets_2)
    resultat_morse_tirets.delete("1.0", tkinter.END)
    resultat_morse_tirets.insert("1.0", sortie_tirets_3)

def morse_francais():
    code_morse = saisie_morse.get()
    code_morse = code_morse.split('.......')
    sortie_francais = []
    for mot in code_morse:
        mot_morse = mot.split('...')
        mot_1 = []
        for element in mot_morse:
            for k, v in dict_morse.items():
                if element == v:
                    mot_1.append(k)
        sortie_francais.append(''.join(mot_1))
    sortie_francais_2 = ' '.join(sortie_francais)
    resultat_morse_francais.delete("1.0", tkinter.END)
    resultat_morse_francais.insert("1.0", sortie_francais_2)
def code_morse_son():
    mot_entrée = saisie_francais.get()
    francais_morse_tirets()
    if not sortie_tirets_2:
        return
    sortie_tirets_3 = " ".join(sortie_tirets_2)
    #symboles_morse = sortie_tirets_3.split()
    for symbole in sortie_tirets_3:
        if symbole == ".":
            winsound.Beep(frequence, duree_point)
        elif symbole == "-":
            winsound.Beep(frequence, duree_tiret)
        elif symbole == " ":
            time.sleep(3 * duree_point / 1000)

bienvenue = tkinter.Label(root,text="Bienvenue sur le traducto'Morse v1, veuillez choisir l'option qui vous convient ci-dessous")
bienvenue.pack()
espace_vide_1 = tkinter.Label(root,text="En Français sans espaces ni caractères spéciaux")
espace_vide_1.pack()
saisie_francais = tkinter.Entry(root)
saisie_francais.pack()
espace_vide_2 = tkinter.Label(root,text="Morse en forme ===.===.=...===")
espace_vide_2.pack()
saisie_morse = tkinter.Entry(root)
saisie_morse.pack()
espace_vide_3 = tkinter.Label(root,text="                                                                     ")
espace_vide_3.pack()
bouton_francais_morse = tkinter.Button(root, text="Français -> Morse",command=francais_morse)
bouton_francais_morse.pack()
espace_vide_4 = tkinter.Label(root,text="                                                                     ")
espace_vide_4.pack()
resultat_francais_morse = tkinter.Text(root, height=5, width=40)
resultat_francais_morse.pack()
espace_vide_5 = tkinter.Label(root,text="                                                                     ")
espace_vide_5.pack()
bouton_morse_taah = tkinter.Button(root, text="Français -> Morse avec ti et taah",command=francais_morse_taah)
bouton_morse_taah.pack()
espace_vide_6 = tkinter.Label(root,text="                                                                     ")
espace_vide_6.pack()
resultat_morse_taah = tkinter.Text(root, height=5, width=40)
resultat_morse_taah.pack()
espace_vide_7 = tkinter.Label(root,text="                                                                     ")
espace_vide_7.pack()
bouton_morse_tirets = tkinter.Button(root, text="Francais -> Morse avec -.-",command=francais_morse_tirets)
bouton_morse_tirets.pack()
espace_vide_8 = tkinter.Label(root,text="                                                                     ")
espace_vide_8.pack()
resultat_morse_tirets = tkinter.Text(root, height=5, width=40)
resultat_morse_tirets.pack()
espace_vide_9 = tkinter.Label(root,text="                                                                     ")
espace_vide_9.pack()
bouton_morse_francais = tkinter.Button(root, text="Morse -> Français",command=morse_francais)
bouton_morse_francais.pack()
espace_vide_10 = tkinter.Label(root,text="                                                                     ")
espace_vide_10.pack()
resultat_morse_francais = tkinter.Text(root, height=5, width=40)
resultat_morse_francais.pack()
espace_vide_11 = tkinter.Label(root,text="                                                                     ")
espace_vide_11.pack()
bouton_morse_son = tkinter.Button(root, text="Ecouter votre mot en Morse",command=code_morse_son)
bouton_morse_son.pack()

root.mainloop()

