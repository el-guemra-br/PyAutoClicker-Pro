![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat)

# PyAutoClicker Pro Modern

**PyAutoClicker Pro Modern** is a powerful, user-friendly auto-clicker with a modern dark GUI and intelligent mouse movement detection. Perfect for automating repetitive clicking tasks with precision and safety.

## Two Versions Available

### 🎨 AutoClicker Pro Modern (Recommended)
Modern dark interface with intuitive controls, perfect for both beginners and advanced users.

### ⚙️ AutoClicker Pro (Original CLI)
Original command-line version for users who prefer terminal-based setup.

---

## Features

✨ **Modern Dark GUI** – Professional interface with intuitive controls  
🎯 **Smart Mouse Pause** – Automatically pauses when you move the cursor  
⏱️ **Customizable Settings** – Adjust delay, interval, hold duration, and more  
🖱️ **Multiple Mouse Buttons** – Support for left, right, and middle clicks  
⌨️ **Global Hotkeys** – Shift+P to pause/resume, Esc to stop  
📊 **Live Status Display** – Real-time click counter and runtime tracking  
🎨 **Dark Theme** – Beautiful, modern UI design  
🔗 **Social Links** – Quick access to creator's GitHub and Instagram profiles  

---

## Installation

### Option 1: Easy Setup (Recommended for Non-Programmers)

1. **Download** Python from [python.org](https://www.python.org/) (Python 3.8+)
   - During installation, check **"Add Python to PATH"**

2. **Navigate** to the project folder

3. **Double-click** `setup.bat` and wait for completion

4. **Double-click** `run.bat` to launch the app

Done! The setup automatically installs all required packages.

### Option 2: Manual Installation

If you prefer to install manually:

```bash
pip install pyautogui keyboard Pillow
```

Then run:
```bash
python "AutoClicker Pro Modern.py"
```

---

## Usage

### Launching the Application

**Easy Method:** Double-click `run.bat`

**Manual Method:** 
```bash
python "AutoClicker Pro Modern.py"
```

### Configuring Settings

Before clicking **Start**, adjust these options:

- **Start Delay (s)** – Seconds to wait before clicking begins (default: 3)
- **Interval (ms)** – Delay between clicks in milliseconds (default: 120)
- **Hold Duration (ms)** – How long to hold the mouse button down (default: 15)
- **Max Clicks** – Maximum number of clicks (0 = infinite)
- **Mouse Button** – Choose left, right, or middle click
- **Smart Pause While Cursor Is Moving** – Auto-pause when you move the mouse (enabled by default)
  - **Settle Delay (ms)** – Time to wait after mouse stops before resuming (default: 250)

### Running the Clicker

1. Configure your preferred settings
2. Click **Start**
3. Wait for the countdown (default 3 seconds)
4. Clicking begins automatically
5. Use **Pause** to temporarily stop (counter stays the same)
6. Use **Resume** to continue from where you paused
7. Use **Stop** to end the session

### Keyboard Shortcuts

- **Shift + P** – Pause/Resume clicking
- **Esc** – Stop immediately
- **Move mouse to screen corner** – PyAutoGUI failsafe (emergency stop)

---

## Safety & Important Notes

⚠️ **Always test with small values first** (low interval, low max clicks)

✅ Move your mouse to the **screen corner** as an emergency failsafe  
✅ Use **Smart Pause** to prevent clicks when you move the mouse  
✅ Keep **Alt+F4** ready to force-close if needed  
✅ Don't use on critical applications without testing first  
✅ Running this script may require administrator privileges, especially on Windows

---

## Troubleshooting

### "Python is not installed or not in PATH"
→ Reinstall Python and ensure you check "Add Python to PATH"

### "Failed to install packages"
→ Try running setup.bat again or manually run:
```bash
python -m pip install --upgrade pip
python -m pip install pyautogui keyboard Pillow
```

### Window doesn't appear
→ Try running setup.bat again to ensure all dependencies are installed

### Icons show as GH/IG text
→ This is normal! The app still works perfectly. SVG icons are optional.

---

## Creator Info

Made by **el-guemra-br**

- GitHub: https://github.com/el-guemra-br
- Instagram: https://instagram.com/el_guemra_br

Follow the social links in the app header to connect!

---

## Requirements

- Python 3.8 or higher
- Windows 7+, macOS, or Linux
- All dependencies installed automatically by setup.bat

---

## License & Disclaimer

Use responsibly. This tool is for automation in legitimate scenarios only.  
The creator is not responsible for misuse of this software.

---

## Visitor Counter

<p align="center">
  <img src="https://github.com/el-guemra-br.png" alt="Creator" width="130" />
  <br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=el-guemra-br.PyAutoClicker-Pro&" />
  <br>
  <sub>
    Thank you for stopping by! Your visit is appreciated. 
  </sub>
</p>

Enjoy! 🚀
