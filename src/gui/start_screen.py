import tkinter as tk
import os
import sys
import src


class MainWindow(tk.Tk):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title("Ammit")
		self.configure(bg="#FFFFFF")

		"""self.iconbitmap("icon.ico")"""
		root_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
		icon_path = os.path.join(root_path, "icon.ico")
		self.iconbitmap = tk.PhotoImage(icon_path)

		self.title_label = tk.Label(
			master=self,
			text="Ammit",
			font=("Arial", 25)
		)

		self.title_label.configure(bg="#FFFFFF")
		self.title_label.pack()

		self.subtitle_label = tk.Label(
			master=self,
			text="Visualize heart rhythm",
			font=("Arial", 10)
		)

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

		self.button.configure(bg="#FFFFFF")
		self.button.pack(pady=10)

		self.license_info = tk.Label(
			master=self,
			text="See LICENSE for license information"
		)

		self.license_info.configure(bg="#FFFFFF")
		self.license_info.pack(side="bottom")
