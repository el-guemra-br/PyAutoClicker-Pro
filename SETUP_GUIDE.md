# PyAutoClicker Pro Modern

A modern, easy-to-use auto-clicker application with a beautiful GUI and smart mouse movement detection.

## Features

✨ **Modern Dark GUI** – Professional interface with intuitive controls  
🎯 **Smart Mouse Pause** – Automatically pauses when you move the cursor  
⏱️ **Customizable Settings** – Adjust delay, interval, hold duration, and more  
🖱️ **Multiple Mouse Buttons** – Support for left, right, and middle clicks  
⌨️ **Global Hotkeys** – Shift+P to pause/resume, Esc to stop  
🎨 **Live Status Display** – Real-time click counter and runtime tracking  
🔗 **Social Links** – Quick access to creator's GitHub and Instagram  

## Quick Start for Non-Programmers

### Step 1: Install Python (First Time Only)

1. Go to https://www.python.org/downloads/
2. Download **Python 3.8+** (Windows installer)
3. Run the installer
4. **IMPORTANT**: Check the box that says "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

### Step 2: Set Up Dependencies (First Time Only)

1. In the project folder, **double-click `setup.bat`**
2. A command window will open and install all required packages automatically
3. Wait for it to complete (might take 1-2 minutes)
4. Press any key when it says "Setup Complete!"

### Step 3: Run the Application

Simply **double-click `run.bat`** to launch the app anytime!

---

## Usage Guide

### Before Starting

Configure these settings:

- **Start Delay (s)** – Seconds to wait before clicking starts (default: 3)
- **Interval (ms)** – Delay between clicks in milliseconds (default: 120)
- **Hold Duration (ms)** – How long to hold the mouse button down (default: 15)
- **Max Clicks** – Maximum number of clicks (0 = infinite)
- **Mouse Button** – Choose left, right, or middle click
- **Smart Pause While Cursor Is Moving** – Auto-pause when you move the mouse (enabled by default)
  - **Settle Delay (ms)** – Time to wait after mouse stops before resuming clicks

### Running

1. Configure settings
2. Click **Start**
3. Wait for countdown (default 3 seconds) – move away if you're careful!
4. Clicking begins automatically
5. Use **Pause** to temporarily stop without resetting counter
6. Use **Resume** to continue from where you paused
7. Use **Stop** to end the session

### Keyboard Shortcuts

- **Shift + P** – Pause/Resume
- **Esc** – Stop immediately
- **Move mouse to top-left corner** – PyAutoGUI failsafe (stops execution)

---

## Troubleshooting

### "Python is not installed or not in PATH"
- **Solution**: Reinstall Python and make sure to check "Add Python to PATH"

### "Failed to install packages"
- **Solution**: Open Command Prompt and run:
  ```
  python -m pip install --upgrade pip
  python -m pip install pyautogui keyboard Pillow cairosvg
  ```

### Window doesn't appear
- **Solution**: Make sure the command window doesn't close. If it does, try running setup.bat again.

### Icons don't show (shows GH/IG text instead)
- **Solution**: This is normal! The app still works perfectly. If you want icons, make sure Pillow and cairosvg were installed (check setup completed successfully).

---

## Safety Tips

⚠️ **Always test with a small max-clicks value first!**

✅ Move your mouse to the **top-left corner of the screen** as an emergency stop (PyAutoGUI failsafe)  
✅ Use **Smart Pause** feature to prevent unwanted clicks when you move the mouse  
✅ Start with low interval values (100-200ms) to test behavior  
✅ Always have Alt+F4 ready to close the window if needed  

---

## Creator

Made by **el-guemra-br**

- GitHub: https://github.com/el-guemra-br
- Instagram: https://instagram.com/el_guemra_br

---

## Requirements

- Python 3.8 or higher
- Windows 7 or later (also works on macOS and Linux)

All dependencies are installed automatically by setup.bat!

---

## Notes

- The Smart Pause feature monitors your cursor in real-time and will pause clicking if you move it
- If your cursor settles after movement, clicking resumes after the settle delay (default 250ms)
- The application respects the PyAutoGUI failsafe – move to the screen corner to emergency stop
- All settings can be adjusted before starting; they're locked while the clicker is running

---

Enjoy! 🚀
