from gui_lab11 import *


def main():

    window = Tk()
    window.title('Geometry Calculator')
    window.geometry('350x350')
    window.resizable(True, True)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
