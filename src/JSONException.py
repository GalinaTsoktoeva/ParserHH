import json


class JSONException:
    """Класс для обработки исключения, если файл поврежден"""
    def __init__(self, *args):
        self.message = args[0] if args else "JSON файл поврежден"

    def __str__(self):
        return self.message

