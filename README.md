# Shivay-1.02
HARDWARE AND SOFTWARE REQUIREMENT





🡺	HARDWARE REQUIREMENT: -

1)	OPERATING SYSTEM	:	Windows 7 and Above
2)	PROCESSOR			:	ANY (recommended – intel  
core-i series)
3)	RAM					:	1GB+
4)	KEYBOARD AND MOUSE


    🡺 SOFTWARE REQUIREMENT: -
	
1)	WINDOWS OS
2)	PYTHON	
 
DESCRIPTION OF THE PROJECT



1)	FEATURES AND USES/PURPOSE: -  

This project is a semi-CUI (Character User Interface) and semi-GUI (Graphic User Interface) based operating system. This also contains encrypted username and password which makes is safer. In home page will find the following options.: -

[1] To Open Google
[3] To Open File Explorer
[4] To Configure and Open Bios’
[5] To Open Terminal
[6] To Open Calculator
[7] To Open Digital Clock
[8] To Close OS Safely

Here Calculator, digital clock and text editor are totally based on GUI whereas you will find others to be idle.
 
2)	INPUT AND OUTPUT: -

In this project you have to give input by using numbers like by entering number 6 a calculator will open or by entering number 3 your file explorer will open.

While talking separately:
1)	Google – You have to enter the URL of the page you want to open
2)	File Explorer – This feature just opens your file explorer where you can move your file or open any file.
3)	Configure and Bios’ – This feature is very helpful in changing password and username. At first you will be asked your current username and password which is encrypted in another file as mentioned above.
4)	Terminal – This is my own made command prompt which have all those features in it.
5)	Calculator – This is a totally GUI based calculator which allows you to add, multiply, subtract, divide, powers, roots and much more.
6)	Digital Clock – This is a GUI based clock which tells you the current time.
7)	Close OS Safely – This exits the OS.
 
FLOW CHART / WORKING / PROGRAM LOGIC: -
 
3)	WHO ARE THE USERS: - 

All the people who want to use a mixed OS which is not only based on CUI but also on GUI. This feature makes it the best in market.
 
 


 








1)	  Dataname.pass: -


	Shivay



2)	  Info.data: -


	1

3)	 Password.pass: -

	1234

4)	alert.py: -

from tkinter import messagebox, Tk


def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


if __name__ == '__main__':
    Tk().withdraw()
    alert('Hello', 'Hello World')
    alert('Hello Again', 'Hello World 2', kind='warning')


5)	brows.py: -

import webbrowser







print('''

░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░██████╗░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗╚════██╗
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║░░███╔═╝
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║██╔══╝░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝

░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ 
███████╗███╗░░██╗░██████╗░██╗███╗░░██╗███████╗
██╔════╝████╗░██║██╔════╝░██║████╗░██║██╔════╝
█████╗░░██╔██╗██║██║░░██╗░██║██╔██╗██║█████╗░░
██╔══╝░░██║╚████║██║░░╚██╗██║██║╚████║██╔══╝░░
███████╗██║░╚███║╚██████╔╝██║██║░╚███║███████╗
╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝
''')


while True:
    browser = input("Serch Browser or Type URL: ")
    webbrowser.open(browser)

6)	calc.py: -

import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Shivay 1.02 Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()


7)	clock.py: -


from tkinter import *
from datetime import datetime
from time import strftime
from PIL import ImageTk,Image

w=Tk()
w.geometry('1280x720')
w.minsize(750,200)
w.title("Digital Clock")


#Extracting day 
a=datetime.today().strftime('%A')
b=(a.upper())
c=(b[0:2]) 

#setting background
img1=Image.open("g3.jpg")
img2= ImageTk.PhotoImage(img1)
Label(w,image=img2).place(x=-2,y=0)


f1=Frame(w,width=750, height=200,bg='#0e1013')
f1.pack(expand=True)

#Mechenism
def time():
    a=strftime('%H : %M : %S')  #%H   %M   %S
    l1.config(text=a)
    l1.after(1000,time)

l1=Label(f1, font=('Century Gothic',60),
          bg='#0e1013',
          foreground='#d3d3d3')

l1.place(x=275,y=35)
time()

l2=Label(f1, font=('Century Gothic',60),
          bg='#0e1013',
          foreground='#d3d3d3')
l2.config(text=c+" |")
l2.place(x=75,y=35)

#Required labels
def labels():
    l3=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='DAY')
    l3.place(x=122,y=130)

    l4=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='HOURS')
    l4.place(x=305,y=130)

    l5=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='MINUTES')
    l5.place(x=445,y=130)

    l3=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='SECONDS')
    l3.place(x=445+145+5,y=130)

labels()

w.mainloop()


8)	file.pyw: -

from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",title="Shivay 1.02 Open",filetypes= (("text files","*.txt"),("all files","*.*")))
    os.startfile(filepath)

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()


9)	g3.jpg: -

 



10)	home.py: -
import time
import os
import socket
from tkinter import messagebox, Tk

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()

print('''


░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░██████╗░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗╚════██╗
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║░░███╔═╝
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║██╔══╝░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝
''')


print("Welcome " + l_n)
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("""
[1] To Open Google 
[3] To Open File Explorer
[4] To Configure and Open BioS
[5] To Open Terminal
[6] To Open Calculator
[7] To Open Digital Clock
[8] To Close OS Safely
""")

select = input("[?]: ")

if select == '1':
   os.startfile('home.py')
   os.startfile('brows.py')
 
elif select == '3':
   os.startfile('home.py')
   os.startfile('file.pyw')

elif select == '4':
   while True:
      b_login = input(str("Please Enter The Password " + l_n + " To Open BioS: "))
      if b_login == l_p:
         print("Opening BioS")
         host_name = socket.gethostname()
         host_ip = socket.gethostbyname(host_name)
         print("[1] USER NAME: " + l_n)
         print("[2] PASSWORD: " + l_p)
         print("Hostname:", host_name)
         print("LOCAL IPS: " + host_ip)
         print()
         print()
         print("Enter [3] to exit BIOS")
         edit_b = input("Enter [?] to change setting: ")
         if edit_b == '1':
            edit_n = input("Enter New Username: ")
            with open('user/dataname.pass', 'w') as f:
               f.writelines(edit_n)
            print("Username Changed To " + edit_n)
            input("Press Enter To Restart: ")
            os.startfile('home.py')
            os.system('exit')

         elif edit_b == '2':
            edit_p = input("Enter New Password: ")
            with open('user/password.pass', 'w') as f:
               f.writelines(edit_p)

            print("Password Changed To " + edit_p)
            input("Press Enter To Restart: ")
            os.startfile('home.py')
            os.system('exit')

         elif edit_b == '3':
            os.startfile('home.py')
            os.system('exit')
      else:
         def alert(title, message, kind='info', hidemain=True):
            if kind not in ('error', 'warning', 'info'):
               raise ValueError('Unsupported alert kind.')

            show_method = getattr(messagebox, 'show{}'.format(kind))
            show_method(title, message)


         if __name__ == '__main__':
            Tk().withdraw()
            alert('Alert', 'Wrong Password!', kind='warning')

elif select == '5':
   os.startfile('home.py')
   os.startfile('terminal.py')

elif select == '6':
   os.startfile('home.py')
   os.startfile('calc.py')

elif select == '7':
   os.startfile('home.py')
   os.startfile('clock.py')

elif select == '8':
   os.system('exit')

else:
   def alert(title, message, kind='info', hidemain=True):
      if kind not in ('error', 'warning', 'info'):
         raise ValueError('Unsupported alert kind.')

      show_method = getattr(messagebox, 'show{}'.format(kind))
      show_method(title, message)


   if __name__ == '__main__':
      Tk().withdraw()
      alert('Alert', 'Please enter an input lying between 1 to 8')
      os.startfile('home.py')


11)	login.py: -

import os
import time
from tkinter import messagebox, Tk

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()


print('''
░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░██████╗░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗╚════██╗
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║░░███╔═╝
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║██╔══╝░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝

██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝



With Alert box, Digital Clock and Improved Calculator!!!
''')


while True:
   log = input("Enter Password To " + l_n + " To Login: ")

   if log == l_p:
      print("Opening Home Page...")
      time.sleep(0.5)
      os.startfile("home.py")
      break

   else:
      def alert(title, message, kind='info', hidemain=True):
         if kind not in ('error', 'warning', 'info'):
            raise ValueError('Unsupported alert kind.')

         show_method = getattr(messagebox, 'show{}'.format(kind))
         show_method(title, message)


      if __name__ == '__main__':
         Tk().withdraw()
         alert('Alert', 'Wrong Password!', kind='warning')



12)	setup.py: -

import os
import time

with open('user/info.data', 'w') as f:
   f.writelines("1")


print('''
░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░██████╗░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗╚════██╗
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║░░███╔═╝
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║██╔══╝░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝

░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
''')


name = input("Please Enter Your Username To Be Displayed: ")
pas = input("Please Enter Your Password To Login: ")

with open('user/dataname.pass', 'w') as f:
   f.writelines(name)

with open('user/password.pass', 'w') as f:
   f.writelines(pas)

print("Setup Complete!!!")
print("Opening Login Page...")
time.sleep(0.5)
os.startfile('login.py')


13)	Shivay1_02.py: -

import os

data_info = open('user/info.data')
data = data_info.read()

if data == '0':
   print("Opening Register Page...")
   os.startfile("setup.py")

if data == '1':
   print("Opening Login Page...")
   os.startfile("login.py")


14)	terminal.py: -
import os

print("""
░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░██████╗░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗╚════██╗
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║░░███╔═╝
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║██╔══╝░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝

████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝

    
""")

while True:
    command = input(">>> ")
    os.system(command) 
 



 



 



 
 

 
 
 
 

 
  
BIBLIOGRAPHY
1.	Python.org
2.	Geeksforgeeks.com
3.	Programiz.com
4.	And many more which I have not recorded.
