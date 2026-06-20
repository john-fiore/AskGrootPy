import os
import sys
import random as ran
import time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
thinking_time = ran.randint(3, 7)

def ask_groot(q: str):
    clear()
    print(f"YOU: {q}")
    print()
    print("Groot is thinking...")
    time.sleep(thinking_time)
    
    clear()
    print("GROOT: I am Groot!")
    print()
    post = input("Would you like to ask another question? (Y/N): ").upper()
    
    if (post == "Y"):
        main()
    else:
        sys.exit(0)

def main():
    clear()
    print("Welcome to AskGroot.")
    print()
    question = input("Enter your question: ")
    ask_groot(question)

if __name__ == "__main__":
    main()