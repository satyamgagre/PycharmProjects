# Step 1: Importing the required library
from spellchecker import SpellChecker

# Step 2: Creating the spell checker class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected = self.spell.correction(word)
            if corrected != word.lower():
                print(f"Correcting '{word}' to '{corrected}'")
            corrected_words.append(corrected)

        # Step 3: Returning the corrected text
        return ' '.join(corrected_words)

    # Step 4: Running the app
    def run(self):
        print("*** THE RIGHT WRITE *** — YOUR SMART PYTHON SPELL CHECKER!")
        while True:
            text = input("\nEnter the text you want to check (type 'exit' to quit): ")
            if text.lower() == 'exit':
                print("\nTHANK YOU FOR USING THE RIGHT WRITE. CLOSING THE PROGRAM...")
                break
            corrected_text = self.correct_text(text)
            print(f"\nCorrected text: {corrected_text}")

# Run the app
if __name__ == "__main__":
    app = SpellCheckerApp()
    app.run()
