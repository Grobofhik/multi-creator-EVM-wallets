#!/usr/bin/env python3
import os
import subprocess
import sys  # Добавлен импорт sys
from installer import check_and_install_libraries

# Создание GUI
try:
    import tkinter as tk
    from tkinter import messagebox, scrolledtext
except ImportError as e:
    print(f"Ошибка: {e}. Установите tkinter вручную и попробуйте снова.")
    sys.exit(1)

# Проверка и установка библиотек перед запуском
check_and_install_libraries(root=tk.Tk())  # Создаём временное окно для сообщений

# Теперь безопасно импортируем eth_account
from eth_account import Account

# Включение поддержки mnemonic (seed-фраз) из eth_account
Account.enable_unaudited_hdwallet_features()

def create_wallet():
    """Генерирует новый кошелек и возвращает seed-фразу, приватный ключ и адрес."""
    account, mnemonic = Account.create_with_mnemonic()
    private_key = account._private_key.hex()
    address = account.address
    return mnemonic, private_key, address

def save_to_file(filename, content):
    """Добавляет содержимое в файл с новой строки."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content + "\n")

def generate_wallets(num_wallets, log_text):
    """Генерирует кошельки и логирует в GUI."""
    output_dir = "wallets"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    seed_file = os.path.join(output_dir, "seed_phrases.txt")
    private_key_file = os.path.join(output_dir, "private_keys.txt")
    address_file = os.path.join(output_dir, "addresses.txt")

    # Очищаем файлы, если они уже существуют
    for file in [seed_file, private_key_file, address_file]:
        if os.path.exists(file):
            os.remove(file)

    log_text.insert(tk.END, f"Начинаем создание {num_wallets} кошельков...\n")
    log_text.see(tk.END)

    for i in range(num_wallets):
        mnemonic, private_key, address = create_wallet()

        save_to_file(seed_file, mnemonic)
        save_to_file(private_key_file, private_key)
        save_to_file(address_file, address)

        log_text.insert(tk.END, f"Кошелек {i + 1} создан:\n")
        log_text.insert(tk.END, f"Seed-фраза: {mnemonic}\n")
        log_text.insert(tk.END, f"Приватный ключ: {private_key}\n")
        log_text.insert(tk.END, f"Адрес: {address}\n")
        log_text.insert(tk.END, f"Данные добавлены в файлы в папке: {output_dir}\n\n")
        log_text.see(tk.END)

    log_text.insert(tk.END, f"Готово! Все кошельки сохранены в {output_dir}\n")
    messagebox.showinfo("Готово", f"Создано {num_wallets} кошельков. Проверьте папку {output_dir}.")

def start_generation():
    """Обработчик кнопки 'Старт'."""
    try:
        num_wallets = int(entry.get())
        if num_wallets <= 0:
            messagebox.showerror("Ошибка", "Количество кошельков должно быть больше 0.")
            return
        generate_wallets(num_wallets, log_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число.")

def open_wallets_folder():
    """Обработчик кнопки 'Открыть папку wallets'."""
    output_dir = "wallets"
    if not os.path.exists(output_dir):
        messagebox.showwarning("Предупреждение", "Папка wallets не существует. Сгенерируйте кошельки сначала.")
        return
    try:
        # Выбираем подходящий файловый менеджер в зависимости от ОС
        if sys.platform.startswith('win'):
            subprocess.Popen(['explorer', output_dir])
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', output_dir])
        else:
            subprocess.Popen(['thunar', output_dir])  # Для Linux, замените на ваш проводник, если нужно
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Не удалось открыть папку. Проверьте, установлен ли файловый менеджер (например, thunar).")

# Создание основного GUI
root = tk.Tk()
root.title("Генератор EVM Кошельков", )
root.geometry("600x500")

# Инструкция
instruction_label = tk.Label(root, text="Генератор EVM кошельков:\n1. Введите количество кошельков (целое число > 0).\n2. Нажмите 'Старт' для генерации.\n3. Проверьте логи ниже и папку 'wallets'.\n\nВнимание: Сохраняйте seed-фразы и ключи в секрете!\nВАЖНО: При повторном запуске скрипта всё содержимое файлов будет УДАЛЕННО", justify=tk.LEFT)
instruction_label.pack(pady=10)

# Строка ввода
entry_label = tk.Label(root, text="Количество кошельков:")
entry_label.pack()
entry = tk.Entry(root, width=10)
entry.pack(pady=5)
entry.insert(0, "1")  # Значение по умолчанию

# Кнопки
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Старт", command=start_generation, bg="green", fg="white")
start_button.pack(side=tk.LEFT, padx=5)

open_button = tk.Button(button_frame, text="Открыть папку wallets", command=open_wallets_folder, bg="blue", fg="white")
open_button.pack(side=tk.LEFT, padx=5)

# Лог-окно (scrolled text для вывода результатов)
log_label = tk.Label(root, text="Лог генерации:")
log_label.pack(anchor=tk.W)
log_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
log_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()