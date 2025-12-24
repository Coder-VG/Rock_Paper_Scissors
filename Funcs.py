import os
import sys

def quitProgram() -> None:
  print("Thanks for playing!")
  quit()

def clearTerminal() -> None:
  os.system("cls" if os.name == "nt" else "clear")

def clearLastLine(lines:int = 1) -> None:
  for line in range(lines):
    sys.stdout.write('\033[A')  # Move cursor up one line
    sys.stdout.write('\033[K')  # Clear the line

def getColorCode(col:str='r'):
  if col=='g':  return '\033[92m'  # GREEN
  elif col=='bg':  return '\033[92m\033[1m'  # BRIGHT_GREEN
  elif col=='gray':  return '\033[90m'  # GRAY
  elif col=='r':  return '\033[0m'  # RESET