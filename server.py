import socket
import pyautogui

# Define the server address and port
SERVER_HOST_NAME = socket.gethostname()
IP_ADDRESS = socket.gethostbyname(SERVER_HOST_NAME)
SERVER_PORT = 52000

def handle_client(conn):
    with conn:
        print("Client connected")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received command: {data}")

            # Process keyboard and mouse commands
            if data.startswith("move "):  # Move the mouse
                _, x, y = data.split()
                pyautogui.moveTo(int(x), int(y))
            elif data.startswith("click"):  # Left-click
                pyautogui.click()
            elif data.startswith("right_click"):  # Right-click
                pyautogui.rightClick()
            elif data.startswith("type "):  # Type a character
                char = data[5:]
                pyautogui.write(char)
            elif data.startswith("press "):  # Press a key
                key = data[6:]
                pyautogui.press(key)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((IP_ADDRESS, SERVER_PORT))
        server_socket.listen()
        print(f"Server listening on {IP_ADDRESS}:{SERVER_PORT}")
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            handle_client(conn)

if __name__ == "__main__":
    main()
