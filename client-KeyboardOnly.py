import socket
from pynput import keyboard, mouse
import pyautogui

# Configure client
SERVER_IP = '172.23.212.107'  # Replace with the server's IP address
PORT = 52000

def send_command(sock, command):
    try:
        sock.sendall(command.encode())
        print(f"Sent command: {command}")
    except socket.error as e:
        print(f"Error sending command: {e}")
        sock.close()

# Capture keyboard events with suppression
def on_key_press(key):
    try:
        send_command(client_socket, f"type {key.char}")
    except AttributeError:
        send_command(client_socket, f"press {key}")
    return False  # Suppresses the key press event locally

def on_key_release(key):
    return False  # Suppresses the key release event locally

# Main function to set up a persistent connection
def main():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print("Connected to the server")

    # Start suppressing and capturing keyboard and mouse events
    while True:
        with keyboard.Listener(on_press=on_key_press, on_release=on_key_release, suppress=True) as key_listener:
            key_listener.join()

if __name__ == "__main__":
    main()
