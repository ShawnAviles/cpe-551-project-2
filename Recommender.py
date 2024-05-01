# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

from Book import Book
from Show import Show
from tkinter import Tk
from tkinter import filedialog
import os

class Recommender:
  def __init__(self):
    self.__bookDict = {}
    self.__showDict = {}
    self.__associations = {}
  
  def loadBooks(self):
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
    file = filedialog.askopenfilename(mode='r', title="Input File", filetypes=(("csv files", "*.csv")))
    if (not file):
      while (not file): 
        file = filedialog.askopenfilename(mode='r', title="Input File", filetypes=(("csv files", "*.csv")))
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
    formattedString = ""
    largestTitle = 0
    largestAuthor = 0
    for book in self.__bookDict:
      if (len(self.__bookDict[book].getTitle()) > largestTitle):
        largestTitle = len(self.__bookDict[book].getTitle())
      if (len(self.__bookDict[book].getAuthor()) > largestAuthor):
        largestAuthor = len(self.__bookDict[book].getAuthor())
    
    formattedString += format("Title", str(largestTitle + 2)) + format("Author(s)", str(largestAuthor)) + "\n"
    for book in self.__bookDict:
      formattedString += format(self.__bookDict[book].getTitle(), str(largestTitle + 2)) + format(self.__bookDict[book].getAuthor(), str(largestAuthor)) + "\n"
    return formattedString

def main():
  recommender = Recommender()
  recommender.loadBooks()
  result = recommender.getBookList()
  print(result)

main()