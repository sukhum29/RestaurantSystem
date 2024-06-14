"""

"""

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from mainwindow import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
