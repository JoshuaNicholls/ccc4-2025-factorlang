# Dictionaries for mapping part of speech
pos_dict = {
    "1": "Noun",
    "-1": "Verb",
    "1j": "Sound",
    "-1j": "Movement"
}

# Noun dictionary (prime numbers mapped to categories)
noun_dict = {
    "2": "Case",
    "3": "Number",
    "5": "Size / Shape",
    "7": "Sign",
    "11": "Animacy",
    "13": "Gender",
    "17": "Pronoun",
    "19": "Consumption",
    "23": "Destruction",
    "29": "Product / Creation",
    "31": "A being, living thing, essence",
    "37": "Object / Possession",
    "41": "Good, goodness, good thing",
    "43": "Sensation / Observation",
    "47": "Feeling / Emotion",
    "53": "Attractiveness",
    "59": "Physical properties",
    "61": "Rule, subject",
    "67": "Combination",
    "71": "Covering / Concealment",
    "73": "Bending / Distortion",
    "79": "Travel / Movement"
}

# Running lists
numeric_values = []
linguistic_properties = []

def print_dict_options(d):
    """Pretty-print dictionary options"""
    for key, value in d.items():
        print(f"{key}: {value}")

while True:
     # Step 1: Choose part of speech
    print("\nChoose part of speech:")
    print_dict_options(pos_dict)
    choice = input("Type option (or q to quit): ")
    
    if choice.lower() == "q":
        break

    if choice in pos_dict:
        prop = pos_dict[choice]
        numeric_values.append(int(choice))
        linguistic_properties.append(prop)
        print(f"Added: {prop} ({choice})")

        # Step 2: If Noun, prompt for noun root
        if prop == "Noun":
            print("\nChoose a noun root:")
            print_dict_options(noun_dict)
            noun_choice = input("Type option: ")
            if noun_choice in noun_dict:
                noun_prop = noun_dict[noun_choice]
                numeric_values.append(int(noun_choice))
                linguistic_properties.append(noun_prop)
                print(f"Added noun root: {noun_prop} ({noun_choice})")
            else:
                print("Invalid noun choice.")
    else:
        print("Invalid choice. Try again.")

print("\nFinal Results:")
print("Numeric values:", numeric_values)
print("Linguistic properties:", linguistic_properties)