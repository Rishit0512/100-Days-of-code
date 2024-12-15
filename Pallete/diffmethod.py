from PIL import Image
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def extract_colors(image_path, num_colors=10):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to RGB mode (in case it's not)
    img = img.convert('RGB')
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Reshape the array to be a list of RGB tuples
    pixels = img_array.reshape(-1, 3)
    
    # Count the occurrences of each color
    color_counts = Counter(map(tuple, pixels))
    
    # Get the most common colors
    most_common_colors = color_counts.most_common(num_colors)
    
    return most_common_colors

def plot_colors(colors):
    # Create a figure
    plt.figure(figsize=(10, 2))
    
    # Plot each color as a bar
    for i, (color, count) in enumerate(colors):
        plt.bar(i, 1, color=np.array(color) / 255.0)
    
    plt.xticks([])
    plt.yticks([])
    plt.title('Most Common Colors')
    plt.show()

if __name__ == "__main__":
    image_path = 'pic.jpg'  # Update this path to your image file
    num_colors = 10  # Number of colors to extract

    common_colors = extract_colors(image_path, num_colors)
    plot_colors(common_colors)
