class Config:
    """
    General configuration parent class
    """
    pass


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
