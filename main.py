# Package using "pyinstaller --onefile --add-data "icon.ico;." main.py" using interpreter with all requirements installed


from src.gui.start_screen import MainWindow


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
