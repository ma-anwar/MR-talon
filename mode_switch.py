from talon.engine import engine
from talon.voice import ui
from talon import cron
from utils import actions

command_exes = ["code.exe", "mintty.exe", "kindle.exe"]
command_titles = []

in_command_context = False

def switch_command():
    engine.mimic("switch to command mode")

def switch_normal():
    engine.mimic("switch to normal mode")

def check_context():
    global in_command_context
    if actions.context_matches(command_titles, command_exes)(ui.active_app(), ui.active_window()):
        if in_command_context:
            return
        else:
            in_command_context = True
            switch_command()
    else:
        if in_command_context:
            in_command_context= False
            switch_normal()
        else:
            return

cron.interval("1s", check_context)