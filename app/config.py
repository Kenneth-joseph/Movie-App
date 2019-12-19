class Config:
    """
    General configuration parent class
    """
    pass

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


class ProdConfig(Config):
    """
    production config child class
    """
    pass


class DevConfig(Config):
    """
    Dvlpmnt config child class
     Args:
    Config: The parent configuration class with General configuration settings
    """
    DEBUG = True
