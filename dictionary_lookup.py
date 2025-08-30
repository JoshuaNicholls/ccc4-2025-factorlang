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

number_dict = {
    "1": "Numerical",
    "2": "Null",
    "3": "Singular",
    "5": "Dual",
    "7": "Trial",
    "11": "Quartal",
    "13": "Quintal",
    # … etc.
    "-1": "Anumerical",
    "-2": "Plural",
    "-3": "Collective",
    "-5": "Paucal",
    "-7": "Infinitive",
    "-11": "Greater Paucal",
    "-13": "Greater Plural"
}

aspect_dict = {
    "1": "Aspect Finite",
    "2": "Simple",
    "3": "Progressive",
    "5": "Gnomic",
    "7": "Perfect",
    "11": "Infinitive",
    "13": "Cyclical"
}

participle_dict = {
    "1": "Finite",
    "2": "?",
    "-1": "Participle",
    "-2": "Agent Particuple"
}

music_dict = {
    "1": "?",
    "2": "?",
    "-1": "?",
    "-2": "?"
}

dance_dict = {
    "1": "?",
    "2": "?",
    "-1": "?",
    "-2": "?"
}

size_dict = {
    "1": "Small Size",
    "2": "Indefinite",
    "3": "Seed",
    "5": "Pinky knuckle",
    "7": "Pinky",
    "11": "Tennis Ball",
    "13": "Handspan",
    "17": "Lower Leg",
    "19": "Half Humanoid",
    "-1": "Larger than Humanoid",
    "-2": "Humanoid",
    "-3": "1.5x Humanoid",
    "-5": "3x Humanoid",
    "-7": "Cathedral Interior",
    "-11": "City",
    "-13": "Colossal",
    "-17": "Planet",
    "-19": "Infinite"
}

shape_dict = {
    "1": "Geometric Shape",
    "2": "Undefined",
    "3": "Line",
    "5": "Circular",
    "7": "Square",
    "11": "Triangle",
    "13": "Semicircle",
    "17": "Spherical",
    "19": "Cylindrical",
    "23": "Cuboid",
    "29": "Tetrahedral",
    "-1": "Non-Geometric Shape",
    "-2": "Unknown",
    "-3": "Ovoid",
    "-5": "Geoid",
    "-7": "Kiki",
    "-11": "Bouba",
    "-13": "Grainy",
    "-17": "Fuzzy",
    "-19": "Mammal"
}

person_number_dict = {
    "1": "Numeropersonal",
    "2": "1st Singular",
    "3": "2nd Singular",
    "5": "3rd Singular",
    "7": "4th Singular",
    "11": "1st Plural",
    "13": "2nd Plural",
    "17": "3rd Plural",
    "19": "4th Plural",
    "23": "1st Dual",
    "29": "2nd Dual",
    "31": "3rd Dual",
    "37": "4th Dual",
    "41": "1st Collective",
    "43": "2nd Collective",
    "47": "3rd Collective",
    "53": "4th Collective",
    "59": "1st Paucal",
    "61": "2nd Paucal",
    "67": "3rd Paucal",
    "71": "4th Paucal",
    "73": "1st Trial",
    "79": "2nd Trial",
    "83": "3rd Trial",
    "89": "4th Trial",
    "93": "1st Infinite",
    "101": "2nd Infinite",
    "103": "3rd Infinite",
    "107": "4th Infinite",
    # + Greater Paucal / Greater Plural / Quartal placeholders here
    "-1": "Numeroapersonal",
    "-2": "Demonstrative Singular",
    "-3": "Interrogative Singular",
    "-5": "Relative Singular",
    "-7": "Demonstrative Plural",
    "-11": "Interrogative Plural",
    "-13": "Relative Plural",
    "-17": "Demonstrative Dual",
    # … etc.
}

element_dict = {
    "1": "Terrestrial Element",
    "2": "Metal",
    "3": "Wood",
    "5": "Earth",
    "7": "Flesh",
    "11": "Water",
    "-1": "Extra-Terrestrial Element",
    "-2": "Fire",
    "-3": "Air",
    "-5": "Spirit",
    "-7": "Dark Matter",
    "-11": "Aether"
}

cardinality_dict = {
    "1": "Non-Cardinals",
    "2": "Fixed",
    "3": "Mutable",
    "-1": "Cardinals",
    "-2": "Spacially Cardinal",
    "-3": "Temporally Cardinal"
}

voice_dict = {
    "1": "Positive Voice",
    "2": "Active",
    "3": "Passive",
    "5": "Mediopassive",
    "-1": "Negative Voice",
    "-2": "Negative Active",
    "-3": "Negative Passive",
    "-5": "Negative Mediopassive"
}

transitivity_dict = {
    "1": "Transitivity",
    "2": "Causative",
    "-1": "",
    "-2": ""
}

animacy_dict = {
    "1": "Animate (Living)",
    "2": "Non-cellular life",
    "3": "Prokaryote",
    "5": "Unicellular Eukaryote",
    "7": "Microscopic Fungus",
    "11": "Microscopic Plant",
    "13": "Macroscopic Plant",
    "17": "Macroscopic Fungus",
    "19": "Microscopic Animal",
    "23": "Low Animal",
    "29": "Mid Animal",
    "31": "High Animal",
    "37": "Near Sapient Animal",
    "41": "Low Sapient",
    "43": "High Spaient",
    "47": "Enlightened Sapient",
    "53": "Low Destroyer",
    "59": "Low Creator",
    "61": "High Destroyer",
    "67": "High Creator",
    "-1": "Inanimate (Non-living)",
    "-2": "Concept",
    "-3": "Subatomic particle",
    "-5": "Atom",
    "-7": "Compound",
    "-11": "Natural Inanimate",
    "-13": "Sapient-made Inanimate",
    "-17": "Dead organic matter",
    "-19": "Part of a living being",
    "-23": "Animate natural phenomenon",
    "-29": "Speech",
    "-31": "Planet",
    "-37": "Star",
    "-41": "Nebula",
    "-43": "Galaxy",
    "-47": "Universe"
}

animal_type_high_dict = {
    "1": "Medium Animal",
    "2": "Beast",
    "3": "Fish",
    "5": "Small Reptile",
    "-1": "",
    "-2": "",
    "-3": "",
    "-5": ""
}

animal_small_reptile_dict = {
    "1": "",
    "2": "Serpent",
    "3": "Tortoise",
    "5": "",
    "-1": "",
    "-2": "",
    "-3": "",
    "-5": ""
}

mood_dict = {
    "1": "Realis",
    "2": "Indicative",
    "3": "Imperative",
    "5": "Necessative",
    "7": "Declarative",
    "11": "Admonitive",
    "-1": "Irrealis",
    "-2": "Optative",
    "-3": "Subjunctive",
    "-5": "Conditional",
    "-7": "Presumptive",
    "-13": "Contrafactual"
}

evidentiality_dict = {
    "1": "Sure source",
    "2": "Did i' meself",
    "3": "(Visual) Saw i' wiv me own oies, oi did",
    "5": "(Auditory) 'Eard i' wiv me own eas, oi did",
    "7": "(Touch / ESP) Few' i' fa sure",
    "11": "(Olfactogustatory) Smew' / tighsted i'",
    "13": "Was jus' roun' t' corner when i' 'appened",
    "17": "Trus'worvy frien' tol' me",
    "19": "Reasonably reloiable source",
    "-1": "Unsure source",
    "-2": "Figured i' ou' based on wha' oi've seen",
    "-3": "Sloightly sketchy source",
    "-5": "Wouldn' trus' as far 's a could frow 'em",
    "-7": "Guaran'ee vis did no' 'appen"
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