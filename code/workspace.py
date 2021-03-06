from talon import Module, Context, ui
import struct
from ctypes import cdll, windll
from win32gui import GetForegroundWindow
import win32gui
import win32con
from user.utils import utilities
try:
    import pyvda
except ImportError:
    pass

ASFW_ANY = -1

mod = Module()
ctx = Context()

CORE = utilities.load_toml_relative("config/core.toml")
mod.list("directions_alt", desc="Caster directions (lease, ross, sauce, dunce)")
ctx.lists["directions_alt"] = CORE["directions"]


def go_to_n(n):
    windll.user32.AllowSetForegroundWindow(ASFW_ANY)
    pyvda.GoToDesktopNumber(n)

@mod.action_class
class Actions:
    def window_maximise():
        """Maximise the current window"""
        wndh = GetForegroundWindow()
        win32gui.ShowWindow(wndh, win32con.SW_MAXIMIZE)

    def window_minimise():
        """Minimise the current window"""
        wndh = GetForegroundWindow()
        win32gui.ShowWindow(wndh, win32con.SW_MINIMIZE)

    def window_close():
        """Close the current window"""
        wndh = GetForegroundWindow()
        win32gui.PostMessage(wndh, win32con.WM_CLOSE, 0, 0)

    def workspace_send(n: int):
        """Close the current window"""
        wndh = ui.active_window().id
        pyvda.MoveWindowToDesktopNumber(wndh, n)

    def workspace_move(n: int):
        """Close the current window"""
        wndh = ui.active_window().id
        pyvda.MoveWindowToDesktopNumber(wndh, n)
        pyvda.GoToDesktopNumber(n)

    def workspace_go(n: int):
        """Close the current window"""
        windll.user32.AllowSetForegroundWindow(ASFW_ANY)
        pyvda.GoToDesktopNumber(n)

    def workspace_next(n: int):
        """Close the current window"""
        current = pyvda.GetCurrentDesktopNumber()
        go_to_n(current+n)

    def workspace_previous(n: int):
        """Close the current window"""
        current = pyvda.GetCurrentDesktopNumber()
        go_to_n(current-n)