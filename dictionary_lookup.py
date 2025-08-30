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