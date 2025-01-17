class Config:
    DEBUG = True
    TESTING = True

    #Configuración de base dedatos 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/dbblog"
    

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True