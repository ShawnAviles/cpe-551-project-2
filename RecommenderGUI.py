# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

from Recommender import Recommender
import tkinter as tk
from tkinter import ttk

class RecommenderGUI():
    def __init__(self):
        self.__recommender = Recommender()
        self.main_window = tk.Tk()
        self.main_window.title("Media For You")
        self.nb = ttk.Notebook(self.main_window)
        self.nb.pack(expand=1, fill=tk.BOTH)

        # Create movie frame
        self.movies = ttk.Frame(self.nb)
        self.moviesText = tk.Text(self.movies, wrap=tk.WORD)
        self.moviesText.configure(state=tk.DISABLED)
        self.moviesStatsText = tk.Text(self.movies, wrap=tk.WORD)
        self.moviesStatsText.configure(state=tk.DISABLED)
        self.nb.add(self.movies, text="Movies")

        # Create show frame
        self.shows = ttk.Frame(self.nb)
        self.showsText = tk.Text(self.shows, wrap=tk.WORD)
        self.showsText.configure(state=tk.DISABLED)
        self.showsStatsText = tk.Text(self.shows, wrap=tk.WORD)
        self.showsStatsText.configure(state=tk.DISABLED)
        self.nb.add(self.shows, text="TV Shows")

        # Create book frame
        self.books = ttk.Frame(self.nb)
        self.booksText = tk.Text(self.books, wrap=tk.WORD)
        self.booksText.configure(state=tk.DISABLED)
        self.booksStatsText = tk.Text(self.books, wrap=tk.WORD)
        self.booksStatsText.configure(state=tk.DISABLED)
        self.nb.add(self.books, text="Books")
