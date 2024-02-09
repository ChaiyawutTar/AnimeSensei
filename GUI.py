import matplotlib
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from tkinter import NW, ttk
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from AnimeDatabase import MyAnimeData



class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__()
        #frame and init window and picture
        self.master.geometry('800x600')
        self.master.title('Anime Sensei')

        self.home = ImageTk.PhotoImage(Image.open('/Users/tar/Documents/sem 2 final/project sem2 animesensei/home.png').resize((40,40),Image.ANTIALIAS))
        self.graph_pic = ImageTk.PhotoImage(Image.open('/Users/tar/Documents/sem 2 final/project sem2 animesensei/graph.jpg').resize((40,40),Image.ANTIALIAS))
        self.settings = ImageTk.PhotoImage(Image.open('/Users/tar/Documents/sem 2 final/project sem2 animesensei/setting.png').resize((40,40),Image.ANTIALIAS))
        self.quit_pic = ImageTk.PhotoImage(Image.open('/Users/tar/Documents/sem 2 final/project sem2 animesensei/quit.png').resize((40,40),Image.ANTIALIAS))

        # self.animebg = ImageTk.PhotoImage(Image.open('/Users/tar/Documents/sem 2 final/project sem2 animesensei/bganimetop.png').resize((40,40),Image.ANTIALIAS))
        # self.animebg = tk.PhotoImage(file='/Users/tar/Documents/sem 2 final/project sem2 animesensei/bganimetop.png')
        self.update()
        self.frame1 = tk.Frame(self, bg='white', width=50, height=self.winfo_height())
        # self.frame.grid(rowspan=2, row=0,column=0, pady=10, sticky="NSEW")
        # self.frame.pack(side='left')

        self.frame2 = tk.Frame(self, bg='green', width=self.winfo_width(), height=100)
        # self.frame2.pack(side='top')
        # self.frame2.pack_propagate(0)
        self.frame2.grid(row=0, column=5, pady=10, sticky="NSEW", columnspan=4)
        self.frame3 = tk.Frame(self, bg='deep sky blue', width=self.winfo_width()-10, height=self.winfo_height()-100)
        # self.frame3.pack(side='top')
        # self.frame3.pack_propagate(0)
        self.frame1.grid(row=0, column=2, pady=10, sticky="NSEW")
        

        # self.create_widgets()
        
        #canvas

        # self.canvas1 = tk.Canvas(self, width=self.winfo_width(), height=100)
        # self.canvas1.pack(side='right')
        # self.canvas1.create_image(20, 20, anchor=NW, image=self.animebg)

        
        # self.frame2 = tk.LabelFrame
        # self.create_widgets()


        # label
        self.label_title = tk.Label(self.frame2, text='ANIME SENSEI', font=("Arial",30), padx=10, pady=100, bg='green')
        self.label_title.grid(row=0, column=0)
        # self.label_title.pack()
        # self.frame3 = tk.Frame(self, bg='white', width=500, height=1000)
        # self.frame3.grid(row=1, column=1)

        #button
        self.home_btn = tk.Button(self.frame1, image=self.home, bg='white', relief='flat', borderwidth=0)
        self.home_btn.grid(row=0,column=0, pady=50)
        self.graph_btn = tk.Button(self.frame1 , image=self.graph_pic, bg='white', relief='flat', borderwidth=0)
        self.graph_btn.grid(row=1,column=0, pady=50)
        self.setting_btn= tk.Button(self.frame1, image=self.settings, bg='white', relief='flat', borderwidth=0)
        self.setting_btn.grid(row=2,column=0, pady=50)
        self.quit_btn = tk.Button(self.frame1, image=self.quit_pic, bg='white', relief='flat', borderwidth=0)
        self.quit_btn.grid(row=3, column=0, pady=50)


        self.show_stat_btn = ttk.Button(self.frame3, text='SHOW MY DESCRIPTIVE STATS')
        self.show_stat_btn.pack(fill='both')


        #setting frame
        self.min_w = 50 # Min width of the frame
        self.max_w = 200 # Max width of the frame
        self.cur_width = self.min_w # Increasing width of the frame
        self.expanded = False # Check if it is completely expanded

        self.frame1.bind('<Enter>', lambda event: self.expand_frame1())
        self.frame1.bind('<Leave>', lambda event: self.contract_frame1())


        self.frame1.grid_propagate(False)

    # def create_widgets(self):
    # # creating a row with combobox widgets for filters
    #     self.frame_dist = ttk.LabelFrame(self.frame3, text="Select Distribution")
    #     self.frame_dist.grid(row=1, column=0, sticky="NEWS")

    #     self.cb_dist = ttk.Combobox(self.frame_dist, state="readonly")
    #     self.cb_dist['values'] = (
    #         'Normal',
    #         'Exponential',
    #         'Uniform',
    #         'Poisson',
    #         'Binomial',
    #         'Geometric'
    #     )
    #     self.cb_dist.bind('<<ComboboxSelected>>', self.update_dist)
    #     self.cb_dist.grid(row=0, column=0, padx=10, pady=10)


    #     self.btn_quit = ttk.Button(self, text="Quit", command=self.destroy)
    #     self.btn_quit.grid(row=2, column=0, pady=10)
    #     self.btn_quit = ttk.Button(self, text="Quit", command=self.destroy)


    #     ## create Matplotlib figure and plotting axes
    #     self.fig_hist = Figure()
    #     self.ax_hist = self.fig_hist.add_subplot()


    #     # create a canvas to host the figure and place it into the main window
    #     self.fig_canvas = FigureCanvasTkAgg(self.fig_hist, master=self)
    #     self.fig_canvas.get_tk_widget().grid(row=0, column=0,
    #                                         sticky="news", padx=10, pady=10)
        
    # def update_dist(self, ev):
    #     dist = self.cb_dist.get()
    #     if dist == 'Normal':
    #         self.data = np.random.normal(size=10000)
    #     elif dist == 'Exponential':
    #         self.data = np.random.exponential(size=10000)
    #     elif dist == 'Uniform':
    #         self.data = np.random.uniform(size=10000)
    #     elif dist == "Poisson":
    #         self.data = np.random.poisson(size=10000)
    #     # elif dist == "Binomial":
    #     #     self.data = np.random.binomial(size=10000)
    #     # elif dist == "Geometric":
    #     #     self.data = np.random.geometric(size=10000)
    #     self.update_plot()



    def expand_frame1(self):
        self.cur_width += 10 # Increase the width by 10
        repeat = self.after(10, self.expand_frame1) # Repeat this func every 5 ms
        self.frame1.config(width=self.cur_width) # Change the width to new increase width
        if self.cur_width >= self.max_w: # If width is greater than maximum width 
            self.expanded = True # Frame is expended
            self.after_cancel(repeat) # Stop repeating the func
            self.configture_text_of_frame1()

    def contract_frame1(self):
        self.cur_width -= 10 #Decrease the width by 10
        repeat =  self.after(10, self.contract_frame1)
        self.frame1.config(width=self.cur_width)
        if self.cur_width <= self.min_w: # If it is back to normal width
            self.expanded = False # Frame is not expanded
            self.after_cancel(repeat) 
            self.configture_text_of_frame1()

    def configture_text_of_frame1(self):
        if self.expanded: # If the frame is exanded
            self.home_btn.config(text='Home', image='', font=(0,21))
            self.setting_btn.config(text='Settings', image='', font=(0,21))
            self.quit_btn.config(text='Quit', image='', font=(0,21))
            self.graph_btn.config(text='Graph', image='', font=(0,21))
        else:
            # Bring the image back
            self.home_btn.config(image=self.home, font=(0,21))
            self.setting_btn.config(image=self.settings, font=(0,21))
            self.quit_btn.config(image=self.quit_pic, font=(0,21))
            self.graph_btn.config(image=self.graph_pic, font=(0,21))

    def show_graph_command(self):
        myAnimeData = MyAnimeData()
        fig1 = myAnimeData.show_anime_release_2012_2022()
        plot1 = FigureCanvasTkAgg(fig1, self)
        plot1.get_tk_widget().grid(row=1,column=1,padx=30)

    def show_graph(self):
        pass
    def run(self):
        self.mainloop()


# class Sidebar(tk.Frame):
#     pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.pack(fill='both', expand=True, side='bottom')
    root.mainloop()
    