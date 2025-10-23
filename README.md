# EVM Wallet Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to the **EVM Wallet Generator**! This is a user-friendly tool with a graphical user interface (GUI) designed to generate wallets compatible with the Ethereum Virtual Machine (EVM). The program creates seed phrases, private keys, and addresses, saving them to files in the `wallets` directory.

## Features
- Generate any number of EVM-compatible wallets.
- Save seed phrases, private keys, and addresses to separate text files.
- Intuitive GUI built with `tkinter`.
- Real-time logging of the generation process.
- Cross-platform support (Windows, macOS, Linux).
- Automatic installation of required libraries.

## Requirements
- **Python**: Version 3.8 or higher.
- **Operating System**: Windows, macOS, or Linux.
- **Dependencies**:
  - `tkinter` (usually included with Python, but may require manual installation on Linux).
  - `eth_account` (automatically installed on first run).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Grobofhik/multi-creator-EVM-wallets.git
   cd multi-creator-EVM-wallets
   python -m venv .venv
   source .venv/bin/activate

## Usage

1. **Run the program:**
    ```bash
    python3 main.py

#### Then:
1. Enter the number of  wallets to generate (e.g., `10`)
2. Click **Start**
3. Watch the long in real-time
4. Check the generated files inside the `wallets/` folder

⚠️ **Important:** Every new launch overwrites the existing files.

# Output Example
### After generation, your project dirictory will include:
```
    wallets/
    ├── seed_phase.txt
    ├── private_keys.txt
    ├── addresses.txt
```
### Each file contains one line per wallet 

## ⚙️ Customization

### By default, the file explorer used on Linux is **Thunar**.
 If you use a different one (like Nautilus, Dolphin, etc.), update this line in the script
```python
    subprocess.Popen(['thunar', output_dir])
```
Replace `Thunar` with your preferred file manager, e.g.:
```
    subprocess.Popen(['nautilus', output_dir])
```

# Author
### **Created by:** Grobofhik
### **GitHub:** @grobofhik


# Licence

### This project is licensed under the **MIT Licence.**
### You are free to use, modify, and distribute if for personal or educational use.

# Support
### If you find this tool useful — consider giving it a ⭐ on GitHub!
