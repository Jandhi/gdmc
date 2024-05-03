from typing import TypeVar

from colored import Fore, Style

from .benchmarking import Benchmark
from .settings import GeneratorSettings
from ..logger import Logger, LoggerSettings, LoggingLevel
from ..noise.global_seed import GlobalSeed
from ..noise.rng import RNG


class ModuleLogger(Logger):
    def __init__(self, settings: LoggerSettings, module: "Module") -> None:
        super().__init__(settings)
        self.module = module

    def format(
        self, text: str, level: LoggingLevel, is_in_console: bool = False
    ) -> str:
        if not self.settings.print_classname:
            return super().format(text, level, is_in_console)

        name = (
            f"{Fore.green}{self.module.get_name()}{Style.reset}"
            if is_in_console
            else self.module.get_name()
        )
        return super().format(f"{name}: {text}", level, is_in_console)


T = TypeVar("T")


class Module:
    name: str = None
    __logger: Logger = None
    rng: RNG

    def init_rng_from_world_seed(self):
        self.__setattr__("rng", RNG(GlobalSeed.get(), self.get_name()))

    @property
    def log(self) -> Logger:
        if not self.__logger:
            self.__logger = ModuleLogger(
                settings=GeneratorSettings.logger_settings, module=self
            )

        return self.__logger

    def set_module_logger_settings(self, logger_settings: LoggerSettings):
        self.log.settings = logger_settings

    """
    Decorator used to determine the main generator function for the module
    Benchmarking will begin when this is called and end when it is finished
    """

    class MainClass:
        def __init__(self, func):
            self.func = func

        # When main is bound to the owner, this allows for us to find the owners class
        def __set_name__(self, owner: "Module", name):
            # Owner is actually a type which inherits from Module, but this type annotation will do
            func = self.func

            def my_func(self, *args, **kwargs):
                return Benchmark.timed(
                    func=func, log=self.log, class_name=owner.get_name()
                )(self, *args, **kwargs)

            setattr(owner, name, my_func)

    @staticmethod
    def main(func: T) -> T:
        return Module.MainClass(func)

    @classmethod
    def get_name(cls) -> str:
        return cls.name or cls.__name__

    def raise_error(self, description: str):
        self.log.error(description)
        raise RuntimeError(description)
