import pyautogui
import numpy as np
from PIL import Image
import keyboard
import time

# Constants
GAME_REGION = (0, 0, 800, 600)  # Region (left, top, width, height) of the game area
OBSTACLE_COLOR = (83, 83, 83)  # RGB color of obstacles
JUMP_THRESHOLD = 100  # Brightness threshold for detecting obstacles
REFRESH_RATE = 0.05  # Frequency of screen capture and processing

def capture_screen(region):                  
    """Capture a screenshot of the specified region."""                                 
    screenshot = pyautogui.screenshot(region=region)
    return np.array(screenshot)

def detect_obstacle(image, color_threshold):
    """Detect if there is an obstacle based on the color threshold."""
    # Convert image to grayscale
    grayscale_image = np.mean(image, axis=2)
    # Apply threshold to detect obstacles
    threshold_image = grayscale_image < color_threshold
    # Check for significant dark areas indicating obstacles
    return np.any(threshold_image)

def main():
    """Main function to automate the T-Rex game."""
    print("Starting the T-Rex game automation...")
    time.sleep(5)  # Time to switch to the game window

    try:
        while True:
            screen = capture_screen(GAME_REGION)
            if detect_obstacle(screen, JUMP_THRESHOLD):
                keyboard.press_and_release('space')
                print("Obstacle detected! Jumping...")
            time.sleep(REFRESH_RATE)
    except KeyboardInterrupt:
        print("Automation stopped by user.")

if __name__ == "__main__":
    main()
