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

# Verb dictionary (prime numbers mapped to categories)
verb_dict = {
    "2": "Agreement",
    "3": "Time / Tense",
    "5": "Aspect / Participle",
    "7": "Negation / Voice / Transitivity",
    "11": "Mood / Evidentiality",
    "13": "Verb Flavour",
    "17": "to be, to identify as, to be equivalent to, [copula]",
    "19": "to consume",
    "23": "to destroy",
    "29": "to produce / create",
    "31": "to be alive, to have essence",
    "37": "to have",
    "41": "to like",
    "43": "to sense, to observe",
    "47": "to feel, to have an emotion",
    "53": "to attract / repel",
    "59": "?",
    "61": "to rule",
    "67": "to combine",
    "71": "to cover / conceal",
    "73": "to distort / bend",
    "79": "to move / to transport"
}

case_dict = {
    "1": "Non-locative cases",
    "2": "Nominative",
    "3": "Accusative",
    "5": "Adjectival",
    "7": "Genitive",
    "11": "Dative",
    "13": "Instrumental",
    "17": "Locative",
    "19": "Vocative",
    "23": "Purposive",
    "29": "Ablative",
    "31": "Semblative",
    "37": "Illative",
    "41": "Partitive",
    "43": "Inessive",
    "47": "Benefactive"
}

tense_dict = {
    "1": "Non-past Tenses",
    "2": "Present",
    "3": "Immediate Future",
    "5": "Hodiernal Future",
    "7": "Crastinal (Future)",
    "11": "Septamanial Future (Couple Weeks)",
    "13": "Annual Future (Couple Years)",
    "17": "Decadinal Future (Couple Decades)",
    "19": "Final Future (End of own lifespan)",
    "23": "Distant Future (Centuries / Millenia)",
    "29": "Eternal Future (End of time)",
    "-1": "Past Tenses",
    "-2": "Immediate Past",
    "-3": "Hodiernal Past",
    "-5": "Hesternal (Past)",
    "-7": "Septamanial Past",
    "-11": "Annual Past (Couple Years)",
    "-13": "Decadinal Past (Couple Decades)",
    "-17": "Final Past (Beginning of own lifespan)",
    "-19": "Distant Past (Centuries / Millenia)",
    "-23": "Eternal Past (Beginning of time)"
}

position_dict = {
    "1": "Right>Left",
    "2": "1st",
    "3": "2nd",
    "5": "3rd",
    "7": "…",
    "-1": "Left>Right",
    "-2": "-1st",
    "-3": "-2nd",
    "-5": "…"
}

phoneme_dict = {
    "1": "?",
    "2": "Consonant",
    "3": "ʔ (vowel separator)",
    "5": "q",
    "7": "ć",
    "11": "t",
    "13": "p",
    "17": "j",
    "19": "d",
    "23": "b",
    "29": "h",
    "31": "x",
    "37": "ś",
    "41": "s",
    "43": "þ",
    "47": "f",
    "53": "xh",
    "59": "g",
    "61": "ź",
    "67": "z",
    "71": "ð",
    "73": "v",
    "79": "ng",
    "83": "ŋ",
    "89": "n",
    "97": "m",
    "101": "r",
    "103": "l",
    "107": "hw",
    "109": "y",
    "-1": "?",
    "-2": "Vowel",
    "-3": "à (consonant separator)",
    "-5": "ā",
    "-7": "ae",
    "-11": "ä",
    "-13": "o",
    "-17": "ö",
    "-19": "e",
    "-23": "ü",
    "-29": "u",
    "-31": "i",
    "-37": "ã",
    "-41": "āe",
    "-43": "â",
    "-47": "oi",
    "-53": "öü",
    "-59": "àu",
    "-61": "ài",
    "-67": "ū",
    "-71": "û",
    "-73": "ī"
}

tone_dict = {
    "1": "Steady tone",
    "2": "High",
    "3": "Low",
    "5": "Mid / None",
    "7": "High-Mid",
    "11": "Low-Mid",
    "-1": "Tone contour",
    "-2": "High-to-Low",
    "-3": "Low-to-High",
    "-5": "High-to-Mid",
    "-7": "Mid-to-Low",
    "-11": "Mid-to-High",
    "-13": "Low-to-Mid"
}

syllabification_dict = {
    "1": "Asyllabic Consonant",
    "2": "Syllabic Consonant",
    "-1": "Aconsonantal Vowel",
    "-2": "Consonantal Vowel"
}

nasalisation_dict = {
    "1": "Oral",
    "2": "Nasal",
    "-1": "?",
    "-2": "?"
}

movement_dict = {
    "1": "?",
    "2": "?",
    "-1": "?",
    "-2": "?"
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

        elif prop == "Verb":
            print("\nChoose a verb root:")
            print_dict_options(verb_dict)
            verb_choice = input("Type option: ")
            if verb_choice in verb_dict:
                verb_prop = verb_dict[verb_choice]
                numeric_values.append(int(verb_choice))
                linguistic_properties.append(verb_prop)
                print(f"Added noun root: {verb_prop} ({verb_choice})")
            else:
                print("Invalid verb choice.")
    else:
        print("Invalid choice. Try again.")

print("\nFinal Results:")
print("Numeric values:", numeric_values)
print("Linguistic properties:", linguistic_properties)