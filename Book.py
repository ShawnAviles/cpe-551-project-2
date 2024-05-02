# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

from Media import Media

class Book(Media):
    def __init__(self, newID, title, averageRating, authors, isbn, isbn13, language, pages, ratings, publicationDate, publisher):
        """
        Constructor for Book class
        :param newID: ID of the book
        :type newID: string
        :param title: Title of the book
        :type title: string
        :param averageRating: Average rating of the book
        :type averageRating: float
        :param author: Author of the book
        :type author: string
        :param isbn: ISBN of the book
        :type isbn: string
        :param isbn13: ISBN13 of the book
        :type isbn13: string
        :param language: Language of the book
        :type language: string
        :param pages: Number of pages in the book
        :type pages: int
        :param ratings: Number of ratings given to the book
        :type ratings: int
        :param publicationDate: Publication date of the book
        :type publicationDate: string
        :param publisher: Publisher of the book
        :type publisher: string
        :return: Instance of Book class
        :rtype: Book
        """
        super().__init__(newID, title, averageRating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__language = language
        self.__pages = pages
        self.__ratings = ratings
        self.__publicationDate = publicationDate
        self.__publisher = publisher
        
    # Accessor functions
    def getAuthors(self):
        """
        Get the author of the book
        :return: Author of the book
        :rtype: string
        """
        return self.__authors
    
    def getISBN(self):
        """
        Get the ISBN of the book
        :return: ISBN of the book
        :rtype: string
        """
        return self.__isbn
    
    def getISBN13(self):
        """
        Get the ISBN13 of the book
        :return: ISBN13 of the book
        :rtype: string
        """
        return self.__isbn13
    
    def getLanguage(self):
        """
        Get the language of the book
        :return: Language of the book
        :rtype: string
        """
        return self.__language
    
    def getPages(self):
        """
        Get the number of pages in the book
        :return: Number of pages in the book
        :rtype: int
        """
        return self.__pages
    
    def getRatings(self):
        """
        Get the number of ratings given to the book
        :return: Number of ratings given to the book
        :rtype: int
        """
        return self.__ratings
    
    def getPublicationDate(self):
        """
        Get the publication date of the book
        :return: Publication date of the book
        :rtype: string
        """
        return self.__publicationDate
    
    def getPublisher(self):
        """
        Get the publisher of the book
        :return: Publisher of the book
        :rtype: string
        """
        return self.__publisher
    
    # Mutator functions
    def setAuthors(self, newAuthors):
        """
        Set the author of the book
        :param newAuthor: New author of the book
        :type newAuthor: string
        :return: None
        """
        self.__authors = newAuthors
        
    def setISBN(self, newISBN):
        """
        Set the ISBN of the book
        :param newISBN: New ISBN of the book
        :type newISBN: string
        :return: None
        """
        self.__isbn = newISBN
        
    def setISBN13(self, newISBN13):
        """
        Set the ISBN13 of the book
        :param newISBN13: New ISBN13 of the book
        :type newISBN13: string
        :return: None
        """
        self.__isbn13 = newISBN13
    
    def setLanguage(self, newLanguage):
        """
        Set the language of the book
        :param newLanguage: New language of the book
        :type newLanguage: string
        :return: None
        """
        self.__language = newLanguage
    
    def setPages(self, newPages):
        """
        Set the number of pages in the book
        :param newPages: New number of pages in the book
        :type newPages: int
        :return: None
        """
        self.__pages = newPages
        
    def setRatings(self, newRatings):
        """
        Set the number of ratings given to the book
        :param newRatings: New number of ratings given to the book
        :type newRatings: int
        :return: None
        """
        self.__ratings = newRatings
        
    def setPublicationDate(self, newPublicationDate):
        """
        Set the publication date of the book
        :param newPublicationDate: New publication date of the book
        :type newPublicationDate: string
        :return: None
        """
        self.__publicationDate = newPublicationDate
    
    def setPublisher(self, newPublisher):
        """
        Set the publisher of the book
        :param newPublisher: New publisher of the book
        :type newPublisher: string
        :return: None
        """
        self.__publisher = newPublisher
