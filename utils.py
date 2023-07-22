import time
import re
import win32api, win32con, win32gui
import ctypes
import keyboard


class WindowManager:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None
        self._user32 = ctypes.windll.user32

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        self._user32.SetForegroundWindow(self._handle)
        if self._user32.IsIconic(self._handle):
            self._user32.ShowWindow(self._handle, 9)


def rightClick():
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    time.sleep(.1)


def leftClick():
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)


def setCursorPos(where):
    win32api.SetCursorPos(where)


def press(what, cooldown=0):
    keyboard.press_and_release(what)
    time.sleep(cooldown)