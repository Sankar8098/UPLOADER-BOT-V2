import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5909685271:AAGrx4Ghfrwvw_J9DH2WS2nXLjAjLF6BrTM")
    
    API_ID = int(os.environ.get("API_ID", "23990433"))
    
    API_HASH = os.environ.get("API_HASH","e6c4b6ee1933711bc4da9d7d17e1eb20")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5821871362"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    MAX_RESULTS = "50"
