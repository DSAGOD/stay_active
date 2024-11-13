# stay_active
A sneaky little helper to keep your screen looking busy! Just the thing for when you need your computer to look productive... even if you’re ‘researching’ cat videos on your phone.
Here's a fun README description for your code that keeps Microsoft Teams active:

---

# 🖱️ Keep-Active-Script: Never Go AFK Again! 🚀

Ever find yourself needing to stay "active" on Microsoft Teams while you're busy... doing *other things*? 😉 Well, this little Python script is here to help!

## 🤔 What It Does

This script automatically simulates a mouse click at the center of your screen every few seconds. Think of it as your digital doppelgänger, always there to give your boss the peace of mind that you're on top of things! 😌

## 🚀 How It Works

Using a simple, yet effective `win32api` function, the script:
1. Positions the cursor to the center of your screen 🖥️
2. Simulates a left-click to show "activity" ⏱️
3. Repeats every 1 minutes to keep your Teams status green 🔥

⚠️ **Note:** Use responsibly! This is for educational purposes only... or so we say. 😉

## 📜 Requirements

To run this, you'll need the following:
- Python 3.x
- The `pywin32` package for simulating mouse movements and clicks
    ```bash
    pip install pywin32
    ```

## 🛠️ Usage

Just run the script, and it will work quietly in the background, keeping your status "active" for as long as needed.

```python
python keep_active.py
```

**Pro tip:** You might want to add a keyboard interrupt (like `CTRL+C`) to stop it when you're truly AFK!

---

Happy "working" 🥂, and may your Teams status always be green! 😆
