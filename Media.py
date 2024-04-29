class Media:
    def __init__(self, newID, title, averageRating):
        self.__ID = newID
        self.__title = title
        self.__avgRating = averageRating
    
    def getID(self):
        return self.__ID
    def setID(self, newID):
        self.__ID = newID

    def getTitle(self):
        return self.__title
    def setTitle(self, newTitle):
        self.__title = newTitle

    def getAverageRating(self):
        return self.__avgRating
    def setAverageRating(self, newAverage):
        self.__avgRating = newAverage