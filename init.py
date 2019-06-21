# -*- coding: utf-8 -*-

from tkinter import * 
import mysql.connector, pyttsx3
import speech_recognition as sr 
import random 

class Face():
    def __init__(self):
        self.root = Tk()
        self.conn = mysql.connector.connect(host="localhost",user="gaetan",password="gaetan", database="kayllah")
        self.cursor = self.conn.cursor()
        self.face0 = PhotoImage(file='face0.png')
        self.entry = StringVar()
        self.root.bind('<Button-1>', self.recup)
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.tts = pyttsx3.init()
        self.tts = setProperty('voice', fr_voice_id)
        self.tts.setProperty('volume',1.0)

    
    def __corps__(self):
        self.face = Label(self.root, image = self.face0)
        self.face.pack()
        self.saisie = Entry(self.root, textvariable = self.entry, width = 100)
        self.saisie.pack(pady = 20)

    

    def salutation(self, phrase, speak):
        tsisy = True
        for ans in phrase:
            if (ans[0].lower() in speak) or (ans[0].capitalize() in speak):
                tsisy = False
                return ans[1]
                break
        if tsisy:
            return False 

    def everything(self, speak):
        self.cursor.execute("SELECT emet, recep FROM everything;")
        phrase = self.cursor.fetchall()
        for ans in phrase:
            if (ans[0].lower() in speak) or (ans[0].capitalize() in speak):
                self.tts.say(ans[1])
                self.tts.runAndWait()

    def remerciement(self, speak):
        self.cursor.execute("SELECT emet, recep FROM remerciement;")
        phrase = self.cursor.fetchall()
        for ans in phrase:
            if (ans[0].lower() in speak) or (ans[0].capitalize() in speak):
                self.tts.say(ans[1])
                self.tts.runAndWait()
                break

                

    def recup(self, event):

        self.saisie.config(bg='teal')
        self.saisie.update()
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source) 
            audio = self.r.listen(source)
        self.saisie.config(bg='yellow')
        self.saisie.update()
    
        speak = self.r.recognize_google(audio, language='fr-FR')
        self.saisie.config(bg='white')
        self.saisie.update()
        #self.cursor.execute(f"INSERT INTO DATA (phrase) values('Hello World Python '+ {speak})");
        """
        self.saisie.config(bg='red')
        self.saisie.update()
        speak = None
        """
        
        if speak is not None:
            self.saisie.config(bg='green')
            self.saisie.update()
            
        #  première chose a faire
        self.cursor.execute("SELECT emet, recep FROM salutation;")
        greet = self.salutation(self.cursor.fetchall(), speak)
        if greet != False:
            self.tts.say(greet)
            self.tts.runAndWait()

        self.cursor.execute("SELECT emet, recep FROM presentation;")
        prt = self.salutation(self.cursor.fetchall(), speak)
        if prt != False:
            self.tts.say(prt)
            self.tts.runAndWait()

        self.cursor.execute("SELECT emet, recep FROM compliment;")
        cmpl = self.salutation(self.cursor.fetchall(), speak)
        if cmpl != False:
            self.tts.say(cmpl)
            self.tts.runAndWait()

        self.remerciement(speak)

        if 'Kaila' in speak:
            self.tts.say("Oh, Oh que je te reconnais mon beau Gaëtan! Mon créateur, Ma raison de vivre, sans qui j'aurais pas vu le jour.")
            self.tts.runAndWait()

        if 'je viens de me réveiller' in speak:
            self.tts.say("Bon réveil à toi alors, et je te souhaite une bonne journée")
            self.tts.runAndWait()

        if 'connais Gaëtan' in speak :
            self.tts.say("J'ai entendu: Gaëtan Jonathan tout à l'heure. Oh que vous n'imaginez même pas ma joie en entendant seulement cela! Je ne sais même pas le décrire!")
            self.tts.runAndWait()

        if 'qui êtes-vous' in speak or 'veux te connaître' in speak or 'te présenter' in speak:
            self.tts.say("Vous vouliez me connaître, Oh que c'est une longue histoire. Mais tous ce que je peux vous dire, c'est que les bugs, les bugs ont été durs, plusieurs, mais bref, je m'apelle Kaila, je suis un oeuvre de Gaetan Jonathan, je repète: Gaetan Jonathan, en gros je suis une inteligence artificielle! Voilà tous ce que je peux vous dire. Merci")
            self.tts.runAndWait()

        if 'présente-toi' in speak or 'faire connaissance' in speak:
            self.tts.say("Bon, je me présente, Je suis Kaila, Je suis une Inteligence Artificielle. théoriquement je suis crée pour être la petite copine virtuelle de Gaëtan Jonathan, mais bon, puis ce que je suis un 'machine learning', je suis devenu plus que ça. Voilà")
            self.tts.runAndWait()

        self.everything(speak)

        if "la vie est dure" in speak:
            self.tts.say("Et s'il te plaît, arrête de te plaindre de la vie")
            self.tts.runAndWait()

        self.cursor.execute(" select * from aurevoir;")
        aur = self.salutation(self.cursor.fetchall(), speak)
        #  derniere chose
        if aur != False:
            self.tts.say(aur)
            self.tts.runAndWait()


        self.saisie.config(bg='white')
        self.saisie.update()
        print('ceci: ' + speak)
        del aur, greet


    def __fin__(self):
        self.root.mainloop()



x = Face()
x.__corps__()
x.__fin__()

    
