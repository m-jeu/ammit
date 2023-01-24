import tkinter as tk

import src


class MainWindow(tk.Tk):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title("Ammit")
		self.configure(bg="#FFFFFF")
		#self.geometry("600x400")
		#self.configure(bg="#FFCCCB")

		self.title = tk.Label(
			master=self,
			text="Ammit",
			font=("Arial", 25)
		)
		#self.title.configure(bg="#FFCCCB")
		self.title.configure(bg="#FFFFFF")
		self.title.pack(pady=10)

		self.button = tk.Button(
			master=self,
			text="Open file",
			command=src.fetch_and_show,
			width=15,
			height=5,
			bd=1
		)
		#self.button.configure(bg="#FFCCCB")
		self.button.configure(bg="#FFFFFF")
		self.button.pack(pady=10)

		#self.button_license = tk.Button(
		#    master=self,
		#    text="License",
		#    command=lambda: os.system("notepad.exe LICENSE"),
		#    width=20,
		#    height=5,
		#)
		#self.button_license.pack()

		#self.text = tk.Label(
		#	master=self,
		#	text="Press the button to open a file."
		#)
		#self.text.configure(bg="#FFCCCB")
		#self.text.configure(bg="#FFFFFF")
		#self.text.pack(pady=10)

		self.license_info = tk.Label(
			master=self,
			text="Maarten de Jeu, 2022.\n See LICENSE for license information."
		)
		#self.license_info.configure(bg="#FFCCCB")
		self.license_info.configure(bg="#FFFFFF")
		self.license_info.pack(side="bottom")


if __name__ == "__main__":
	a = MainWindow()
	a.mainloop()
