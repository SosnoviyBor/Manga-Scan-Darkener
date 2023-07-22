import win32api


# Название браузера брать отсюда
# https://docs.python.org/3/library/webbrowser.html
BROWSER = "chrome"
# Да, двойные бекслеши важны
BROWSER_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Папка со сканами
WORKFOLDER = "E:\\Data\\Переведунство\\darkener\\"

# Сколько раз прогонять скрипт затемнения на папку
ITERANTIONS = 1


class MouseCoordinates:
    # + = вниз/вправо
    # - = вверх/влево
    MONITOR_WIDTH = win32api.GetSystemMetrics(0)
    MONITOR_HEIGHT = win32api.GetSystemMetrics(1)
    
    CENTER = (
        int(MONITOR_WIDTH / 2),
        int(MONITOR_HEIGHT / 2)
    )
    CONTEXT_MENU_COPY_BUTTON = (
        CENTER[0] + 10,
        CENTER[1] + 60
    )
    EXTENSION_MENU = (
        CENTER[0],
        MONITOR_HEIGHT - 190
    )
    EXTENSION_PNG_BUTTON = (
        CENTER[0],
        EXTENSION_MENU[0] - 145
    )


class KeyInputs:
    CLOSE_TAB = "ctrl+w"
    PASTE = "ctrl+v"
    FLATTEN_IMAGE = "ctrl+r"     # Кастомный бинд!
    SAVE_AS = "ctrl+shift+s"
    UNDO = "ctrl+z"
    ENTER = "enter"
    TAB = "tab"