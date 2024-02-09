import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

# Load the data from a CSV file into a pandas dataframe
df = pd.read_csv('/Users/tar/Documents/sem 2 final/project sem2 animesensei/Anime-3.csv')

# Create a function to plot the rating by year
def plot_rating_by_year(year):
    # Filter the dataframe to only include anime from the selected year
    df_filtered = df[df['Release_year'] == year]
    
    # Group the filtered dataframe by rating and count the number of anime in each rating category
    rating_counts = df_filtered.groupby('Rating')['Name'].count()
    
    # Create a bar chart showing the number of anime in each rating category
    fig, ax = plt.subplots()
    ax.bar(rating_counts.index, rating_counts.values)
    
    ax.set_title(f'Anime Ratings for {year}')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Number of Anime')
    plt.show()
    

# Create a function to handle the user's year selection
def select_year():
    # Get the year selected by the user
    year = int(year_var.get())
    
    # Call the function to plot the rating by year
    plot_rating_by_year(year)

# Create the tkinter window
root = Tk()
root.title('Anime Rating by Year')

# Create a Toplevel window for year selection
year_window = Toplevel(root)
year_window.title('Select Year')

# Create a label and dropdown menu for year selection
year_label = Label(year_window, text='Select Year:')
year_label.pack(side=LEFT)

year_var = StringVar(year_window)
year_var.set('1980')

year_dropdown = OptionMenu(year_window, year_var, *[str(year) for year in range(1980, 2023)])
year_dropdown.pack(side=LEFT)

# Create a button to submit the year selection
submit_button = Button(year_window, text='Submit', command=select_year)
submit_button.pack(side=LEFT)

# Start the tkinter mainloop
root.mainloop()
