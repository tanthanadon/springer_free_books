from pathlib import Path
import os

if __name__ == "__main__":
    os.system("cat part* > springer_free_books.zip")
    os.system("unzip springer_free_books.zip")
        
