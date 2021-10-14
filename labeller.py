import os
import numpy as np
import pandas as pd
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image, ImageEnhance

if __name__ == "__main__":
    if not os.path.exists('labels.csv'):  # if no labels.csv build dataframe and create file
        images = sorted(os.listdir('./images/'))
        lat = [im.split(',')[0] for im in images]
        lon = [im.split(',')[1][:-4] for im in images]
        data = pd.DataFrame({'Filename': images, 'Lat': lat, 'Lon': lon})
        data['Street'] = ''
        data['Foreign Object'] = ''
        data['Shadow'] = ''
        data.to_csv('labels.csv', index=False)
        del data

    data = pd.read_csv('labels.csv')
    df = data.copy(deep=True)

    # randomly choose from images that haven't been labelled
    df = df.loc[df['Street'].isna()]
    random_sample = np.random.choice(df.index, size=len(df), replace=False)

    # start looping through the images and building gui's
    i = 0
    keep_going = True
    while keep_going:
        rs = random_sample[i]
        filename = f"./images/{df.loc[rs, 'Filename']}"
        # instantiate tkinter gui object
        root = tk.Tk()


        def on_closing():  # don't break if we close the window
            root.destroy()


        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.geometry("975x675")
        root.title("Label Images")
        im = Image.open(filename)
        im = ImageEnhance.Contrast(im).enhance(1.5)
        im = PhotoImage(im)
        #  im = PhotoImage(Image.open(filename))
        canvas = tk.Canvas(root, width=640, height=640)
        canvas.pack(anchor='nw')
        canvas.create_image(0, 0, anchor='nw', image=im)

        # create Street variable
        street = tk.StringVar(root, value='Good')
        # create radio button
        slabel = tk.Label(root, text='Street Condition', font='bold')
        slabel.place(x=800, y=5)
        s1 = tk.Radiobutton(root, text='Good', variable=street, value='Good', command=None, )
        s1.place(x=800, y=25)
        s2 = tk.Radiobutton(root, text='Crack', variable=street, value='Crack', command=None, )
        s2.place(x=800, y=45)
        s3 = tk.Radiobutton(root, text='Pothole', variable=street, value='Pothole', command=None, )
        s3.place(x=800, y=65)
        s4 = tk.Radiobutton(root, text='Crack (Repaired)', variable=street, value='Crack (Repaired)', command=None, )
        s4.place(x=800, y=85)

        # create Foreign Object variable
        for_obj = tk.StringVar(root, value='None')
        # for_obj = tk.StringVar(root, value=for_obj_val)
        flabel = tk.Label(root, text='Foreign Object', font='bold')
        flabel.place(x=800, y=125)
        f1 = tk.Radiobutton(root, text='None', variable=for_obj, value='None', command=None, )
        f1.place(x=800, y=145)
        f15 = tk.Radiobutton(root, text='Car', variable=for_obj, value='Car', command=None, )
        f15.place(x=800, y=165)
        f2 = tk.Radiobutton(root, text='Car (Partial)', variable=for_obj, value='Car (Partial)', command=None, )
        f2.place(x=800, y=185)
        f3 = tk.Radiobutton(root, text='Sewer', variable=for_obj, value='Sewer', command=None, )
        f3.place(x=800, y=205)
        f4 = tk.Radiobutton(root, text='Plant', variable=for_obj, value='Plant', command=None, )
        f4.place(x=800, y=225)
        f5 = tk.Radiobutton(root, text='Person', variable=for_obj, value='Person', command=None, )
        f5.place(x=800, y=245)
        f6 = tk.Radiobutton(root, text='Sidewalk', variable=for_obj, value='Sidewalk', command=None, )
        f6.place(x=800, y=265)
        f6 = tk.Radiobutton(root, text='Other', variable=for_obj, value='Other', command=None, )
        f6.place(x=800, y=285)

        # create Shadow variable
        shadow = tk.StringVar(root, value='No')
        # shadow = tk.StringVar(root, value=shadow_val)
        flabel = tk.Label(root, text='Shadow', font='bold')
        flabel.place(x=800, y=325)
        f1 = tk.Radiobutton(root, text='Yes', variable=shadow, value='Yes', command=None, )
        f1.place(x=800, y=345)
        f2 = tk.Radiobutton(root, text='No', variable=shadow, value='No', command=None, )
        f2.place(x=800, y=365)


        # functions for buttons
        def save_values():
            global i
            global data
            data.loc[rs, 'Street'] = street.get()
            data.loc[rs, 'Foreign Object'] = for_obj.get()
            data.loc[rs, 'Shadow'] = shadow.get()
            data.to_csv('labels.csv', index=False)
            i += 1
            root.destroy()


        def go_back():
            global i
            i -= 1
            root.destroy()


        def finish():
            global keep_going
            keep_going = False
            root.destroy()


        def skip():
            global i
            i += 1
            root.destroy()

        # buttons
        b1 = tk.Button(root, text='Skip', command=skip)
        b1.place(x=790, y=405)
        b2 = tk.Button(root, text='Go Back', command=go_back)
        b2.place(x=700, y=405)
        b3 = tk.Button(root, text='Save', command=save_values)
        b3.place(x=860, y=405)
        b4 = tk.Button(root, text='Done', command=finish)
        b4.place(x=800, y=445)
        # call event loop
        root.mainloop()
