import time
import random

# Sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is an amazing programming language",
    "Artificial Intelligence is the future",
    "Typing speed tests are fun and challenging",
    "Keep practicing to improve your typing skills"
]

def typing_test():
    # Pick a random sentence
    sentence = random.choice(sentences)
    print("\nType this sentence:")
    print(f"➡ {sentence}\n")

    input("Press Enter when you are ready...")

    # Start timer
    start_time = time.time()
    typed_text = input("\nStart typing: ")
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time

    # Calculate Words Per Minute (WPM)
    words = len(sentence.split())
    wpm = (words / time_taken) * 60

    # Calculate accuracy
    correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(sentence) and c == sentence[i])
    accuracy = (correct_chars / len(sentence)) * 100

    print("\n--- Results ---")
    print(f"Time taken: {round(time_taken, 2)} seconds")
    print(f"Speed: {round(wpm, 2)} WPM")
    print(f"Accuracy: {round(accuracy, 2)}%")

# Run the typing test
typing_test()
