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