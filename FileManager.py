import json
import os

class FileManager:
    """ Gestionnaire de fichiers pour lire et écrire des données dans des fichiers. """
    @staticmethod
    def write_data(file_name, data):
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_data(file_name):
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                return json.load(file)
        return None