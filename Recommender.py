# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: This file contains the Recommender class, which contains functions to load data from csv files, calculate statistics on shows/movies and books,
# search for shows/movies and books, and get recommendations based on associations between books and shows/movies. 

from Book import Book
from Show import Show
from tkinter import filedialog
import os
from tkinter import messagebox
import numpy as np
from matplotlib.figure import Figure

class Recommender:
  def __init__(self):
    """
    Constructor for Recommender class
    :return: Instance of Recommender class
    :return type: Recommender
    """
    self.__bookDict = {}
    self.__showDict = {}
    self.__associations = {}
  
  def loadBooks(self):
    """
    This function creates a file dialog with tkinter to allow the user to upload a csv file for data on books and stores the data in a book dictionary
    :return: None
    """
    #Prompt the user for the file and keep prompting if the file is not valid/doesn't exist
    file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    file = open(file, "r")

    #Iterate through the file and create a new book object for each line and add it to the book dicitonary
    current = 0
    for line in file:
      if (current != 0):
        formattedLine = line.strip().split(",")
        newBook = Book(formattedLine[0], formattedLine[1], float(formattedLine[3]), formattedLine[2], formattedLine[4], formattedLine[5], formattedLine[6], int(formattedLine[7]), int(formattedLine[8]), formattedLine[9], formattedLine[10])
        if (formattedLine[0] not in self.__bookDict):
          self.__bookDict[formattedLine[0]] = newBook
      else:
        current += 1
    file.close()
  
  def loadShows(self):
    """
    This function creates a file dialog with tkinter to allow the user to upload a csv file for data on shows/movies and stores the data in a show dictionary
    :return: None
    """
    #Prompt the user for the file and keep prompting if the file is not valid/doesn't exist
    file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    file = open(file, "r")

    #Iterate through the file and create a new show object for each line and add it to the book dicitonary
    current = 0
    for line in file:
      if (current != 0):
        formattedLine = line.strip().split(",")
        newShow = Show(formattedLine[0], formattedLine[2], float(formattedLine[5]), formattedLine[1], formattedLine[3], formattedLine[4], formattedLine[6], formattedLine[7], int(formattedLine[8]), formattedLine[9], formattedLine[10], formattedLine[11], formattedLine[12])
        if (formattedLine[0] not in self.__showDict):
          self.__showDict[formattedLine[0]] = newShow
      else:
        current += 1
    file.close()

  def loadAssociations(self):
    """
    This function creates a file dialog with dkinter to allow the user to upload a csv file for data on associations between books and shows/movies and stores the data in an association dictionary
    :return: None
    """
    #Prompt the user for the file and keep prompting if the file is not valid/doesn't exist
    file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    file = open(file, "r")

    #Iterate through the file twice and to create an association both ways and add it to the dictionary
    for line in file:
      formattedLine = line.strip().split(",")
      if (formattedLine[0] not in self.__associations):
        self.__associations[formattedLine[0]] = {formattedLine[1]: 1}
      elif (formattedLine[1] not in self.__associations[formattedLine[0]]):
        self.__associations[formattedLine[0]][formattedLine[1]] = 1
      else:
        self.__associations[formattedLine[0]][formattedLine[1]] += 1
    for line in file:
      formattedLine = line.strip().split(",")
      if (formattedLine[1] not in self.__associations):
        self.__associations[formattedLine[1]] = {formattedLine[0]: 1}
      elif (formattedLine[0] not in self.__associations[formattedLine[1]]):
        self.__associations[formattedLine[1]][formattedLine[0]] = 1
      else:
        self.__associations[formattedLine[1]][formattedLine[0]] += 1
    file.close()

  def getMovieList(self):
    """
    This function creates a formatted string with a column for movie titles and a column for the matching movie runtimes using the dictionary and iterating over it to obtain the
    largest length string for each column to properly format it
    :return: A formatted string with a column for movie titles and a column for movie runtimes
    :return type: string
    """
    formattedString = ""
    largestTitle = 0
    largestRuntime = 0
    #Find the longest string of movie titles and movie runtimes to get length for each column
    for movie in self.__showDict:
      if (self.__showDict[movie].getShowType() == "Movie"):
        if (len(self.__showDict[movie].getTitle()) > largestTitle):
          largestTitle = len(self.__showDict[movie].getTitle())
        if (len(self.__showDict[movie].getDuration()) > largestRuntime):
          largestRuntime = len(self.__showDict[movie].getDuration())

    #Print the columns of movie titles with their runtimes 
    formattedString += format("Title", str(largestTitle + 2)) + format("Runtime", str(largestRuntime)) + "\n"
    for movie in self.__showDict:
      if (self.__showDict[movie].getShowType() == "Movie"):
        formattedString += format(self.__showDict[movie].getTitle(), str(largestTitle + 2)) + format(self.__showDict[movie].getDuration(), str(largestRuntime)) + "\n"
    return formattedString
  
  def getTVList(self):
    """
    This function creates a formatted string with a column for show titles and a column for the matching number of seasons for the show using the dictionary and iterating over it to obtain the 
    largest length string for each column to properly format it
    :return: A formatted string with a column for show titles and a column for number of seasons
    :return type: string
    """
    formattedString = ""
    largestTitle = 0
    largestSeason = 0
    #Find the longest string of show titles and show seasons to get length for each column
    for show in self.__showDict:
      if (self.__showDict[show].getShowType() == "TV Show"):
        if (len(self.__showDict[show].getTitle()) > largestTitle):
          largestTitle = len(self.__showDict[show].getTitle())
        if (len(self.__showDict[show].getDuration()) > largestSeason):
          largestSeason = len(self.__showDict[show].getDuration())
    
    #Print the columns of show titles with their number of seasons 
    formattedString += format("Title", str(largestTitle + 2)) + format("Seasons", str(largestSeason)) + "\n"
    for show in self.__showDict:
      if (self.__showDict[show].getShowType() == "TV Show"):
        formattedString += format(self.__showDict[show].getTitle(), str(largestTitle + 2)) + format(self.__showDict[show].getDuration(), str(largestSeason)) + "\n"
    return formattedString
  
  def getBookList(self):
    """
    This function creates a formatted string with a column for book titles and a column for the matching authors of the book using the dictionary and iterating over it to obtain the 
    largest length string for each column to properly format it
    :return: A formatted string with a column for book titles and a column for the authors of the book
    :return type: string
    """
    formattedString = ""
    largestTitle = 0
    largestAuthor = 0
    #Find the longest string of book titles and book authors to get length for each column
    for book in self.__bookDict:
      if (len(self.__bookDict[book].getTitle()) > largestTitle):
        largestTitle = len(self.__bookDict[book].getTitle())
      if (len(self.__bookDict[book].getAuthors()) > largestAuthor):
        largestAuthor = len(self.__bookDict[book].getAuthors())
    
    #Print the columns of book titles with their authors
    formattedString += format("Title", str(largestTitle + 2)) + format("Author(s)", str(largestAuthor)) + "\n"
    for book in self.__bookDict:
      formattedString += format(self.__bookDict[book].getTitle(), str(largestTitle + 2)) + format(self.__bookDict[book].getAuthors(), str(largestAuthor)) + "\n"
    return formattedString
  
  def getMovieStats(self):
    """
    This function iterates over the show dictionary while only looking at the movies to obtain the rating percentages, average movie duration, most prolific director, most prolific actor, and most frequent genre.
    This is done by keeping track of desired data with dictionary and looping in order to create a formatted string with the data.
    :return: A formatted string with the rating percentages, average movie duration, most prolific director, most prolific actor, and most frequent genre
    :return type: string
    """
    ratings = {}
    directors = {}
    directorMax = 0
    bestDirector = ""
    actors = {}
    actorMax = 0
    bestActor = ""
    genres = {}
    genreMax = 0
    bestGenre = ""
    count = 0
    total = 0
    formattedString = "Ratings:\n"

    #Iterate through the movies to get the count for each rating, director, actor, and genre. Store it in dictionaries to determine ones with highest count
    for movie in self.__showDict:
      if (self.__showDict[movie].getShowType() == "Movie"):
        #Rating Part
        if (self.__showDict[movie].getRating() not in ratings):
          if ((self.__showDict[movie].getRating() == "") and ("None" not in ratings)):
            ratings["None"] = 1
          elif ((self.__showDict[movie].getRating() == "") and ("None" in ratings)):
            ratings["None"] += 1
          else:
            ratings[self.__showDict[movie].getRating()] = 1
        else:
            ratings[self.__showDict[movie].getRating()] += 1

        #Duration Part
        total += int(self.__showDict[movie].getDuration().split(" ")[0])

        #Director Part
        if ((self.__showDict[movie].getDirector() not in directors) and (self.__showDict[movie].getDirector() != "")):
          directors[self.__showDict[movie].getDirector()] = 1
          if (directors[self.__showDict[movie].getDirector()] > directorMax):
              directorMax = directors[self.__showDict[movie].getDirector()]
              bestDirector = self.__showDict[movie].getDirector()
        else:
          if (self.__showDict[movie].getDirector() != ""):
            directors[self.__showDict[movie].getDirector()] += 1
            if (directors[self.__showDict[movie].getDirector()] > directorMax):
              directorMax = directors[self.__showDict[movie].getDirector()]
              bestDirector = self.__showDict[movie].getDirector()
        
        #Actor Part
        actorList = self.__showDict[movie].getActors().split("\\")
        for actor in actorList:
          if ((actor not in actors) and (actor != "")):
            actors[actor] = 1
            if (actors[actor] > actorMax):
                actorMax = actors[actor]
                bestActor = actor
          else:
            if (actor != ""):
              actors[actor] += 1
              if (actors[actor] > actorMax):
                actorMax = actors[actor]
                bestActor = actor
        
        #Genre Part
        genreList = self.__showDict[movie].getGenres().split("\\")
        for genre in genreList:
          if ((genre not in genres) and (genre != "")):
            genres[genre] = 1
            if (genres[genre] > genreMax):
                genreMax = genres[genre]
                bestGenre = genre
          else:
            if (genre != ""):
              genres[genre] += 1
              if (genres[genre] > genreMax):
                genreMax = genres[genre]
                bestGenre = genre
        count += 1

    #Add all the stats to the formatted string
    for rating in ratings:
      formattedString += rating + " " + str(format(ratings[rating]/count * 100, ".2f")) + "%" + "\n"
    formattedString += "\nAverage Movie Duration: " + str(format(total/count, ".2f")) + " minutes\n\n"
    formattedString += "Most Prolific Director: " + bestDirector + "\n\n"
    formattedString += "Most Prolific Actor: " + bestActor + "\n\n"
    formattedString += "Most Frequent Genre: " + bestGenre
    return formattedString
  
  def getTVStats(self):
    """
    This function iterates over the show dictionary while only looking at the tv shows to obtain the rating percentages, average number of seasons, most prolific actor, and most frequent genre.
    This is done by keeping track of desired data with dictionary and looping in order to create a formatted string with the data.
    :return: A formatted string with the rating percentages, average number of seasons, most prolific actor, and most frequent genre
    :return type: string
    """
    ratings = {}
    actors = {}
    actorMax = 0
    bestActor = ""
    genres = {}
    genreMax = 0
    bestGenre = ""
    total = 0
    count = 0
    formattedString = "Ratings:\n"

    #Iterate through the show to get the count for each rating, seasons, actor, and genre. Store it in dictionaries to determine ones with highest count
    for show in self.__showDict:
      if (self.__showDict[show].getShowType() == "TV Show"):
        #Rating Part
        if (self.__showDict[show].getRating() not in ratings):
          if ((self.__showDict[show].getRating() == "") and ("None" not in ratings)):
            ratings["None"] = 1
          elif ((self.__showDict[show].getRating() == "") and ("None" in ratings)):
            ratings["None"] += 1
          else:
            ratings[self.__showDict[show].getRating()] = 1
        else:
            ratings[self.__showDict[show].getRating()] += 1
        
        #Season Part
        total += int(self.__showDict[show].getDuration().split(" ")[0])

        #Actor Part
        actorList = self.__showDict[show].getActors().split("\\")
        for actor in actorList:
          if ((actor not in actors) and (actor != "")):
            actors[actor] = 1
            if (actors[actor] > actorMax):
                actorMax = actors[actor]
                bestActor = actor
          else:
            if (actor != ""):
              actors[actor] += 1
              if (actors[actor] > actorMax):
                actorMax = actors[actor]
                bestActor = actor
        
        #Genre Part
        genreList = self.__showDict[show].getGenres().split("\\")
        for genre in genreList:
          if ((genre not in genres) and (genre != "")):
            genres[genre] = 1
            if (genres[genre] > genreMax):
                genreMax = genres[genre]
                bestGenre = genre
          else:
            if (genre != ""):
              genres[genre] += 1
              if (genres[genre] > genreMax):
                genreMax = genres[genre]
                bestGenre = genre
        count += 1

    #Add all the stats to the formatted string
    for rating in ratings:
      formattedString += rating + " " + str(format(ratings[rating]/count * 100, ".2f")) + "%" + "\n"
    formattedString += "\nAverage Number of Seasons: " + str(format(total/count, ".2f")) + " seasons\n\n"
    formattedString += "Most Prolific Actor: " + bestActor + "\n\n"
    formattedString += "Most Frequent Genre: " + bestGenre
    return formattedString

  def getBookStats(self):
    """
    This function iterates over the book dictionary to obtain the average page count, the most prolific author, and the most prolific publisher.
    This is done by keeping track of desired data with dictionary and looping in order to create a formatted string with the data.
    :return: A formatted string with the average page count, the most prolific author, and the most prolific publisher
    :return type: string
    """
    total = 0
    count = 0
    authors = {}
    authorMax = 0
    bestAuthor = ""
    publishers = {}
    publisherMax = 0
    bestPublisher = ""
    formattedString = ""
    #Iterate through the movies to get the count for each page, author, and publisher. Store it in dictionaries to determine ones with highest count
    for book in self.__bookDict:
      #Page Part
      total += int(self.__bookDict[book].getPages())

      #Author Part
      authorList = self.__bookDict[book].getAuthors().split("\\")
      for author in authorList:
        if ((author not in authors) and (author != "")):
          authors[author] = 1
          if (authors[author] > authorMax):
              authorMax = authors[author]
              bestAuthor = author
        else:
          if (author != ""):
            authors[author] += 1
            if (authors[author] > authorMax):
              authorMax = authors[author]
              bestAuthor = author
      
      #Publisher Part
      if (self.__bookDict[book].getPublisher() not in publishers):
        publishers[self.__bookDict[book].getPublisher()] = 1
        if (publishers[self.__bookDict[book].getPublisher()] > publisherMax):
          publisherMax = publishers[self.__bookDict[book].getPublisher()]
          bestPublisher = self.__bookDict[book].getPublisher()
      else:
        if (self.__bookDict[book].getPublisher() != ""):
          publishers[self.__bookDict[book].getPublisher()] += 1
          if (publishers[self.__bookDict[book].getPublisher()] > publisherMax):
            publisherMax = publishers[self.__bookDict[book].getPublisher()]
            bestPublisher = self.__bookDict[book].getPublisher()
      count += 1

    #Add all the stats to the formatted string
    formattedString += "Average Page Count: " + str(format(total/count, ".2f")) + " pages\n\n"
    formattedString += "Most Prolific Author: " + bestAuthor + "\n\n"
    formattedString += "Most Prolific Publisher: " + bestPublisher
    return formattedString
  
  def searchTVMovies(self, typeOfMedia, title, director, actor, genre):
    """
    This function takes in a type of media, a title, a director, an actor, and a genre and returns a formatted string with all the 
    shows/movies that match the criteria
    :param typeOfMedia: The type of media, either "Movie" or "TV Show"
    :param typeOfMedia type: string
    :param title: The title of the media
    :param title type: string
    :param director: The director of the media
    :param director type: string
    :param actor: The actor in the media
    :param actor type: string
    :param genre: The genre of the media
    :param genre type: string
    :return: A formatted string with all the shows/movies that match the criteria
    :return type: string
    """
    # If no parameters are given, return an error message
    if typeOfMedia != "Movie" and typeOfMedia != "TV Show":
      messagebox.showerror("Error", "Must select Movie or TV Show")
      return "No Results"
    
    if title == "" and director == "" and actor == "" and genre == "":
      messagebox.showerror("Error", "Must enter information for at least one: Title, Director, Actor, and/or Genre")
      return "No Results"
    
    # search through the show dictionary and select all objects that adhere to the user's data
    results = []
    for show in self.__showDict.values():
      # only check for value match if the search parameter exists (not empty)
      if (show.getShowType() == typeOfMedia and
        (title.lower() in show.getTitle().lower() if title else True) and
        (director.lower() in show.getDirector().lower() if director else True) and
        (actor.lower() in show.getActors().lower() if actor else True) and
        (genre.lower() in show.getGenres().lower() if genre else True)):
        results.append(show)
    
    if len(results) == 0:
      return "No Results Found"

    # determine longest strings for proper column width (adding 2 for padding)
    longest_title = max(len(show.getTitle()) for show in results) + 2
    longest_director = max(len(show.getDirector()) for show in results) + 2
    if (longest_director == 2):
        longest_director = 10
    longest_actor = max(len(show.getActors()) for show in results) + 2
    longest_genre = max(len(show.getGenres()) for show in results) + 2
    
    # format the results into a string, header at the top
    formatted_result = f"{'Title':<{longest_title}}{'Director':<{longest_director}}{'Actors':<{longest_actor}}{'Genre':<{longest_genre}}\n"
    for show in results:
      formatted_result += f"{show.getTitle():<{longest_title}}{show.getDirector():<{longest_director}}{show.getActors():<{longest_actor}}{show.getGenres():<{longest_genre}}\n"
    
    return formatted_result
  
  def searchBooks(self, title, author, publisher):
    # If no parameters are given, return an error message
    if title == "" and author== "" and publisher == "":
      messagebox.showerror("Error", "Please enter information for at least one: Title, Author, and/or Publisher.")
      return "No Results"
    
    # Search through the book dictionary and select all objects that adhere to the user's data
    results = []
    for book in self.__bookDict.values():
      # only check for value match if the search parameter exists
      if ((title.lower() in book.getTitle().lower() if title else True) and
          (author.lower() in book.getAuthors().lower() if author else True) and
          (publisher.lower() in book.getPublisher().lower() if publisher else True)):
          results.append(book)
    
    if len(results) == 0:
      return "No Results Found"
    
    # determine longest strings for proper column width (adding 3 for padding)
    longest_title = max(len(book.getTitle()) for book in results) + 3
    longest_author = max(len(book.getAuthors()) for book in results) + 3
    longest_publisher = max(len(book.getPublisher()) for book in results) + 3
    
    # format the results into a string, header at the top
    formatted_result = f"{'Title':<{longest_title}}{'Author(s)':<{longest_author}}{'Publisher':<{longest_publisher}}\n"
    for book in results:
      formatted_result += f"{book.getTitle():<{longest_title}}{book.getAuthors():<{longest_author}}{book.getPublisher():<{longest_publisher}}\n"
    
    return formatted_result

  def getRecommendations(self, typeOfMedia, title):
    """
    This function takes in a type of media and a title and returns a formatted string with all the recommendations
    for the title based on the associations between books and shows/movies.
    :param typeOfMedia: The type of media that the title is
    :param typeOfMedia type: string
    :param title: The title of the media
    :param title type: string
    :return: A formatted string with all the recommendations for the title
    :return type: string
    """
    if typeOfMedia == "Movie" or typeOfMedia == "TV Show":
      if self.__bookDict != {}:
        for idShow, show in self.__showDict.items():
          if show.getTitle() == title:
            result = ""
            if idShow in self.__associations:
              for currentID in self.__associations[idShow]:
                if currentID in self.__bookDict:
                  result += f"Title:\n{self.__bookDict[currentID].getTitle()}\nAuthor:\n{self.__bookDict[currentID].getAuthors()}\nAverage Rating:\n{self.__bookDict[currentID].getAverageRating()}\nISBN:\n{self.__bookDict[currentID].getISBN()}\nISBN13:\n{self.__bookDict[currentID].getISBN13()}\nLanguage Code:\n{self.__bookDict[currentID].getLanguage()}\nPages:\n{self.__bookDict[currentID].getPages()}\nRating Count:\n{self.__bookDict[currentID].getRatings()}\nPublication Date:\n{self.__bookDict[currentID].getPublicationDate()}\nPublisher:\n{self.__bookDict[currentID].getPublisher()}\n\n********************************\n\n"
            return result
        messagebox.showwarning("Error", "Title does not have any recommendations")
        return "No results"
      else:
        return "Enter books first to get recommendations"
    else:
      if self.__showDict != {}:
        for idBook, book in self.__bookDict.items():
          if book.getTitle() == title:
            result = ""
            if idBook in self.__associations:
              for currentID in self.__associations[idBook]:
                if currentID in self.__showDict:
                  result += f"Title:\n{self.__showDict[currentID].getTitle()}\nDirector:\n{self.__showDict[currentID].getDirector()}\nActors:\n{self.__showDict[currentID].getActors()}\nAverage Rating:\n{self.__showDict[currentID].getAverageRating()}\nCountry Code:\n{self.__showDict[currentID].getCountryCode()}\nDate Added:\n{self.__showDict[currentID].getDateAdded()}\nYear Released:\n{self.__showDict[currentID].getYearReleased()}\nRating:\n{self.__showDict[currentID].getRating()}\nDuration:\n{self.__showDict[currentID].getDuration()}\nGenres:\n{self.__showDict[currentID].getGenres()}\nDescription:\n{self.__showDict[currentID].getDescription()}\n\n********************************\n\n"
            return result
        messagebox.showwarning("Error", "Title does not have any recommendations")
        return "No results"
      else:
        return "Enter shows first to get recommendations"
      
  def getMovieChart(self):
    """
    Thus function creates a pie chart of the rating percentages for movies by iterating through the show dictionary 
    and only looking at the movies to obtain the rating percentages. After the loop, a number array and a key array 
    are created to store the values and keys of the rating and their counts. These arrays are then used to create the
    matplotlib pie chart in a figure which is then received by the GUI when the shows are input.
    :return: A figure of the pie chart of the rating percentages for movies
    """
    ratings = {}
    for show in self.__showDict:
      if (self.__showDict[show].getShowType() == "Movie"):
        #Get ratings for each movie and store in a dictionary
        if (self.__showDict[show].getRating() not in ratings):
          if ((self.__showDict[show].getRating() == "") and ("None" not in ratings)):
            ratings["None"] = 1
          elif ((self.__showDict[show].getRating() == "") and ("None" in ratings)):
            ratings["None"] += 1
          else:
            ratings[self.__showDict[show].getRating()] = 1
        else:
            ratings[self.__showDict[show].getRating()] += 1
    nums = []
    keys = []
    totalCount = 0
    #Making arrays for values and keys of rating and their counts to be used to create the matplotlib pie chart
    for rating, count in ratings.items():
      totalCount += count
      nums.append(count)
      keys.append(rating)
    graphNums = np.array(nums) / totalCount * 100
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot()
    ax.pie(graphNums, labels=keys, autopct='%1.1f%%')
    ax.set_title("Rating Percentages for Movies")
    #Return the figure/pie chart to be inserted into the TKinter Canvas
    return fig

  def getShowChart(self):
    """
    Thus function creates a pie chart of the rating percentages for shows by iterating through the show dictionary
    and only looking at the tv shows to obtain the rating percentages and their respective rating. After the loop, 
    a number array and a key array are created to store the values and keys of the rating and their counts. These 
    arrays are then used to create the matplotlib pie chart in a figure which is then received by the GUI when the 
    shows are input.
    :return: A figure of the pie chart of the rating percentages for shows
    """
    ratings = {}
    for movie in self.__showDict:
      if (self.__showDict[movie].getShowType() == "TV Show"):
        #Get ratings for each show and store in a dictionary
        if (self.__showDict[movie].getRating() not in ratings):
          if ((self.__showDict[movie].getRating() == "") and ("None" not in ratings)):
            ratings["None"] = 1
          elif ((self.__showDict[movie].getRating() == "") and ("None" in ratings)):
            ratings["None"] += 1
          else:
            ratings[self.__showDict[movie].getRating()] = 1
        else:
            ratings[self.__showDict[movie].getRating()] += 1
    nums = []
    keys = []
    totalCount = 0
    #Making arrays for values and keys of rating and their counts to be used to create the matplotlib pie chart
    for rating, count in ratings.items():
      totalCount += count
      nums.append(count)
      keys.append(rating)
    graphNums = np.array(nums) / totalCount * 100
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot()
    ax.pie(graphNums, labels=keys, autopct='%1.1f%%')
    ax.set_title("Rating Percentages for Shows")
    #Return the figure/pie chart to be inserted into the TKinter Canvas
    return fig