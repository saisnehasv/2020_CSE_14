from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import tkinter as tk, threading


global UploadAction
global file,video

def fnm():
    global filename
    filename = filedialog.askopenfilename()
    return filename

def UploadAction(event=None):
    fname=fnm()
    print(fname)

def btn_clicked():
    print("Button Clicked")


def stream(label):
     os.system(filename)

def func():
        my_label = tk.Label(window)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()
        
def openProgram():
    os.system("python evaluation\predict.py evaluation\models\overlapped-weights368.h5 " + filename)

def new_window():    
            root.destroy()
            global window
            window = Tk()

            window.geometry("862x519")
            window.title("Intuitive Perception")
            img = ImageTk.PhotoImage(Image.open("images/icon.jpeg"))
            window.iconphoto(False,img)
            window.configure(bg = "#ffffff")
            canvas = Canvas(
                window,
                bg = "#ffffff",
                height = 519,
                width = 862,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)


            canvas.create_rectangle(
                0, 472, 0+862, 472+47,
                fill = "#0d0b72",
                outline = "")


            canvas.create_rectangle(
                0, 0, 0+862, 0+27,
                fill = "#0d0b72",
                outline = "")

            canvas.create_text(
                431.0, 102.5,
                text = "Intuitive Perception",
                fill = "#080c63",
                font = ("CenturyGothic-Bold", int(24.0)))

            canvas.create_text(
                430.5, 165.0,
                text = "Upload a video to generate subtitles",
                fill = "#000000",
                font = ("CenturyGothic-Bold", int(13.0)))

            img0 = PhotoImage(file = f"images/img0.png")
            b0 = Button(
                image = img0,
                borderwidth = 0,
                highlightthickness = 0,
                command = UploadAction,
                relief = "flat")

            b0.place(
                x = 187, y = 313,
                width = 127,
                height = 38)

            img1 = PhotoImage(file = f"images/img1.png")
            b1 = Button(
                image = img1,
                borderwidth = 0,
                highlightthickness = 0,
                command = func,
                relief = "flat")

            b1.place(
                x = 375, y = 313,
                width = 127,
                height = 38)

            img2 = PhotoImage(file = f"images/img2.png")
            b2 = Button(
                image = img2,
                borderwidth = 0,
                highlightthickness = 0,
                command = openProgram,
                relief = "flat")

            b2.place(
                x = 558, y = 313,
                width = 127,
                height = 38)

            image_0 = PhotoImage(file = "images/image_0.png")
            canvas_image_0 = canvas.create_image(
                625.0, 272.0,
                image=image_0)

            image_1 = PhotoImage(file = "images/image_1.png")
            canvas_image_1 = canvas.create_image(
                439.0, 271.0,
                image=image_1)

            image_2 = PhotoImage(file = "images/image_2.png")
            canvas_image_2 = canvas.create_image(
                250.5, 272.0,
                image=image_2)

            window.resizable(False, False)
            window.mainloop()
            

root = Tk()

root.geometry("862x519")
root.title("Intuitive Perception")
img = ImageTk.PhotoImage(Image.open("images/icon.jpeg"))
root.iconphoto(False,img)
root.configure(bg = "#080c63")
canvas = Canvas(
    root,
    bg = "#080c63",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431, 0, 431+431, 0+519,
    fill = "#ffffff",
    outline = "")

title = Label(text="Welcome to Intuitive Perception", bg="#080c63",fg="white",font=("CenturyGothic-Bold",int(16.0)))
title.place(x=30.0,y=78.0)

canvas.create_rectangle(
    55, 130, 55 + 240, 130 + 5,
    fill = "#ffffff",
    outline = "")
    
info_text = Label(text="Use our application to generate subtitles \n"
                   "for videos.\n\n"

                   "What makes Intuitive percetion better?\n\n"

                   "We aim to generate subtitles for Videos\n"
                   "independent of the audio.\n\n"

                   "Our software uses machine learning to\n"
                   "achieve this with the accuracy rate\n"
                   "between 70-80%.",
              bg="#080c63",fg="white",justify="left",font=("CenturyGothic",int(13.0)))

info_text.place(x=27.0,y=178.0)


canvas.create_text(
    650.5,88.0,
    text = "Instructions",
    fill = "#080c63",
    font = ("CenturyGothic-Bold", int(20.0)))

steps_text = Label(text="Follow the 3 Simple Instructions.\n\n\n"
                        "Step 1: Click on Add Video button to add \n"
                        "            the video of your choice.\n\n"
                        "Step 2: You can verify the video selected\n"
                        "            by clicking on the Play Video button.\n\n"
                        "Step 3: To process the video and get the\n"
                        "            subtitles, Click on Generate Subtitles\n"
                        "            button\n.",
              bg="#ffffff",fg="#080c63",justify="left",font=("CenturyGothic",int(13.0))) #black :#000000 

steps_text.place(x=470,y=120.0)

img0 = PhotoImage(file = f"images/img-0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: new_window(),
    relief = "flat")
b0.place(
    x = 549, y = 400,
    width = 195,
    height = 54)





root.resizable(False, False)
root.mainloop()