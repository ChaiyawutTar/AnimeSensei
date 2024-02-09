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



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.title("AnimeSensei")
        self.create_widgets()
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        # self.graph_canvas = None
        
    def create_widgets(self):
        # Frame 1 - ANIMESENSEI
        frame1 = tk.Frame(self.master, bg="blue", pady=10)
        frame1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        label1 = tk.Label(frame1, text="ANIMESENSEI", fg="white", font=("Arial", 24), bg="blue")
        label1.pack()

        # Frame 2 - Home, Statistic, Quit
        frame2 = tk.Frame(self.master, bg="gray", pady=10, padx=10)
        frame2.grid(row=1, column=0, sticky="nsew")
        button1 = tk.Button(frame2, text="Home", font=("Arial", 18), padx=20, pady=10)
        button1.pack(fill="x")
        button2 = tk.Button(frame2, text="Statistic", font=("Arial", 18), padx=20, pady=10, command=self.show_statistic)
        button2.pack(fill="x")
        button3 = tk.Button(frame2, text="Quit", font=("Arial", 18), padx=20, pady=10, command=self.master.destroy)
        button3.pack(fill="x")

        # Frame 3 - Display Graph button and graph
        frame3 = tk.Frame(self.master, bg="white", pady=10, padx=10)
        frame3.grid(row=1, column=1, sticky="nsew")
        display_button1 = tk.Button(frame3, text="show anime in release 2012 to 2022 Graph", font=("Arial", 18), padx=20, pady=10, command=self.display_graph_show_anime_release_2012_2022)
        display_button1.pack(fill="x")
        display_button2 = tk.Button(frame3, text="show boxplot number of episodes for each Release year in 2012 to 2022  ", font=("Arial", 18), padx=20, pady=10, command=self.show_boxplot)
        display_button2.pack(fill="x")
        display_button1 = tk.Button(frame3, text="Top 10 Rating for each Tags", font=("Arial", 18), padx=20, pady=10, command=self.show_network_graph)
        display_button1.pack(fill="x")
        display_button1 = tk.Button(frame3, text="Show correlation between Episodes and Rating", font=("Arial", 18), padx=20, pady=10, command=self.show_correlation)
        display_button1.pack(fill="x")
        self.graph_canvas = tk.Canvas(frame3, bg="white", width=600, height=300)
        self.graph_canvas.pack(expand=True, fill="both")
        

        # Set row and column weights
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(1, weight=1)
        frame1.rowconfigure(0, weight=1)
        frame1.columnconfigure(0, weight=1)
        frame2.rowconfigure(0, weight=1)
        frame2.columnconfigure(0, weight=1)
        frame3.rowconfigure(0, weight=1)
        frame3.columnconfigure(0, weight=1)

        
    # def display_graph(self):
    #     x = np.linspace(-5, 5, 100)
    #     y = np.sin(x)
    #     fig, ax = plt.subplots(figsize=(6, 4))
    #     ax.plot(x, y)
    #     ax.set_title("Sine wave")
    #     ax.set_xlabel("X-axis")
    #     ax.set_ylabel("Y-axis")
    #     self.draw_figure(fig)
    
    def display_graph_show_anime_release_2012_2022(self):
        data = MyAnimeData()
        fig, ax = plt.subplots(figsize=(8, 4))
        data.show_anime_release_2012_2022()
        self.graph_canvas.delete("all")  
        FigureCanvasTkAgg(fig, master=self.graph_canvas).get_tk_widget().pack(side="top", fill="both", expand=1)
        plt.show()
        # print(ax.shape)
        
    def show_statistic(self):
        # Get describe output from MyAnimeData
        data = MyAnimeData()
        desc = data.df.describe()
        desc_str = str(desc)
        # Create new toplevel window
        top = tk.Toplevel(self.master)
        top.title("Data Describe")
        # Create Text widget and insert describe output
        text = tk.Text(top, height=20, width=80)
        text.insert(tk.END, desc_str)
        text.pack()

    def show_boxplot(self):
        # Get boxplot output from MyAnimeData
        data = MyAnimeData()
        fig, ax = plt.subplots(figsize=(8, 4))
        data.show_boxplot_ReleaseYear_2012_2022_Episodes_noout()
        self.graph_canvas.delete("all")  
        FigureCanvasTkAgg(fig, master=self.graph_canvas).get_tk_widget().pack(side="top", fill="both", expand=1)
        plt.show()

    def show_network_graph(self):
        # get network graph
        data = MyAnimeData()
        # fig, ax = plt.subplots(figsize=(8,4))
        # clear frame3
        # for widget in self.frame3.winfo_children():
        #     widget.destroy()
        network_graph = data.create_network_graph()
        # display network graph in frame3
        # FigureCanvasTkAgg(fig , master=self.graph_canvas).get_tk_widget().pack(side="top", fill="both", expand=1)
        plt.show()
        # canvas = FigureCanvasTkAgg(network_graph, master=self.frame3)
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def show_correlation(self):
        data = MyAnimeData()
        # fig, ax = plt.subplots(figsize=(8, 4))
        data.create_colleration()
        # self.graph_canvas.delete("all")  
        # FigureCanvasTkAgg(fig, master=self.graph_canvas).get_tk_widget().pack(side="top", fill="both", expand=1)
        plt.show()
        
    def show_UI(self):
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()
