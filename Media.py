# "I pledge my honor that I have abided by the Stevens Honor System." - Shawn Aviles, Justin Ferber, Harris Pyo
# Author: Shawn Aviles, Justin Ferber, Harris Pyo
# Date: 5/5/24
# Description: 

class Media:
    def __init__(self, newID, title, averageRating):
        """
        Constructor for Media class
        :param newID: ID of the media
        :type newID: string
        :param title: Title of the media
        :type title: string
        :param averageRating: Average rating of the media
        :type averageRating: float
        :return: Instance of Media class
        :rtype: Media
        """
        self.__ID = newID
        self.__title = title
        self.__avgRating = averageRating
    
    def getID(self):
        """
        Get the ID of the media
        :return: ID of the media
        :rtype: string
        """
        return self.__ID
    
    def setID(self, newID):
        """
        Set the ID of the media
        :param newID: New ID of the media
        :type newID: string
        :return: None
        """
        self.__ID = newID

    def getTitle(self):
        """
        Get the title of the media
        :return: Title of the media
        :rtype: string
        """
        return self.__title
    
    def setTitle(self, newTitle):
        """
        Set the title of the media
        :param newTitle: New title of the media
        :type newTitle: string
        :return: None
        """
        self.__title = newTitle

    def getAverageRating(self):
        """
        Get the average rating of the media
        :return: Average rating of the media
        :rtype: float
        """
        return self.__avgRating
    
    def setAverageRating(self, newAverage):
        """
        Set the average rating of the media
        :param newAverage: New average rating of the media
        :type newAverage: float
        :return: None
        """
        self.__avgRating = newAverage