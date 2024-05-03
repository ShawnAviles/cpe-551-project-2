# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

from Book import Book
from Show import Show
from tkinter import filedialog
import os
from tkinter import messagebox

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
    file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    file = open(file, "r")
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
    file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    file = open(file, "r")
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
    file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(title="Input File", initialdir=os.getcwd(), filetypes=(("csv files", "*.csv"),))
    file = open(file, "r")
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
    for movie in self.__showDict:
      if (self.__showDict[movie].getShowType() == "Movie"):
        if (len(self.__showDict[movie].getTitle()) > largestTitle):
          largestTitle = len(self.__showDict[movie].getTitle())
        if (len(self.__showDict[movie].getDuration()) > largestRuntime):
          largestRuntime = len(self.__showDict[movie].getDuration())

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
    for show in self.__showDict:
      if (self.__showDict[show].getShowType() == "TV Show"):
        if (len(self.__showDict[show].getTitle()) > largestTitle):
          largestTitle = len(self.__showDict[show].getTitle())
        if (len(self.__showDict[show].getDuration()) > largestSeason):
          largestSeason = len(self.__showDict[show].getDuration())
    
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
    for book in self.__bookDict:
      if (len(self.__bookDict[book].getTitle()) > largestTitle):
        largestTitle = len(self.__bookDict[book].getTitle())
      if (len(self.__bookDict[book].getAuthors()) > largestAuthor):
        largestAuthor = len(self.__bookDict[book].getAuthors())
    
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

    formattedString += "Average Page Count: " + str(format(total/count, ".2f")) + " pages\n\n"
    formattedString += "Most Prolific Author: " + bestAuthor + "\n\n"
    formattedString += "Most Prolific Publisher: " + bestPublisher
    return formattedString
  
  def searchTVMovies():
    print("Search TV Movies")

  def searchBooks():
    print("Search Books")

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
  
# def main():
#   recommender = Recommender()
#   recommender.loadShows()
#   recommender.loadAssociations()
#   recommender.loadBooks()
#   result = recommender.getBookList()
#   print(result)
#   result = recommender.getBookStats()
#   print(result)
#   recommender.loadShows()
#   result = recommender.getTVList()
#   print(result)
#   result = recommender.getTVStats()
#   print(result)
#   result = recommender.getMovieList()
#   print(result)
#   result = recommender.getMovieStats()
#   print(result)

# main()