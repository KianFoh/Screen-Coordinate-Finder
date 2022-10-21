import PIL
import tkinter
from tkinter import *
import keyboard
import pyautogui

#window
root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Screen coordinate finder")
root.configure(bg='gray')

#Label & Entry declaration
x_lable = Label(root, text='X:',bg = "gray", font='arial 10')
y_lable = Label(root, text='Y:', bg="gray", font='arial 10')
rgb_lable = Label(root, text='RGB:', bg="gray", font='arial 10')
instruction_lable =Label(root, text='Move your mouse cursor And \n press Space to capture the coordinate', bg="gray", font='arial 12 bold')
coordinate_x = Entry(root, bg="white", font='arial 10', width=5)
coordinate_y = Entry(root, bg="white", font='arial 10', width=5)
rgb_code = Entry(root, bg="white", font='arial 10', width=10)
coordinate_x.place(x=170, y=50)
coordinate_y.place(x=170, y=100)
rgb_code.place(x=295,y =75)

def capture_coordinate ():
        if keyboard.is_pressed('space'):
                coordinate_x.delete(0, 'end')
                coordinate_y.delete(0, 'end')
                rgb_code.delete(0, 'end')
                # Get new coordinate and rgb code
                coordinate = pyautogui.position()
                image = pyautogui.screenshot()
                pixel = image.getpixel(coordinate)
                x = coordinate[0]
                y = coordinate[1]
                rgb = str(pixel[0]) + ',' + str(pixel[1]) + ',' + str(pixel[2])
                coordinate_x.insert(0, x)
                coordinate_y.insert(0, y)
                rgb_code.insert(0, rgb)

        root.after(5, capture_coordinate)

x_lable.place(x= 150 , y = 50)
y_lable.place(x=150, y=100)
rgb_lable.place(x= 250, y = 75)
instruction_lable.place(x=75, y=150)
root.after(5, capture_coordinate)
root.mainloop()
