from itertools import combinations
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas.plotting import table
import networkx as nx
import spicy as sp
from wordcloud import WordCloud

path = '/Users/tar/Documents/sem 2 final/project sem2 animesensei/Anime-3.csv'
orig_df = pd.read_csv(path)
# orig_df.shape

df = orig_df.copy()
# df = df.dropna()
# print(df_cutcol)
new_df = df
nameAnimeList = df['Name'].tolist()
# print(nameAnimeList)
ratingAnimeList = df['Rating'].tolist()
# print(ratingAnimeList)
# print(df.columns)
# print(df.isnull().sum())
# print(df.mean())
# print(df.median())
# print(df.mode().loc[0,])
# for i in df['Tags']:
#     print(type(i))

# print(df.describe())

#anime release in 2018 rating
df_release2018_rating = df[df['Release_year'] == 2018]['Rating'].dropna()
mean_release2018_rating = df_release2018_rating.mean()
med_release2018_rating = df_release2018_rating.median()
std_release2018_rating = df_release2018_rating.std()
IQR_release2018_rating = df_release2018_rating.quantile(0.75) - df_release2018_rating.quantile(0.25)
# print(df_release2018_rating)
# print(f"mean={mean_release2018_rating}, median={med_release2018_rating}, standard deviation={std_release2018_rating}, IQR={IQR_release2018_rating}")

outlier = df[df['Release_year'] == 2018]['Rating'].dropna()[(df.Rating <= df_release2018_rating.quantile(0.25)-1.5*(IQR_release2018_rating)) & (df.Rating >= df_release2018_rating.quantile(0.75)+1.5*(IQR_release2018_rating))]
higher_f = df_release2018_rating.quantile(0.75)+1.5*(IQR_release2018_rating)
lower_f = df_release2018_rating.quantile(0.25)-1.5*(IQR_release2018_rating)
# print(f"{outlier} and this lower fence={lower_f} , higher fence={higher_f}")

# df.hist()
# plt.show()

#anime release in 2019





#anime release in 2020

#finished 



#show anime release in 2012 - 2022 # timeseries
year_freq = df['Release_year'].dropna().value_counts().sort_index()
# # print(year_freq.to_list()[90:101])
# temp_df = pd.DataFrame(year_freq.to_list()[90:101]) # count anime in 2012 - 2022
# temp_df.rename(columns={0:'Count'}, inplace=True)
# temp_df.set_index(np.arange(2012,2023), inplace=True)
# # print(temp_df)
# line1 = sns.lineplot(data=temp_df, x=temp_df.index, y='Count', color='blue')
# plt.show()

class MyAnimeData:
    def __init__(self) -> None:
        self.path = '/Users/tar/Documents/sem 2 final/project sem2 animesensei/Anime-3.csv'
        self.orig_df = pd.read_csv(path)
        self.df = orig_df.copy()
    
    def show_anime_release_2012_2022(self): # timeseries
        year_freq = self.df['Release_year'].dropna().value_counts().sort_index()
        temp_df = self.df['Release_year'].dropna().value_counts().sort_index()
        temp_df = pd.DataFrame(year_freq.to_list()[90:101]) # count anime in 2012 - 2022
        temp_df.rename(columns={0:'Count'}, inplace=True)
        temp_df.set_index(np.arange(2012,2023), inplace=True)
        line1 = sns.lineplot(data=temp_df, x=temp_df.index, y='Count', color='blue')
        plt.title('Show anime release in 2012 to 2022')
        plt.xlabel('Year Release')
        plt.ylabel('Frequency')
        plt.show()

    def show_boxplot_ReleaseYear_2012_2022_Episodes_noout(self):
        
        first_var = 'End_year'
        selected_var = 'Episodes'
        mean_ = df[selected_var].mean()
        sd_ = df[selected_var].std()
        q1 = df[selected_var].quantile(0.25)
        q3 = df[selected_var].quantile(0.75)
        iqr = q3-q1
        cleaned_df = df[~((df[selected_var] < q1-1.5*iqr) | (df[selected_var] > q3+1.5*iqr))]
        cleaned_df = cleaned_df[~((cleaned_df[selected_var] < mean_-3*sd_) | (cleaned_df[selected_var] > mean_+3*sd_))].sort_index()
        cleaned_df = cleaned_df.loc[(cleaned_df['Release_year'] >= 2011) & (cleaned_df['Release_year'] <= 2022)]
        sns.boxplot(x=first_var, y=selected_var,  data=cleaned_df)
        plt.show()
    
    def save_statistic(self):
        desc = self.df.describe()
        plot = plt.subplot(111, frame_on=False)

        #remove axis
        plot.xaxis.set_visible(False) 
        plot.yaxis.set_visible(False) 
        table(plot, desc,loc='upper right')
        plt.savefig('/Users/tar/Documents/sem 2 final/project sem2 animesensei/desc_table.png')

    def create_colleration(self):
        # show colleration between rating and episode with clean data frame with outlier
        first_var = 'End_year'
        selected_var = 'Episodes'
        mean_ = df[selected_var].mean()
        sd_ = df[selected_var].std()
        q1 = df[selected_var].quantile(0.25)
        q3 = df[selected_var].quantile(0.75)
        iqr = q3-q1
        cleaned_df = df[~((df[selected_var] < q1-1.5*iqr) | (df[selected_var] > q3+1.5*iqr))]
        cleaned_df = cleaned_df[~((cleaned_df[selected_var] < mean_-3*sd_) | (cleaned_df[selected_var] > mean_+3*sd_))].sort_index()
        cleaned_df = cleaned_df.loc[(cleaned_df['Release_year'] >= 2012) & (cleaned_df['Release_year'] <= 2022)]
        # sns.pairplot(cleaned_df)
        sns.relplot(data=cleaned_df,
            x=first_var, 
            y=selected_var,
            color=(102/255,205/255,170/255))
        # sns.heatmap(cleaned_df.corr(),
        #     square=True,
        #     linewidths=0.25,    
        #     linecolor=(0,0,0),
        #     cmap=sns.color_palette("coolwarm"),
        #     annot=True)
        plt.show()

    def network(self):
        self.df['clean_tags'] = self.df['Tags'].str.replace(', ', '').str.replace('.', '').str.strip()

        # Get unique tags
        unique_tags = set()
        for tags in self.df['clean_tags']:
            if isinstance(tags, str):
                unique_tags.update(tag.strip() for tag in tags.split(','))

        # Create network graph
        G = nx.Graph()
        G.add_nodes_from(unique_tags)

        # Add edges
        for tags in self.df['clean_tags']:
            if isinstance(tags, str):
                tags_list = [tag.strip() for tag in tags.split(',')]
                for tag1, tag2 in combinations(tags_list, 2):
                    if not G.has_edge(tag1, tag2):
                        G.add_edge(tag1, tag2, weight=1)
                    else:
                        G[tag1][tag2]['weight'] += 1

        # Draw graph
        pos = nx.spring_layout(G, k=0.5, seed=42)
        node_size = [G.degree(n) * 100 for n in G.nodes()]
        edge_width = [d['weight'] / 5 for (u, v, d) in G.edges(data=True)]
        nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color='lightblue')
        nx.draw_networkx_edges(G, pos, width=edge_width, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        plt.axis('off')
        plt.show()
    def create_network_graph(self):
        # Create a new dataframe with only the relevant columns
        tags_cols = ['Tags']
        rating_cols = ['Rating']
        df_tags = self.df[tags_cols + rating_cols]

        # Remove duplicates
        df_tags = df_tags.drop_duplicates()

        # Split the tags by "," and remove any extra spaces
        df_tags['Tags'] = df_tags['Tags'].str.split(",")
        df_tags['Tags'] = df_tags['Tags'].apply(lambda x: [i.strip() for i in x])

        # Create a dictionary to hold the number of anime with each tag
        tags_dict = {}
        for index, row in df_tags.iterrows():
            tags = row['Tags']
            for tag in tags:
                if tag not in tags_dict:
                    tags_dict[tag] = 0
                tags_dict[tag] += 1

        # Create a list of the top 6 tags
        top_tags = sorted(tags_dict.items(), key=lambda x: x[1], reverse=True)[:6]
        top_tags = [tag[0] for tag in top_tags]

        # Create a new dataframe with only the anime that have at least one of the top tags
        df_top_tags = df_tags[df_tags['Tags'].apply(lambda x: bool(set(x).intersection(top_tags)))]

        # Create a new dataframe with only the top 10 anime measured by rating
        df_top_10 = self.df.sort_values('Rating', ascending=False).head(10)

        # Create the network graph
        G = nx.Graph()
        for index, row in df_top_tags.iterrows():
            tags = row['Tags']
            rating = row['Rating']
            for tag in tags:
                if tag in top_tags:
                    G.add_node(tag)
                    G.nodes[tag]['count'] = tags_dict[tag]
                    if G.has_edge(tag, rating):
                        G[tag][rating]['weight'] += 1
                    else:
                        G.add_edge(tag, rating, weight=1)

        # Set the positions of the nodes in the graph
        pos = nx.spring_layout(G)

        # Draw the nodes and edges of the graph
        nx.draw_networkx_nodes(G, pos, node_size=[d['count']*20 for (n, d) in G.nodes(data=True)])
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)

        # Show the graph
        plt.show()

    def show_top_10_anime_by_rating(self):
        top_10 = self.df.nlargest(10, 'Rating')[['Title', 'Rating']]
        print(top_10)

    def create_network_graph(self):
        df_tags = self.df[['Tags', 'Rating', 'Japanese_name']].dropna()
        df_tags['Tags'] = df_tags['Tags'].str.split(',')
        df_tags['Tags'] = df_tags['Tags'].apply(lambda x: [i.strip() for i in x])
        df_tags = df_tags.explode('Tags')
        df_tags = df_tags[df_tags['Tags'].isin(['Drama', 'Fantasy', 'Romance', 'Action', 'Adventure', 'Shounen'])]
        df_top10 = df_tags.sort_values('Rating', ascending=False).groupby('Tags').head(10)
        G = nx.Graph()
        G.add_nodes_from(df_tags['Tags'].unique())
        for tag in df_tags['Tags'].unique():
            G.nodes[tag]['count'] = len(df_tags[df_tags['Tags'] == tag])
        for _, row in df_top10.iterrows():
            G.add_node(row.name, Japanese_name=row['Japanese_name'])
            G.add_edge(row['Tags'], row.name, weight=row['Rating'])
        
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, k=0.8)
        nx.draw(G, pos, with_labels=True, font_size=10, font_weight='bold', node_color='lightblue', alpha=0.8, 
                node_size=[d.get('count', 0)*50 for (n, d) in G.nodes(data=True)])
        
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, font_color='black')
        
        nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'Japanese_name'), font_size=8, font_color='black')
        # nx.draw_networkx_labels(G, pos, labels={node: G.nodes[node]['Japanese_name'] for node in G.nodes()}, font_size=8)
        plt.axis('off')
        plt.title('Network Graph of Top 10 Rated Anime by Tags', fontsize=14)
        plt.show()
    
    def wordCloud(self):
        tags = ' '.join(df['Release_season'])

        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(tags)
        image = wordcloud.to_image()
        image_tk = ttk.ImageTk.PhotoImage(image)
        return image_tk
        # Plot the WordCloud
        # plt.figure(figsize=(10, 5))
        # plt.imshow(wordcloud, interpolation='bilinear')
        # plt.axis('off')
        # plt.title('Anime Tags Word Cloud')
        # plt.show()



if __name__ == "__main__":
    data = MyAnimeData()
    # data.show_anime_release_2012_2022()
    # print(data.show_statistic())
    # data.save_statistic()
    # data.show_boxplot_ReleaseYear_2012_2022_Episodes()
    # data.network()
    # print(data.df['Tags'])
    # data.create_network_graph()
    # data.show_top_10_anime_by_rating()
    # data.create_colleration()
    print(data.df.columns)
    # print(data.df.shape)
    