'''
Created By Stavros Stathopoulos 27/11/22
'''
import tkinter as tk
import mainfunc
from threading import Thread
#this class is providing the programm with the graphicks
class Graphics():
    path_warning = r"matterials\sign-warning-icon_34355.ico"
    path_icon = r"matterials\icon.ico"
    bg_colour = "#CFF5E7"
    fg_colour = "#59C1BD"
    font_40 = "Arial 40"
    font_20 = "Arial 20"
    font_15 = "Arial 15"
    def __init__(self, w):
      #This function Starts the first welcome window of the up. It is using a button to confirm and a labbel to inform the user
        self.w = w
        self.canvas = tk.Canvas(w, width=400, height=200 )
        self.canvas.pack(padx = 40, pady = 40)
        l1 = tk.Label(self.canvas, text = 'Hey, I am your assistand!', bg = Graphics.bg_colour,  font = Graphics.font_40)
        l1.pack(expand = True, padx = 0, pady = 0)
        b =tk.Button(self.canvas, text = "Let's Start!", font = Graphics.font_20 ,bg = Graphics.fg_colour,  command = self.iampressed)
        b.pack(expand = True, fill = "both", padx = 0, pady = 0)

    #the following function is activated when the user presses the let's start button
    def iampressed(self):
      #it opens a second window to inform the user for the terms of use. It creates a check button and when the user checks it there are two buttons to confirm that he agrees or not
      self.answer = tk.Tk()
      self.answer.configure(bg = Graphics.bg_colour)
      self.answer.geometry("600x200")
      self.answer.iconbitmap(Graphics.path_warning)
      self.answer.title("Confirmation")
      l6 = tk.Label(self.answer, text = "Question", bitmap = "question", bg = Graphics.bg_colour)
      l6.pack()
      l3 = tk.Label(self.answer, text = "By pressing agree,\n you are granding access to your microphone \nand your location!", bg = Graphics.bg_colour, font = Graphics.font_20)
      l3.pack(expand = True, fill = "both", padx = 0, pady = 0)
      self.terms_of_use = tk.Checkbutton(self.answer, text = "I wonna read the terms of use", bg = Graphics.bg_colour, font = Graphics.font_15, command = self.terms_of_use_window)
      self.terms_of_use.pack(expand = True, fill = "both", padx = 0, pady = 0)
      #Graphics.terms_of_use_window(self)
    def i_have_read_the_terms(self):
      termsbutton = tk.Checkbutton(self.terms, text = "I read the terms of use", bg = Graphics.bg_colour, font = Graphics.font_15, command = self.agreedisagreebtns)
      termsbutton.pack(expand = True, fill = "both", padx = 0, pady = 0)
      self.frame2 = tk.Frame(self.terms,bg = Graphics.bg_colour, padx = 0, pady = 0)
      self.frame2.pack(expand = True, fill = "both", padx = 0, pady = 0)

    #these are the buttons agree and disagree
    def agreedisagreebtns(self):
      b2 = tk.Button(self.frame2, text = "Agree",font = Graphics.font_20,bg = Graphics.fg_colour, command=self.agreepressed )
      b2.pack(side="left", padx = 30, pady = 30)
      b3 = tk.Button(self.frame2, text = "Disagree",font = Graphics.font_20,bg = Graphics.fg_colour, command=self.disagreepressed )
      b3.pack(side="right", padx = 30, pady = 30)

    #this function is starting the assistand when the user is agreeing
    def agreepressed(self):
      self.answer.destroy()
      self.w.destroy()
      self.terms.destroy()
      self.agreeanswer = tk.Tk()
      self.agreeanswer.configure(bg = Graphics.bg_colour)
      self.agreeanswer.geometry("500x150")
      self.agreeanswer.iconphoto(False, tk.PhotoImage( file=Graphics.path_icon))
      self.agreeanswer.title("Assistand")
      l5 = tk.Label(self.agreeanswer, text = "Assistand is starting right away!", font = Graphics.font_20, bg = Graphics.bg_colour)
      l5.pack(pady = 30)
      ##target=thread_function, args=(index,)
      #start = Thread(target=self.open_main, args=(self,))
      #mainfunc.main()
      self.open_main()

    #this function is closing the assistand when the user is disagreeing
    def disagreepressed(self):
      self.answer.destroy()
      self.w.destroy()
      self.terms.destroy()
      self.disanswer = tk.Tk()
      self.disanswer.configure(bg = Graphics.bg_colour)
      self.disanswer.geometry("500x150")
      self.disanswer.title("Sorry")
      self.disanswer.iconphoto(False, tk.PhotoImage(file=Graphics.path_icon))
      l4 = tk.Label(self.disanswer, text = "Sorry without accepting the terms of use\n assistand can't work!", font = Graphics.font_20, bg = Graphics.bg_colour)
      l4.pack(pady = 30)
    #
    def terms_of_use_window(self):
      self.terms = tk.Tk()
      self.terms.configure(bg = Graphics.bg_colour)
      self.terms.geometry("500x200")
      self.terms.iconbitmap(Graphics.path_warning)
      self.terms.title("Terms Of Use")
      termslabel = tk.Label(self.terms, text = "the terms of use" , font = Graphics.font_20, bg = Graphics.bg_colour)
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
    def open_main(self):
      self.agreeanswer.destroy
      self.started= tk.Tk()
      self.started.configure(bg = self.bg_colour)
      self.started.geometry("800x240")
      self.started.title("Assistand")
      #self.started.iconphoto(False, tk.PhotoImage(file=Graphics.path_icon))
      Thread(target = mainfunc.main(), args=())
      




    

#the main window parrameters
w = tk.Tk()
w.configure(bg = Graphics.bg_colour)
w.geometry("800x240")
w.title("Assistand")
w.iconphoto(False, tk.PhotoImage(file=Graphics.path_icon))
Graphics(w)
w.mainloop()