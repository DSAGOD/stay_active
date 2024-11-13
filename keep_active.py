
"""
Created on Wed Nov 13 11:38:35 2024

@author: KishanSingh
"""
import win32api, win32con , time

def click(x, y):
    print("clicked");
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# Get the screen resolution
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)

# Calculate center coordinates
center_x = screen_width // 2
center_y = screen_height // 2

def my_function():
    # Click at the center of the screen
    click(center_x, center_y)

while True:
    my_function()
    time.sleep(1*60)  # Wait 5 seconds before calling again