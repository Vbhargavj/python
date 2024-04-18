import pyautogui as pg
import time

# Introduce a delay of 3 seconds
time.sleep(3)
search_terms = [
    "BHARGAV VADUKAR IG",
    "virat kohli",
    "rohit sharma",
    "bhargfav meaning",
    "Genetic algorithms",
    "Neural networks",
    "Cryptocurrency",
    "Network security",
    "Operating systems",
    "Python programming",
    "Machine learning", "Web development",
    "Data science",
    "Artificial intelligence",
    "Computer vision",
    "Natural language processing",
    "Deep learning",
    "OpenAI GPT",
    "Robotics",
    "Cybersecurity",
    "Internet of Things",
    "Blockchain technology",
    "Cloud computing",
    "Software development",
    "Augmented reality",
    "Virtual reality",
    "Quantum computing",
    "Human-computer interaction",
    "UX/UI design",
    "Mobile app development",
    "Game development",
    "Data visualization",
    "Bioinformatics",
    #     "Computer graphics",
    # "apple", "banana", "orange", "grape", "pineapple",
    # "strawberry", "watermelon", "kiwi", "blueberry", "mango",
    # "peach", "pear", "plum", "lemon", "lime",
    # "cherry", "apricot", "coconut", "fig", "papaya",
    # "raspberry", "blackberry", "cranberry", "melon", "dragonfruit",
    # "avocado", "guava", "nectarine", "tangerine", "persimmon",
    
    "keyboard",
    "sunset",
    "jazz",
    "mountain",
    "ocean",
    "banana",
    "cathedral",
    "guitar",
    "butterfly",
    # "piano",
    # "coffee",
    # "moonlight",
    # "waterfall",
    # "tiger",
    # "candle",
    # "fireworks",
    # "sandcastle",
    # "whale",
    # "carousel",
    # "rainbow",
    # "volcano",
    # "cactus",
    # "zebra",
    # "crystal",
    # "squirrel",
    # "dragonfly",
    # "jellyfish",
    # "lighthouse"
    ]# Press and release the Ctrl and T keys simultaneously
for iem in search_terms:
    time.sleep(2)
    pg.hotkey('ctrl', 't')
    time.sleep(1)
    pg.write(iem)
    time.sleep(0)
    pg.hotkey('enter')
    time.sleep(3)
    pg.hotkey('ctrl', 'w')
    
