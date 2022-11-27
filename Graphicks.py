import tkinter as tk
import main
print("!!")
class Graphics():
  def __init__(self, w):
    print("hey")
    self.w = w
    l1 = tk.Label(w, text = 'Hey, I am your assistand!', bg = "#CFF5E7",  font = 'Arial 40')
    l1.pack(expand = True, fill = "both", padx = 5, pady = 5)

    frame = tk.Frame(self.w, padx = 5, pady = 5)
    frame.pack(expand = True, fill = "both", padx = 10, pady = 10)

    b =tk.Button(frame, text = "Let's Start!", font = "Arial 20",bg = "#59C1BD",  command = self.pressed)
    b.pack(expand = True, fill = "both", padx = 5, pady = 5)

  def pressed(self):
    print("I was presset")
    
    main.main()
    



w = tk.Tk()
w.geometry("900x500")
w.title("Assistand")
Graphics(w)
print("!!@@")
w.mainloop()
