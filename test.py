import tkinter as tk
import mainfunc
import speech_recognition as sr
import pyttsx3
import webSearching
import stringManipulation

#this function is the main. It starts the assistand
#

#this class is providing the programm with the graphicks
class Graphics():

    def __init__(self, w):
      #This function Starts the first welcome window of the up. It is using a button to confirm and a labbel to inform the user
        self.w = w
        self.canvas = tk.Canvas(w, width=400, height=200 )
        self.canvas.pack(padx = 40, pady = 40)
        l1 = tk.Label(self.canvas, text = 'Hey, I am your assistand!', bg = "#CFF5E7",  font = 'Arial 40')
        l1.pack(expand = True, padx = 0, pady = 0)
        b =tk.Button(self.canvas, text = "Let's Start!", font = "Arial 20",bg = "#59C1BD",  command = self.iampressed)
        b.pack(expand = True, fill = "both", padx = 0, pady = 0)

    #the following function is activated when the user presses the let's start button
    def iampressed(self):
      #it opens a second window to inform the user for the terms of use. It creates a check button and when the user checks it there are two buttons to confirm that he agrees or not
      self.answer = tk.Tk()
      self.answer.configure(bg = "#CFF5E7")
      self.answer.geometry("600x200")
      self.answer.iconbitmap(r'C:\Users\sstav\OneDrive\Desktop\AI_assistant-main\warning - Αντιγραφή.ico')
      self.answer.title("Confirmation")
      l6 = tk.Label(self.answer, text = "Question", bitmap = "question", bg = "#CFF5E7")
      l6.pack()
      l3 = tk.Label(self.answer, text = "By pressing agree,\n you are granding access to your microphone \nand your location!", bg = "#CFF5E7", font = "Arial 20")
      l3.pack(expand = True, fill = "both", padx = 0, pady = 0)
      self.terms_of_use = tk.Checkbutton(self.answer, text = "I wonna read the terms of use", bg = "#CFF5E7", font = "Arial 15", command = self.terms_of_use_window)
      self.terms_of_use.pack(expand = True, fill = "both", padx = 0, pady = 0)
      #Graphics.terms_of_use_window(self)
    def i_have_read_the_terms(self):
      termsbutton = tk.Checkbutton(self.terms, text = "I read the terms of use", bg = "#CFF5E7", font = "Arial 15", command = self.agreedisagreebtns)
      termsbutton.pack(expand = True, fill = "both", padx = 0, pady = 0)
      self.frame2 = tk.Frame(self.terms,bg = "#CFF5E7", padx = 0, pady = 0)
      self.frame2.pack(expand = True, fill = "both", padx = 0, pady = 0)

    #these are the buttons agree and disagree
    def agreedisagreebtns(self):
      b2 = tk.Button(self.frame2, text = "Agree",font = "Arial 20",bg = "#59C1BD", command=self.agreepressed )
      b2.pack(side="left", padx = 30, pady = 30)
      b3 = tk.Button(self.frame2, text = "Disagree",font = "Arial 20",bg = "#59C1BD", command=self.disagreepressed )
      b3.pack(side="right", padx = 30, pady = 30)

    #this function is starting the assistand when the user is agreeing
    def agreepressed(self):
      self.answer.destroy()
      self.w.destroy()
      self.terms.destroy()
      self.agreeanswer = tk.Tk()
      self.agreeanswer.configure(bg = "#CFF5E7")
      self.agreeanswer.geometry("500x150")
      self.agreeanswer.iconphoto(False, tk.PhotoImage(file=r'C:\Users\sstav\OneDrive\Desktop\AI_assistant-main\icon.ico'))
      self.agreeanswer.title("Assistand")
      l5 = tk.Label(self.agreeanswer, text = "Assistand is starting right away!", font = "Arial 20", bg = "#CFF5E7")
      l5.pack(pady = 30)
      #mainfunc.main()
      #if (mainfunc.main.MyText == "terminate"):
       # Graphics.terminate()

    #this function is closing the assistand when the user is disagreeing
    def disagreepressed(self):
      self.answer.destroy()
      self.w.destroy()
      self.terms.destroy()
      self.disanswer = tk.Tk()
      self.disanswer.configure(bg = "#CFF5E7")
      self.disanswer.geometry("500x150")
      self.disanswer.title("Sorry")
      self.disanswer.iconphoto(False, tk.PhotoImage(file=r'C:\Users\sstav\OneDrive\Desktop\AI_assistant-main\icon.ico'))
      l4 = tk.Label(self.disanswer, text = "Sorry without accepting the terms of use\n assistand can't work!", font = "Arial 20", bg = "#CFF5E7")
      l4.pack(pady = 30)
    #
    def terms_of_use_window(self):
      self.terms = tk.Tk()
      self.terms.configure(bg = "#CFF5E7")
      self.terms.geometry("500x200")
      self.terms.iconbitmap(r'C:\Users\sstav\OneDrive\Desktop\AI_assistant-main\warning - Αντιγραφή.ico')
      self.terms.title("Terms Of Use")
      termslabel = tk.Label(self.terms, text = "the terms of use" , font = "Arial 20", bg = "#CFF5E7")
      termslabel.pack()

      self.i_have_read_the_terms()
    def terminate(self):
      try:
        self.terms.destroy
        self.disanswer.destroy
        self.agreeanswer.destroy
        self.w.destroy
        self.answer.destroy
      except:
        pass
    
#the main window parrameters
w = tk.Tk()
w.configure(bg = "#CFF5E7")
w.geometry("800x240")
w.title("Assistand")
w.iconphoto(False, tk.PhotoImage(file=r'C:\Users\sstav\OneDrive\Desktop\AI_assistant-main\icon.ico'))
Graphics(w)


w.mainloop()