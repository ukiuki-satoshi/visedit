import unicodedata

from . import color_settings

class Tagger:

    COLOR_CODE = {
        'BLACK': 'black',
        'RED': 'red',
        'GREEN': 'green',
        'YELLOW': 'yellow',
        'BLUE': 'blue',
        'PURPLE': 'purple',
        'CYAN': 'cyan',
        'WHITE': 'white',
    }

    @staticmethod
    def striked(text):
        return ''.join(["<s>", text, "</s>"])

    @staticmethod
    def colored(text, color):
        if color.upper() not in Tagger.COLOR_CODE:
            raise Exception("Invalid Color: {c}".format(c=color))
        color_code = Tagger.COLOR_CODE[color.upper()]
        return ''.join(['<span style="color: ', color_code, ';">', text, "</span>"])
        
    @staticmethod
    def td(text):
        return ''.join(['<td style="text-align=center">', text, "</td>"])
    
    @staticmethod
    def tr(text):
        return ''.join(["<tr>", text, "</tr>"])
    
    @staticmethod
    def table(text):
        return ''.join(['<table style="table-layout: fixed;">', text, "</table>"])

class Textizer:

    COLOR_CODE = {
        'BLACK': '\033[30m',
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'PURPLE': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
        'END': '\033[0m',
        'BOLD': '\038[1m',
        'UNDERLINE': '\033[4m',
        'INVISIBLE': '\033[08m',
        'REVERSE': '\033[07m',
    }

    @staticmethod
    def get_char_width(char):
        char_type = unicodedata.east_asian_width(char)
        if char_type in ["W", "F"]:
            return 2
        else:
            return 1
        
    @staticmethod
    def padding_char(char):
        if char in ["", " "]:
            return "  "
        elif Textizer.get_char_width(char) == 1:
            return " " + char
        else:
            return char
        
    @staticmethod
    def colored(text, color):

        if color.upper() not in Textizer.COLOR_CODE:
            raise Exception("Invalid Color: {c}".format(c=color))
        return Textizer.COLOR_CODE[color.upper()] + text + Textizer.COLOR_CODE["END"]

class HTMLFormatter(object):
    def __init__(self, color_settings):
       self._cs = color_settings

    def elem(self, text):
        return Tagger.td(
            Tagger.colored(text, self._cs["base"]))

    def padding(self, text):
        return text

    def wrong(self, text):
        return Tagger.colored(text, self._cs["wrong"])

    def correct(self, text):
        return Tagger.colored(text, self._cs["correct"])

    def output(self, t1, t2):
        return Tagger.table(Tagger.tr(t1) + Tagger.tr(t2))
    
class TextFormatter(object):
    def __init__(self, color_settings, truncate=False):
        self._cs = color_settings
        self._truncate = truncate

    def elem(self, text):
        return Textizer.colored(text, self._cs["base"])

    def padding(self, text):
        if self._truncate:
            return text
        else:
            return Textizer.padding_char(text)

    def wrong(self, text):
        return Textizer.colored(text, self._cs["wrong"])

    def correct(self, text):
        return Textizer.colored(text, self._cs["correct"])

    def output(self, t1, t2):
        return t1 + "\n" + t2
