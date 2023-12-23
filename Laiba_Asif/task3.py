#R00201303

def countingCharFreq(sentence):
    sentence = sentence.lower()
    freqOfChar = {}
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Ignore blank spaces
        if char != ' ':
            freqOfChar[char] = freqOfChar.get(char, 0) + 1
    
    return freqOfChar

def main():
    print("Character Frequency Counter")
    print("Enter a sentence (type 'end' to exit):")
    
    freqOfCharuency = {}
    
    while True:
        userInput = input(">>> ")
        if userInput.lower() == 'end':
            print("Goodbye!")
            break
        
        # Update character frequency
        freqOfCharuency.update(countingCharFreq(userInput))

    storedCharacters = sorted(freqOfCharuency.keys())
    
    print("\nCharacter frequencies (excluding spaces):")
    for char in storedCharacters:
        print(f"{char}: {freqOfCharuency[char]}")

    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    notPresent = alphabets - set(freqOfCharuency.keys())
    
    print("\nCharacters that were not input:")
    print(', '.join(notPresent))

if _name_ == "_main_":
    main()
