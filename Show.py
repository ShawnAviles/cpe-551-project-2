from Media import Media

class Show(Media):
    def __init__(self, newID, title, averageRating, showType, directors, actors, countryCode, dateAdded, yearReleased, rating, duration, genres, description):
        """
        Constructor for Show class
        :param newID: ID of the show
        :type newID: string
        :param title: Title of the show
        :type title: string
        :param averageRating: Average rating of the show
        :type averageRating: float
        :param showType: Type of the show
        :type showType: string
        :param directors: Directors of the show
        :type directors: string
        :param actors: Actors in the show
        :type actors: string
        :param countryCode: Country code of the show
        :type countryCode: string
        :param dateAdded: Date the show was added
        :type dateAdded: string
        :param yearReleased: Year the show was released
        :type yearReleased: int
        :param rating: Rating of the show
        :type rating: float
        :param duration: Duration of the show
        :type duration: int
        :param genres: Genres of the show
        :type genres: string
        :param description: Description of the show
        :type description: string
        :return: Instance of Show class
        :rtype: Show
        """
        super().__init__(newID, title, averageRating)
        self.__showType = showType
        self.__directors = directors
        self.__actors = actors
        self.__countryCode = countryCode
        self.__dateAdded = dateAdded
        self.__yearReleased = yearReleased
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description
        
    # Accessor functions
    def getShowType(self):
        """
        Get the type of the show
        :return: Type of the show
        :rtype: string
        """
        return self.__showType
    
    def getDirectors(self):
        """
        Get the directors of the show
        :return: Directors of the show
        :rtype: string
        """
        return self.__directors
    
    def getActors(self):
        """
        Get the actors in the show
        :return: Actors in the show
        :rtype: string
        """
        return self.__actors
    
    def getCountryCode(self):
        """
        Get the country code of the show
        :return: Country code of the show
        :rtype: string
        """
        return self.__countryCode
    
    def getDateAdded(self):
        """
        Get the date the show was added
        :return: Date the show was added
        :rtype: string
        """
        return self.__dateAdded
    
    def getYearReleased(self):
        """
        Get the year the show was released
        :return: Year the show was released
        :rtype: int
        """
        return self.__yearReleased
    
    def getRating(self):
        """
        Get the rating of the show
        :return: Rating of the show
        :rtype: float
        """
        return self.__rating
    
    def getDuration(self):
        """
        Get the duration of the show
        :return: Duration of the show
        :rtype: int
        """
        return self.__duration
    
    def getGenres(self):
        """
        Get the genres of the show
        :return: Genres of the show
        :rtype: string
        """
        return self.__genres
    
    def getDescription(self):
        """
        Get the description of the show
        :return: Description of the show
        :rtype: string
        """
        return self.__description
    
    # Mutator functions
    def setShowType(self, newShowType):
        """
        Set the type of the show
        :param newShowType: New type of the show
        :type newShowType: string
        :return: None
        """
        self.__showType = newShowType
        
    def setDirectors(self, newDirectors):
        """
        Set the directors of the show
        :param newDirectors: New directors of the show
        :type newDirectors: string
        :return: None
        """
        self.__directors = newDirectors
    
    def setActors(self, newActors):
        """
        Set the actors in the show
        :param newActors: New actors in the show
        :type newActors: string
        :return: None
        """
        self.__actors = newActors
    
    def setCountryCode(self, newCountryCode):
        """
        Set the country code of the show
        :param newCountryCode: New country code of the show
        :type newCountryCode: string
        :return: None
        """
        self.__countryCode = newCountryCode
    
    def setDateAdded(self, newDateAdded):
        """
        Set the date the show was added
        :param newDateAdded: New date the show was added
        :type newDateAdded: string
        :return: None
        """
        self.__dateAdded = newDateAdded
        
    def setYearReleased(self, newYearReleased):
        """
        Set the year the show was released
        :param newYearReleased: New year the show was released
        :type newYearReleased: int
        :return: None
        """
        self.__yearReleased = newYearReleased
        
    def setRating(self, newRating):
        """
        Set the rating of the show
        :param newRating: New rating of the show
        :type newRating: float
        :return: None
        """
        self.__rating = newRating
    
    def setDuration(self, newDuration):
        """
        Set the duration of the show
        :param newDuration: New duration of the show
        :type newDuration: int
        :return: None
        """
        self.__duration = newDuration
    
    def setGenres(self, newGenres):
        """
        Set the genres of the show
        :param newGenres: New genres of the show
        :type newGenres: string
        :return: None
        """
        self.__genres = newGenres
    
    def setDescription(self, newDescription):
        """
        Set the description of the show
        :param newDescription: New description of the show
        :type newDescription: string
        :return: None
        """
        self.__description = newDescription
    