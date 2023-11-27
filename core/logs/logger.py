from enum import Enum
from colored import Fore, Style
from dataclasses import dataclass
from datetime import datetime
from io import TextIOWrapper
from tqdm import tqdm
from typing import Iterable

@dataclass
class _LoggingLevel:
    rank : int
    color : str

class LoggingLevel(Enum):
    CRITICAL = _LoggingLevel(60, Fore.red)
    ERROR    = _LoggingLevel(50, Fore.light_red)
    WARNING  = _LoggingLevel(40, Fore.yellow)
    SUCCESS  = _LoggingLevel(30, Fore.green)
    INFO     = _LoggingLevel(20, Fore.cyan)
    DEBUG    = _LoggingLevel(10, Fore.dark_gray)

class LoggerSettings:
    print_to_console : bool
    print_timestamp : bool
    print_level : bool
    print_classname : bool
    minimum_console_level : LoggingLevel
    minimum_file_level : LoggingLevel
    __file : TextIOWrapper

    def __init__(self,
                    print_to_console : bool = True,
                    print_timestamp : bool = False,
                    print_level : bool = True,
                    print_classname : bool = True,
                    output_file : str | None = None,
                    minimum_console_level : LoggingLevel = LoggingLevel.DEBUG,
                    minimum_file_level : LoggingLevel = LoggingLevel.DEBUG,
                 ) -> None:
        self.print_to_console = print_to_console
        self.print_timestamp = print_timestamp
        self.print_level = print_level
        self.print_classname = print_classname
        self.__output_file = output_file
        self.__file = None
        self.minimum_console_level = minimum_console_level
        self.minimum_file_level = minimum_file_level

        if output_file:
            self.__file = open(output_file, mode='w')

    __output_file : str | None

    def clone(self):
        return LoggerSettings(
            self.print_to_console,
            self.print_timestamp,
            self.print_level,
            self.print_classname,
            self.__output_file,
            self.minimum_console_level,
            self.minimum_file_level
        )
    
    @property
    def output_file(self) -> str | None:
        return self.__output_file
    
    # We ensure that a new output_file string will open the right file
    @output_file.setter
    def output_file(self, value : str | None):
        if self.output_file:
            self.__file.close()

        self.__output_file = value

        if value:
            self.__file = open(value, mode='w')
    
    def __del__(self):
        if self.output_file:
            self.__file.close()

class Logger:
    settings : LoggerSettings

    def __init__(self, settings : LoggerSettings | None = None) -> None:
        self.settings = settings or LoggerSettings()

    def format(self, text : str, level : LoggingLevel, is_in_console : bool = False) -> str:
        if self.settings.print_level:
            # We don't use colors unless we are in console
            level_str = f'{level.value.color}{level.name}{Style.reset}' if is_in_console else level.name
            buffer = (max(0, 5 - len(level.name))) * ' '
            text = f'[{level_str}]{buffer} {text}'
        
        if self.settings.print_timestamp:
            timestamp = f'{datetime.now().strftime("%H:%M:%S")} - '

            if is_in_console:
                timestamp = f'{Fore.dark_gray}{timestamp}{Style.reset}'

            text = f'{timestamp}{text}'

        # Add newlines for file printing
        if not is_in_console:
            text = f'{text}\n'
        
        return text

    def __log(self, text : str, level : LoggingLevel):
        
        is_console_level = level.value.rank >= self.settings.minimum_console_level.value.rank
        if self.settings.print_to_console and is_console_level:
            print(
                self.format(text=text, level=level, is_in_console=True)
            )

        is_file_level = level.value.rank >= self.settings.minimum_file_level.value.rank
        if self.settings.output_file and is_file_level:
            file_text = self.format(text=text, level=level, is_in_console=False)
            self.settings._LoggerSettings__file.write(file_text)

    def debug(self, text : str):
        self.__log(text, LoggingLevel.DEBUG)

    def info(self, text : str):
        self.__log(text, LoggingLevel.INFO)

    def warning(self, text : str):
        self.__log(text, LoggingLevel.WARNING)

    def error(self, text : str):
        self.__log(text, LoggingLevel.ERROR)

    def critical(self, text : str):
        self.__log(text, LoggingLevel.CRITICAL)

    # skips log formatting
    def display(self, text : str, console_only=False):
        if self.settings.print_to_console:
            print(text)
        if self.settings.output_file and not console_only:
            self.settings._LoggerSettings__file.write(text)

    def progress(self, iterable : Iterable, description : str, position : int = 0, leave=True):
        output = self.format(
            text=description, 
            level=LoggingLevel.INFO, 
            is_in_console=True
        )

        return tqdm(iterable=iterable, desc=output, position=position, leave=leave)