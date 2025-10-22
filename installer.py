#!/usr/bin/env python3

import importlib.util
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

# Списсок необходимых библиотек
REQUIRED_LIBRARIES = ["eth_account"]

# Установщик библиотеки через pip
def install_library(library):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        return True, f"Библиотека {library} успешно утсновленна"
    except subprocess.CalledProcessError:
        return False, f"Ошибка при установке {library}, проверьте подключение к интернету и права для устанвки"

# Проверяет и устанавливает
def check_and_install_libraries(root=None):
    missing_libraries = []
    for library in REQUIRED_LIBRARIES:
        if importlib.util.find_spec(library) is None:
            missing_libraries.append(library)

    if missing_libraries:
        if root: # Если передан root , показываем сообщение
            messagebox.showerror("Установка зависимостей", f"Обнаруженны отсутсвующие библиотеки: {',' .join(missing_libraries)}. Устанавливаю.......")
            print(f"Обнаруженно остутсвие бибоиотеки: {',' .join(missing_libraries)}. Устанавливаю.....")

    for library in missing_libraries:
        success, message = install_library(library)
        print(message)
        if root:
            messagebox.showinfo("Результат установки", message)
        if not success:
            if root:
                messagebox.showerror("Ошибка", f"Не удалось установить {library}. проверьте интернет и права доступа")
            sys.exit(1)
    else:
        if root:
            messagebox.showinfo("Проверка зависимостей", "Все необходимые библиотеки установленны")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    check_and_install_libraries()
    root.destroy()