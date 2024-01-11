import curses
import time
from colorama import Fore, Back, Style

class ProgressBarLogger:

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.start_color()        
        curses.use_default_colors()
        
        self.stdscr.clear()
        self.height, self.width = self.stdscr.getmaxyx()

        self.progress_win = curses.newwin(5, self.width, self.height -3, 1)
        self.log_win = curses.newwin(self.height - 3, self.width - 2, 1, 1)

    def initUI(self, text):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN) 
        self.progress_win.addstr(1, 0, text, curses.color_pair(1))
        self.progress_win.addstr(2, 0, "Progreso: [")
        self.progress_win.refresh()

        self.log_win.scrollok(True)
        self.log_win.idlok(True)
        self.log_win.refresh()

    def drawProgressBar(self, progress):
        bar_width = self.width - 20
        bar_progress = int(bar_width * progress / 100)

        self.progress_win.addstr(2, 12, "#" * bar_progress) 
        self.progress_win.addstr(2, 14 + bar_width, f"{progress}% ]")
        self.progress_win.refresh()

    def log(self, message):
        self.log_win.addstr(message + '\n')
        self.log_win.refresh()

    def close(self):
        curses.endwin()

if __name__ == "__main__":

    progress_logger = ProgressBarLogger()
    progress_logger.initUI()

    try:
        for i in range(101):
            progress_logger.drawProgressBar(i)
            progress_logger.log(f"Actualización número {i}")

            time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass

    finally:
        progress_logger.close()
