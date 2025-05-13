import tkinter
from LogIn import FereastraLogIn

class MeniuPrincipal:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title = 'test'
        self.root.geometry = '300x300'

        
        self.root.mainloop()

    def fereastra_log_in(self):
        ferastra = FereastraLogIn()

if __name__ == '__main__':
    
    meniuprincipal = MeniuPrincipal()
    meniuprincipal.fereastra_log_in()