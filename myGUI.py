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
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.frame1 = tk.Frame(self.master, bg="blue", pady=10)
        self.frame1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.frame2 = tk.Frame(self.master, bg="gray", pady=10, padx=10)
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.frame3 = tk.Frame(self.master, bg="white", pady=10, padx=10)
        self.frame3.grid(row=1, column=1, sticky="nsew")
        self.create_widgets()
        
    def create_widgets(self):
        # Frame 1 - ANIMESENSEI
        # self.frame1 = tk.Frame(self.master, bg="blue", pady=10)
        # self.frame1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        label1 = tk.Label(self.frame1, text="ANIMESENSEI", fg="white", font=("Arial", 24), bg="blue")
        label1.pack()

        # Frame 2 - Home, Statistic, Quit
        # self.frame2 = tk.Frame(self.master, bg="gray", pady=10, padx=10)
        # self.frame2.grid(row=1, column=0, sticky="nsew")
        button1 = tk.Button(self.frame2, text="Home", font=("Arial", 18), padx=20, pady=10)
        button1.pack(fill="x")
        button2 = tk.Button(self.frame2, text="Statistic", font=("Arial", 18), padx=20, pady=10, command=self.show_statistic)
        button2.pack(fill="x")
        button3 = tk.Button(self.frame2, text="Quit", font=("Arial", 18), padx=20, pady=10, command=self.master.destroy)
        button3.pack(fill="x")

        # Frame 3 - Display Graph button and graph
        # self.frame3 = tk.Frame(self.master, bg="white", pady=10, padx=10)
        # self.frame3.grid(row=1, column=1, sticky="nsew")
        display_button1 = tk.Button(self.frame3, text="show anime in release 2012 to 2022 Graph", 
                                    font=("Arial", 18), padx=20, pady=10, command=self.display_graph_show_anime_release_2012_2022)
        display_button1.pack(fill="x")
        display_button2 = tk.Button(self.frame3, text="show boxplot number of episodes for each Release year in 2012 to 2022", 
                                    font=("Arial", 18), padx=20, pady=10, command=self.show_boxplot)
        display_button2.pack(fill="x")
        display_button3 = tk.Button(self.frame3, text="Top 10 Rating for each Tags", font=("Arial", 18), padx=20, pady=10, 
                                    command=self.show_network_graph)
        display_button3.pack(fill="x")
        display_button4 = tk.Button(self.frame3, text="Show correlation between Episodes and Rating", 
                                    font=("Arial", 18), padx=20, pady=10, command=self.show_correlation)
        display_button4.pack(fill="x")
        display_button5 = tk.Button(self.frame3, text="show anime rating in every year release", 
                                    font=("Arial", 18), padx=20, pady=10, command=self.top_level_select_year)
        display_button5.pack(fill="x")
        display_button6 = tk.Button(self.frame3, text="show word cloud", 
                                    font=("Arial", 18), padx=20, pady=10, command=self.show_wordclould_release_season)
        display_button6.pack(fill="x")
        

        self.graph_canvas = tk.Canvas(self.frame3, bg="white", width=600, height=250)
        self.graph_canvas.pack(expand=True, fill="both")
        

        # Set row and column weights
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame3.columnconfigure(0, weight=1)

        
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
        network_graph = data.create_network_graph()

        # clear self.frame3
        for widget in self.self.frame3.winfo_children():
            widget.destroy()

        # display network graph in self.frame3
        FigureCanvasTkAgg(network_graph, master=self.graph_canvas).get_tk_widget().pack(side="top", fill="both", expand=1)
        plt.show()
        # canvas = FigureCanvasTkAgg(network_graph, master=self.self.frame3)
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def show_correlation(self):
        data = MyAnimeData()
        # fig, ax = plt.subplots(figsize=(8, 4))
        text = 'We can see that episodes and rating is independent correlation'
        desc_str = str(text)
        # Create new toplevel window
        top = tk.Toplevel(self.master)
        top.title("Correlation Describe")
        # Create Text widget and insert describe output
        text = tk.Text(top, height=20, width=80)
        text.insert(tk.END, desc_str)
        text.pack()
        data.create_colleration()
        # self.graph_canvas.delete("all")  
        # FigureCanvasTkAgg(fig, master=self.graph_canvas).get_tk_widget().pack(side="top", fill="both", expand=1)
        plt.show()

    def plot_rating_by_year(self, year):
        # Filter the dataframe to only include anime from the selected year
        data = MyAnimeData()
        df_filtered = data.df[data.df['Release_year'] == year]
        # Group the filtered dataframe by rating and count the number of anime in each rating category
        rating_counts = df_filtered.groupby('Rating')['Name'].count()
        # Create a bar chart showing the number of anime in each rating category
        fig, ax = plt.subplots()
        # FigureCanvasTkAgg(fig, master=top).get_tk_widget().pack(side="top", fill="both", expand=1)
        ax.bar(rating_counts.index, rating_counts.values)
        ax.set_title(f'Anime Ratings for {year}')
        ax.set_xlabel('Rating')
        ax.set_ylabel('Number of Anime')
        plt.show()

    def top_level_select_year(self):
        year_window = tk.Toplevel()
        year_window.title('Select Year')

        # Create a label and dropdown menu for year selection
        year_label = tk.Label(year_window, text='Select Year:')
        year_label.pack(side=tk.LEFT)

        self.year_var = tk.StringVar(year_window)
        self.year_var.set('1980')

        year_dropdown = tk.OptionMenu(year_window, self.year_var, *[str(year) for year in range(1980, 2023)])
        year_dropdown.pack(side=tk.LEFT)

        # Create a button to submit the year selection
        submit_button = tk.Button(year_window, text='Submit', command=self.select_year)
        submit_button.pack(side=tk.LEFT)
    # Create a function to handle the user's year selection

    def select_year(self):
        # Get the year selected by the user
        year = int(self.year_var.get())

        # Call the function to plot the rating by year
        self.plot_rating_by_year(year)

    def show_wordclould_release_season(self):
        data = MyAnimeData()
        top = tk.Toplevel(self.master, image=data.wordCloud)
        top.pack()

    def run(self):
        self.mainloop
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
