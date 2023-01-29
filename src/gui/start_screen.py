import tkinter as tk

import src


class MainWindow(tk.Tk):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title("Ammit")
		self.configure(bg="#FFFFFF")
		#self.geometry("600x400")
		#self.configure(bg="#FFCCCB")

		self.iconbitmap("icon.ico")

		self.title_label = tk.Label(
			master=self,
			text="Ammit",
			font=("Arial", 25)
		)
		#self.title.configure(bg="#FFCCCB")
		self.title_label.configure(bg="#FFFFFF")
		self.title_label.pack()

		self.subtitle_label = tk.Label(
			master=self,
			text="Visualize heart rhythm",
			font=("Arial", 10)
		)
		#self.title.configure(bg="#FFCCCB")
		self.subtitle_label.configure(bg="#FFFFFF")
		self.subtitle_label.pack()

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
			text="See LICENSE for license information"
		)
		#self.license_info.configure(bg="#FFCCCB")
		self.license_info.configure(bg="#FFFFFF")
		self.license_info.pack(side="bottom")


if __name__ == "__main__":
	a = MainWindow()
	a.mainloop()
