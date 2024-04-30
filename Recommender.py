# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

from Book import Book
from Show import Show
import os

class Recommender:
  def __init__(self):
    self.__bookDict = {}
    self.__showDict = {}
    self.__associations = {}
  
  def loadBooks(self):
    filedialog = input("Please enter the name of the file that you would like to load books from: ")
    if (not os.path.exists(filedialog)):
      while (not os.path.exists(filedialog)): 
        filedialog = input(f"{filedialog} does not exist! Please enter the name of the file that you would like to load books from: ")
    readFile = open(filedialog, "r")
    for line in readFile:
      formattedLine = line.strip().split(",")
      newBook = Book(formattedLine[0], formattedLine[1], float(formattedLine[2]), formattedLine[3], formattedLine[4], formattedLine[5], formattedLine[6], int(formattedLine[7]), int(formattedLine[8]), formattedLine[9], formattedLine[10])
      if (formattedLine[0] not in self.__bookDict):
        self.__bookDict[formattedLine[0]] = newBook
    readFile.close()
  
  def loadShows(self):
    filedialog = input("Please enter the name of the file that you would like to load shows from: ")
    if (not os.path.exists(filedialog)):
      while (not os.path.exists(filedialog)): 
        filedialog = input(f"{filedialog} does not exist! Please enter the name of the file that you would like to load shows from: ")
    readFile = open(filedialog, "r")
    for line in readFile:
      formattedLine = line.strip().split(",")
      newShow = Show(formattedLine[0], formattedLine[1], float(formattedLine[2]), formattedLine[3], formattedLine[4], formattedLine[5], formattedLine[6], formattedLine[7], int(formattedLine[8]), float(formattedLine[9]), int(formattedLine[10]), formattedLine[11], formattedLine[12])
      if (formattedLine[0] not in self.__showDict):
        self.__showDict[formattedLine[0]] = newShow
    readFile.close()

  def loadAssociations(self):
    filedialog = input("Please enter the name of the file that you would like to load associations from: ")
    if (not os.path.exists(filedialog)):
      while (not os.path.exists(filedialog)): 
        filedialog = input(f"{filedialog} does not exist! Please enter the name of the file that you would like to load associations from: ")
    readFile = open(filedialog, "r")
    for line in readFile:
      formattedLine = line.strip().split(",")
      if (formattedLine[0] not in self.__associations):
        self.__associations[formattedLine[0]] = {formattedLine[1]: 1}
      elif (formattedLine[1] not in self.__associations[formattedLine[0]]):
        self.__associations[formattedLine[0]][formattedLine[1]] = 1
      else:
        self.__associations[formattedLine[0]][formattedLine[1]] += 1
    for line in readFile:
      formattedLine = line.strip().split(",")
      if (formattedLine[1] not in self.__associations):
        self.__associations[formattedLine[1]] = {formattedLine[0]: 1}
      elif (formattedLine[0] not in self.__associations[formattedLine[01]]):
        self.__associations[formattedLine[1]][formattedLine[0]] = 1
      else:
        self.__associations[formattedLine[1]][formattedLine[0]] += 1
    readFile.close()

    