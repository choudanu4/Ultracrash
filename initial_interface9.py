from tkinter import *
import os


file_path = os.getcwd()

class Application(Frame):
    
    final_path=None   
        

    def __init__(self, master, radio_var):
        super(Application, self).__init__(master)
        self.grid()
        self.pathway = None
        self.create_widgets(radio_var)

    def execute(self, game):
        """Takes a game option and executes corresponding file."""
        kookoo = game.get()
        Application.final_path= file_path + "\\" + kookoo
        print(Application.final_path)

                
    def create_widgets(self, radio_var):
        radio_var.set("python")
        f1 = Frame(self)     
        f2 = Frame(self)
        f3 = Frame(self)
        photo = PhotoImage(file="welcome.gif", master=root)
        f1.button = Button(f1, image=photo)
        f1.button.photo = photo 
        f1.button.grid(column = 1)
        choose_set = Label(f2, text="Choose Set:")
        choose_set.grid(row=0,column=0,sticky=E)
        card_entry_input = StringVar()
        card_entry = Entry(f2, textvariable=card_entry_input,width=60)
        card_entry.grid(row=0,column=1)
        txt = Label(f2, text=".txt")
        txt.grid(row=0,column=2,sticky=W)
        choice_lbl = Label(f3, text="Now choose which game you would like to play:")
        choice_lbl.grid(row=0,column=0)

        ####create game RadioButtons####
        global file_path
              
        Radiobutton(master=f3,
                    text="Command Conjugators",
                    variable = radio_var,
                    value = "command_conjugators.py" ,
                    ).grid(row=1)
        Radiobutton(master=f3,
                    text="Matching Mayhem",
                    variable = radio_var,
                    value = "matching_mayhem.py" ,
                    ).grid(row=2)
        Radiobutton(master=f3,
                    text="Shooter Soilder",
                    variable = radio_var,
                    value = "shooter_soilder.py" ,
                    ).grid(row=3)
        
        ####-------------------------####
        submit = Button(f3,
                        text="¯\_(ツ)_/¯  Start Playing?",
                        command=self.execute(radio_var))
        submit.grid(row=4)
        
        
        
        f1.grid(row=0,column=0)
        f2.grid(row=1,column=0)
        f3.grid(row=2,column=0)

    
        
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    root.title("Vocabulary Funhouse")
    radio_var = StringVar()
    app = Application(root, radio_var)
    root.mainloop()
       
