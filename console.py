from datetime import datetime
import rich
from rich.table import Table

class timer:

    def __init__(self) -> None:
        self.time = datetime.now()

    def getTime(self) -> str:
        now = datetime.now()
        delta = now - self.time
        return delta.total_seconds()

class Console:

    def __init__(self) -> None:
        self.timers: dict = {}

    def _init_grid(self) -> Table.grid:
        grid = Table.grid()
        grid.add_column()
        grid.add_column()

        return grid

    def _get_time(self) -> str:
        return datetime.now().strftime("[grey23][bold][[/bold]%H:%M:%S[bold]][/bold][/grey23] ")

    def log(self, toLog: str) -> None:
        grid = self._init_grid()
        grid.add_row(self._get_time(), toLog)
        rich.print(grid)

    def info(self, toLog: str) -> None:
        grid = self._init_grid()
        grid.add_row(self._get_time(), f"[white on cyan] INFO [/white on cyan] [cyan bold]{toLog}[/cyan bold]")
        rich.print(grid)

    def warn(self, toWarn: str) -> None:
        grid = self._init_grid()
        grid.add_row(self._get_time(), f"[black on yellow] WARN [/black on yellow] [yellow]{toWarn}[/yellow]")
        rich.print(grid)

    def error(self, toError: str) -> None:
        grid = self._init_grid()
        grid.add_row(self._get_time(), f"[white on red] ERROR [/white on red] [red bold]{toError}[/red bold]")
        rich.print(grid)

    def clear(self) -> None:
        print("\033[H\033[J")

    def time(self, timerName: str="timer"):
        self.timers[timerName] = timer()

    def timeEnd(self, timerName: str="timer") -> float:
        time = self.timers.get(timerName)

        if time:
            seconds = time.getTime()
            self.timers.pop(timerName)
            return seconds

    def timeLog(self, timerName: str="timer") -> float:
        time = self.timers.get(timerName)

        if time:
            return time.getTime()

if __name__ == "__main__":
    console = Console()
    console.error("Hello, World")
    console.warn("Hello, World")
    console.info("Hello, World")