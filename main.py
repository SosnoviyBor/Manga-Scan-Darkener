import config
from utils import *

import webbrowser
import os
import time


def main():
    webbrowser.register(config.BROWSER, None, webbrowser.BackgroundBrowser(config.BROWSER_PATH))
    browser = webbrowser.get(config.BROWSER)
    files = os.listdir(config.WORKFOLDER)
    images = set()
    for file in files:
        images.add(file[:-4])
    images = sorted(list(images))
    image_count = len(images)
    
    print(
       f"Найдено {image_count} изображений. Одна итерация их обработки займет около " +
       f"{image_count * 5.9} секунд\n" +
       "\n" +
       "Скрипт запущен. Пожалуйста, не трогайте мышь на протяжении его работы \n"
    )
    time.sleep(3)
    
    start_time = time.time()
    parse_images(browser, images)
    end_time = round(time.time() - start_time, 2)
    
    print(f"{image_count} изображений было успешно обработано за {end_time} сек")


def parse_images(browser:webbrowser.BaseBrowser, images:list):
    for _ in range(config.ITERANTIONS):
        for image_id in images:
            image_png = config.WORKFOLDER + image_id + ".png"
            image_psd = config.WORKFOLDER + image_id + ".psd"
            
            # Открыть ПСД в фотошопе
            os.startfile(image_psd)
            time.sleep(.5)
            
            # Открыть ПНГ в браузере и скопировать его
            browser.open(image_png)
            setCursorPos(config.MouseCoordinates.CENTER)
            rightClick()
            setCursorPos(config.MouseCoordinates.CONTEXT_MENU_COPY_BUTTON)
            leftClick()
            press(config.KeyInputs.CLOSE_TAB, .1)
            
            # Открыть окно фотошопа
            window = WindowManager()
            window.find_window_wildcard(f"{image_id}.psd*")
            window.set_foreground()
            
            # Пройтись в фотошопе по файлу
            # Окно фотошопа
            press(config.KeyInputs.PASTE, .1)
            press(config.KeyInputs.FLATTEN_IMAGE, .1)
            press(config.KeyInputs.SAVE_AS, .75)
            # Окно "Сохранить как"
            setCursorPos(config.MouseCoordinates.EXTENSION_MENU)
            leftClick()
            setCursorPos(config.MouseCoordinates.EXTENSION_PNG_BUTTON)
            leftClick()
            press(config.KeyInputs.ENTER, .1)
            # Предупреждение о перезаписи старого ПНГ
            press(config.KeyInputs.TAB, .1)
            press(config.KeyInputs.ENTER, .5)
            # Выбор способа сохранения в ПНГ
            press(config.KeyInputs.ENTER, .5)
            # Откат ПСД
            press(config.KeyInputs.UNDO, .1)
            # Окно "Сохранить как"
            press(config.KeyInputs.SAVE_AS, .5)
            press(config.KeyInputs.ENTER, .5)
            # Предупреждение о перезаписи старого ПСД
            press(config.KeyInputs.TAB, .1)
            press(config.KeyInputs.ENTER, .5)
            # Закрытие вкладки со страницей
            press(config.KeyInputs.CLOSE_TAB)


if __name__ == "__main__":
    main()