import socket
from pynput import keyboard, mouse
import pyautogui  # Used to hide the mouse off-screen

# Configure client
SERVER_IP = '172.23.212.107'  # Replace with the server's IP address
PORT = 52000
pyautogui.FAILSAFE=False

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        s.sendall(command.encode())
        print(f"Sent command: {command}")

# Capture keyboard events with suppression
def on_key_press(key):
    try:
        send_command(f"type {key.char}")
    except AttributeError:
        send_command(f"press {key}")
    return False  # Suppresses the key press event locally

def on_key_release(key):
    return False  # Suppresses the key release event locally

# Capture mouse events with suppression
def on_move(x, y):
    pyautogui.moveTo(3000, 3000)  # Move mouse cursor off-screen to disable local interaction
    send_command(f"move {x} {y}")
    return False  # Suppresses the move event locally

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            send_command("click")
        elif button == mouse.Button.right:
            send_command("right_click")
    return False  # Suppresses the click event locally

# Start suppressing and capturing keyboard and mouse events
# with keyboard.Listener(on_press=on_key_press, on_release=on_key_release, suppress=True) as key_listener, \
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release, suppress=True) as key_listener:
    #  mouse.Listener(on_move=on_move, on_click=on_click, suppress=True) as mouse_listener:
    pyautogui.moveTo(3000, 3000)  # Move the mouse off-screen to disable client-side control
    key_listener.join()
    # mouse_listener.join()
