# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

from Recommender import Recommender
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RecommenderGUI():
    def __init__(self):
        self.__recommender = Recommender()
        self.main_window = tk.Tk()
        self.main_window.title("Media For You")
        self.main_window.geometry("1200x800")

        # Lower button frame
        # Needed to be created before the notebook so that the notebook or it would not be shown
        self.buttonFrame = tk.Frame(self.main_window)
        self.loadShowsButton = tk.Button(self.buttonFrame, text="Load Shows", command=self.loadShows)
        self.loadBooksButton = tk.Button(self.buttonFrame, text="Load Books", command=self.loadBooks)
        self.loadAssociationsButton = tk.Button(self.buttonFrame, text="Load Associations", command=self.loadAssociations)
        self.creditInfoBoxButton = tk.Button(self.buttonFrame, text="Credit Info Box", command=self.creditInfoBox)
        self.quitButton = tk.Button(self.buttonFrame, text="Quit", command=self.main_window.destroy)
        self.loadShowsButton.pack(side=tk.LEFT, expand=1)
        self.loadBooksButton.pack(side=tk.LEFT, expand=1)
        self.loadAssociationsButton.pack(side=tk.LEFT, expand=1)
        self.creditInfoBoxButton.pack(side=tk.LEFT, expand=1)
        self.quitButton.pack(side=tk.LEFT, expand=1)
        self.buttonFrame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create notebook
        self.nb = ttk.Notebook(self.main_window)
        self.nb.pack(expand=1, fill=tk.BOTH)

        # Create movie frame
        self.movies = ttk.Frame(self.nb)
        self.moviesText = tk.Text(self.movies, wrap=tk.WORD)
        self.moviesText.insert("1.0", "Please enter data to view movie data.")
        self.moviesText.configure(state=tk.DISABLED)
        self.moviesStatsText = tk.Text(self.movies, wrap=tk.WORD)
        self.moviesStatsText.insert("1.0", "Please enter data to view movie stats data.")
        self.moviesStatsText.configure(state=tk.DISABLED)
        self.moviesText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.moviesStatsText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.nb.add(self.movies, text="Movies")

        # Create show frame
        self.shows = ttk.Frame(self.nb)
        self.showsText = tk.Text(self.shows, wrap=tk.WORD)
        self.showsText.insert("1.0", "Please enter data to view TV show data.")
        self.showsText.configure(state=tk.DISABLED)
        self.showsStatsText = tk.Text(self.shows, wrap=tk.WORD)
        self.showsStatsText.insert("1.0", "Please enter data to view TV show stats data.")
        self.showsStatsText.configure(state=tk.DISABLED)
        self.showsText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.showsStatsText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.nb.add(self.shows, text="TV Shows")

        # Create book frame
        self.books = ttk.Frame(self.nb)
        self.booksText = tk.Text(self.books, wrap=tk.WORD)
        self.booksText.insert("1.0", "Please enter data to view book data.")
        self.booksText.configure(state=tk.DISABLED)
        self.booksStatsText = tk.Text(self.books, wrap=tk.WORD)
        self.booksStatsText.insert("1.0", "Please enter data to view book stats data.")
        self.booksStatsText.configure(state=tk.DISABLED)
        self.booksText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.booksStatsText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.nb.add(self.books, text="Books")

        # Create search frame
        self.searchMovieShow = ttk.Frame(self.nb)
        self.inputFrame = tk.Frame(self.searchMovieShow)
        self.typeFrame = tk.Frame(self.inputFrame)
        self.typeLabel = tk.Label(self.typeFrame, text="Type: ")
        self.typeCombo = ttk.Combobox(self.typeFrame, values=["Movie", "TV Show"])
        self.typeLabel.pack(side=tk.LEFT)
        self.typeCombo.pack(side=tk.LEFT)
        self.titleFrame = tk.Frame(self.inputFrame)
        self.titleLabel = tk.Label(self.titleFrame, text="Title: ")
        self.titleEntry = tk.Entry(self.titleFrame, width=40)
        self.titleLabel.pack(side=tk.LEFT)
        self.titleEntry.pack(side=tk.LEFT)
        self.directorFrame = tk.Frame(self.inputFrame)
        self.directorLabel = tk.Label(self.directorFrame, text="Director: ")
        self.directorEntry = tk.Entry(self.directorFrame, width=40)
        self.directorLabel.pack(side=tk.LEFT)
        self.directorEntry.pack(side=tk.LEFT)
        self.actorFrame = tk.Frame(self.inputFrame)
        self.actorLabel = tk.Label(self.actorFrame, text="Actor: ")
        self.actorEntry = tk.Entry(self.actorFrame, width=40)
        self.actorLabel.pack(side=tk.LEFT)
        self.actorEntry.pack(side=tk.LEFT)
        self.genreFrame = tk.Frame(self.inputFrame)
        self.genreLabel = tk.Label(self.genreFrame, text="Genre: ")
        self.genreEntry = tk.Entry(self.genreFrame, width=40)
        self.genreLabel.pack(side=tk.LEFT)
        self.genreEntry.pack(side=tk.LEFT)
        self.searchButton = tk.Button(self.inputFrame, text="Search", command=self.searchShows)
        self.searchMoviesShowText = tk.Text(self.searchMovieShow, wrap=tk.WORD)
        self.searchMoviesShowText.insert("1.0", "Please perform a search to see the data.\nMake sure data has been input as well.")
        self.searchMoviesShowText.configure(state=tk.DISABLED)    
        # Pack all the widgets  
        self.typeFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.titleFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.directorFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.actorFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.genreFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.searchButton.pack(side=tk.LEFT)
        self.inputFrame.pack(side=tk.TOP, fill=tk.X)
        self.searchMoviesShowText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.nb.add(self.searchMovieShow, text="Search Movies/TV")

        # Book search frame
        self.searchBook = ttk.Frame(self.nb)
        self.bookInputFrame = tk.Frame(self.searchBook)
        self.bookTitleFrame = tk.Frame(self.bookInputFrame)
        self.bookTitleLabel = tk.Label(self.bookTitleFrame, text="Title: ")
        self.bookTitleEntry = tk.Entry(self.bookTitleFrame, width=40)
        self.bookTitleLabel.pack(side=tk.LEFT)
        self.bookTitleEntry.pack(side=tk.LEFT)
        self.bookAuthorFrame = tk.Frame(self.bookInputFrame)
        self.bookAuthorLabel = tk.Label(self.bookAuthorFrame, text="Author: ")
        self.bookAuthorEntry = tk.Entry(self.bookAuthorFrame, width=40)
        self.bookAuthorLabel.pack(side=tk.LEFT)
        self.bookAuthorEntry.pack(side=tk.LEFT)
        self.bookPublisherFrame = tk.Frame(self.bookInputFrame)
        self.bookPublisherLabel = tk.Label(self.bookPublisherFrame, text="Publisher: ")
        self.bookPublisherEntry = tk.Entry(self.bookPublisherFrame, width=40)
        self.bookPublisherLabel.pack(side=tk.LEFT)
        self.bookPublisherEntry.pack(side=tk.LEFT)
        self.searchBookButton = tk.Button(self.bookInputFrame, text="Search", command=self.searchBooks)
        self.searchBookText = tk.Text(self.searchBook, wrap=tk.WORD)
        self.searchBookText.insert("1.0", "Please perform a search to see the data.\nMake sure data has been input as well.")
        self.searchBookText.configure(state=tk.DISABLED)
        # Pack all the widgets
        self.bookTitleFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.bookAuthorFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.bookPublisherFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.searchBookButton.pack(side=tk.LEFT)
        self.bookInputFrame.pack(side=tk.TOP, fill=tk.X)
        self.searchBookText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.nb.add(self.searchBook, text="Search Books")

        # Recommendations frame
        self.recommendations = ttk.Frame(self.nb)
        self.recommendationsInputFrame = tk.Frame(self.recommendations)
        self.recommendationsTypeFrame = tk.Frame(self.recommendationsInputFrame)
        self.recommendationsTypeLabel = tk.Label(self.recommendationsTypeFrame, text="Type: ")
        self.recommendationsTypeCombo = ttk.Combobox(self.recommendationsTypeFrame, values=["Movie", "TV Show", "Book"])
        self.recommendationsTypeLabel.pack(side=tk.LEFT)
        self.recommendationsTypeCombo.pack(side=tk.LEFT)
        self.recommendationsTitleFrame = tk.Frame(self.recommendationsInputFrame)
        self.recommendationsTitleLabel = tk.Label(self.recommendationsTitleFrame, text="Title: ")
        self.recommendationsTitleEntry = tk.Entry(self.recommendationsTitleFrame, width=40)
        self.recommendationsTitleLabel.pack(side=tk.LEFT)
        self.recommendationsTitleEntry.pack(side=tk.LEFT)
        self.recommendationsButton = tk.Button(self.recommendationsInputFrame, text="Get Recommendations", command=self.getRecommendations)
        self.recommendationsText = tk.Text(self.recommendations, wrap=tk.WORD)
        self.recommendationsText.insert("1.0", "Please perform a search to see the data.\nMake sure data has been input as well.")
        self.recommendationsText.configure(state=tk.DISABLED)
        # Pack all the widgets
        self.recommendationsTypeFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.recommendationsTitleFrame.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.recommendationsInputFrame.pack(side=tk.TOP, fill=tk.X)
        self.recommendationsButton.pack(side=tk.LEFT)
        self.recommendationsText.pack(side=tk.TOP, expand=1, fill=tk.BOTH)        
        self.nb.add(self.recommendations, text="Recommendations")

    def searchShows(self):
        print("searching shows")
    
    def searchBooks(self):
        print("searching shows")

    def getRecommendations(self):
        """
        This function gets the recommendations for the user based on the type of media and title they input. It uses
        the functions from the instance of the Recommender class to get the recommendations and display them in the text box.
        The function is called when the user clicks the "Get Recommendations" button.
        :return: None
        """
        typeMedia = self.recommendationsTypeCombo.get()
        titleMedia = self.recommendationsTitleEntry.get()
        associations = self.__recommender.getRecommendations(typeOfMedia=typeMedia, title=titleMedia)
        self.recommendationsText.configure(state=tk.NORMAL)
        self.recommendationsText.delete("1.0", tk.END)
        self.recommendationsText.insert("1.0", associations)
        self.recommendationsText.configure(state=tk.DISABLED)
    
    def loadShows(self):
        """
        This function loads the TV shows and movies from the CSV files and displays them in the text boxes. It also
        loads the statistics for the TV shows and movies and displays them in the corresponding text boxes. To do this, 
        it uses the functions from the instance of the Recommender class to get the data from the user. The function is called
        when the user clicks the "Load Shows" button.
        :return: None
        """
        self.__recommender.loadShows()
        result = self.__recommender.getTVList()
        self.showsText.configure(state=tk.NORMAL)
        self.showsText.delete("1.0", tk.END)
        self.showsText.insert("1.0", result)
        self.showsText.configure(state=tk.DISABLED)
        statsResult = self.__recommender.getTVStats()
        self.showsStatsText.configure(state=tk.NORMAL)
        self.showsStatsText.delete("1.0", tk.END)
        self.showsStatsText.insert("1.0", statsResult)
        self.showsStatsText.configure(state=tk.DISABLED)
        movieResult = self.__recommender.getMovieList()
        self.moviesText.configure(state=tk.NORMAL)
        self.moviesText.delete("1.0", tk.END)
        self.moviesText.insert("1.0", movieResult)
        self.moviesText.configure(state=tk.DISABLED)
        movieStatsResult = self.__recommender.getMovieStats()
        self.moviesStatsText.configure(state=tk.NORMAL)
        self.moviesStatsText.delete("1.0", tk.END)
        self.moviesStatsText.insert("1.0", movieStatsResult)
        self.moviesStatsText.configure(state=tk.DISABLED)
    
    def loadBooks(self):
        """
        This function loads the books from the user input CSV file and displays them in the text box. The function also
        loads the statistics for the books and displays them in the corresponding text box. To do this, it uses the functions
        getBookList and getBookStats from the instance of the Recommender class.
        :return: None
        """
        self.__recommender.loadBooks()
        result = self.__recommender.getBookList()
        self.booksText.configure(state=tk.NORMAL)
        self.booksText.delete("1.0", tk.END)
        self.booksText.insert("1.0", result)
        self.booksText.configure(state=tk.DISABLED)
        statsResult = self.__recommender.getBookStats()
        self.booksStatsText.configure(state=tk.NORMAL)
        self.booksStatsText.delete("1.0", tk.END)
        self.booksStatsText.insert("1.0", statsResult)
        self.booksStatsText.configure(state=tk.DISABLED)
    
    def loadAssociations(self):
        """
        This function just calls the loadAssociations function from the instance of the Recommender class to load the associations based
        on the user input association file. It does not display anything to the user, and is called when the user clicks the "Load Associations" button.
        :return: None
        """
        self.__recommender.loadAssociations()
    
    def creditInfoBox(self):
        """
        This function displays a messagebox with the credit information for the program when the user clicks the "Credit Info Box" button.
        """
        messagebox.showinfo("Credit Information", "This program was created by Shawn Aviles, Justin Ferber, and Harris Pyo.\nThe project was completed on May 5, 2024.")
    
def main():
    RecommenderGUI()
    tk.mainloop()

main()