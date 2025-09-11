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
    "5": "Size",
    "7": "Element",
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
    "0": "Shape",
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
    "0": "Cardinality",
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
    "0": "Transitivity",
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

high_animal_dict = {
    "1": "High Animal",
    "2": "Beast",
    "3": "Dog",
    "5": "Small Reptile",
    "-1": "",
    "-2": "",
    "-3": "",
    "-5": ""
}

small_reptile_dict = {
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
    "0": "Evidentiality",
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

# Gender (Cat + num)
gender_dict = {
    "0": "Gender Mod",
    "1": "Agender",
    "2": "Female ~ Gender",
    "3": "Male ~ Gendersquared",
    "5": "Third ~ Thirdgender",
    "7": "Twothirds ~ Twothirdsgender",
    "11": "Quarter ~ Quartergender",
    "13": "Threequarters ~ Threequartersgender",
    "17": "Fifth ~ Fifthgender",
    "19": "Twofifths ~ Twofifthsgender",
    "-1": "Omnigender - Genderinfinity",
    "-2": "Female / Male Bigender",
    "-3": "Female / Third Bigender",
    "-5": "Female / Twothirds Bigender",
    "-7": "Third / Twothirds Bigender",
    "-11": "Female / Third / Twothirds Trigender",
    "-13": "Female / Quarter Bigender",
    "-17": "Female / Threequarters Bigender",
    "-19": "Male / Quarter Bigender",
    "-23": "Male / Threequarters Bigender",
    "-29": "Quarter / Threequarters Bigender",
    "-31": "Female / Male / Quarter Trigender",
    "-37": "Female / Male / Threequarters Trigender",
    "-41": "Female / Quarter / Threequarters Trigender",
    "-43": "Male / Quarter / Threequarters Trigender",
    "-47": "Female / Male / Quarter / Threequarters Tetragender"
    # ...etc.
}

# Gender (Cat + num modifiers)
gender_mod_dict = {
    "0": "Agender",
    "1": "-",
    "2": "Hyper-",
    "-2": "Demi-"
}

# Flavour
flavour_dict = {
    "1": "Flavour",
    "2": "Salty",
    "3": "Sour",
    "5": "Bitter",
    "7": "Sweet",
    "11": "Savoury",
    "13": "Radioactive",
    "-1": "?",
    "-2": "?"
}

# Person
person_dict = {
    "1": "Personal",
    "2": "1st",
    "3": "2nd",
    "5": "3rd",
    "7": "4th",
    "-1": "Non-personal",
    "-2": "Demonstrative",
    "-3": "Interrogative",
    "-5": "Relative"
    # ...etc.
}

# To be
to_be_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Consumption
consumption_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To consume
to_consume_dict = {
    "1": "Consume",
    "2": "Eat",
    "3": "Devour",
    "-1": "",
    "-2": ""
}

# Destruction
destruction_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To destroy
to_destroy_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Product / creation
product_creation_dict = {
    "1": "",
    "2": "creation",
    "3": "creator",
    "-1": "",
    "-2": ""
}

# To produce / create
to_produce_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# A being / living thing / essence
being_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To be alive / have essence
to_be_alive_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Object / possession
object_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To have
to_have_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Good
good_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To like
to_like_dict = {
    "1": "like",
    "2": "love",
    "-1": "dislike",
    "-2": "hate"
}

# Sensation / observation
sensation_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To sense / observe
to_sense_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Feeling / emotion
feeling_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To feel / have emotion
to_feel_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Attractiveness
attractiveness_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To attract / repel
to_attract_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# Physical properties
physical_props_dict = {
    "1": "Property",
    "2": "Quantity",
    "3": "Mass",
    "5": "Time",
    "7": "Length",
    "11": "Temperature",
    "13": "Current",
    "17": "Luminosity",
    "-1": "",
    "-2": "Antimass"
}

# Rule / ruler
rule_dict = {
    "1": "rule",
    "2": "rule / reign",
    "3": "majesty",
    "-1": "",
    "-2": ""
}

# To rule
to_rule_dict = {
    "1": "to rule",
    "2": "to rule",
    "3": "to have ruling qualities",
    "-1": "",
    "-2": ""
}

# Combination
combination_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To combine
to_combine_dict = {
    "1": "",
    "2": "to combine 2 things",
    "3": "to assimilate something into a whole",
    "-1": "",
    "-2": ""
}

# Covering / concealment
covering_dict = {
    "1": "",
    "2": "covered",
    "3": "covering / coverer",
    "-1": "uncovered / revealed",
    "-2": "uncovering / revealer"
}

# To cover / conceal
to_cover_dict = {
    "1": "",
    "2": "",
    "3": "",
    "-1": "",
    "-2": ""
}

# Distortion / bending
distortion_dict = {
    "1": "",
    "2": "",
    "-1": "",
    "-2": ""
}

# To bend / distort
to_bend_dict = {
    "1": "to bend",
    "2": "to distort",
    "-1": "",
    "-2": ""
}

# Travel / movement
travel_dict = {
    "1": "movement",
    "2": "travel",
    "3": "transport",
    "-1": "",
    "-2": ""
}

# To move / transport
to_move_dict = {
    "1": "to move",
    "2": "to travel",
    "3": "to transport",
    "-1": "",
    "-2": ""
}

replacement_key_dict = {
    "Pronoun" : "Person",
    "Adjectival": "Case",
    "Genitive": "Case",
    "Partitive": "Case"
}

def print_dict_options(d):
    """Pretty-print dictionary options"""
    for key, value in d.items():
        print(f"{key}: {value}")
        
def to_dict_name(dict_part):
    for key, value in replacement_key_dict.items():
        print(f"DEBUG: dict_part = {dict_part}, key = {key}, value = {value}")
        replaced = dict_part.replace(str(key), str(value))
        # replaced = dict_part.replace("Adjectival", "Case")
    print(f"DEBUG: replaced = {replaced}")
    underscore = replaced.replace(" ", "_")
    lowered = underscore.lower()
    print(f"DEBUG: lowered = {lowered}")
    return lowered
        
def handle_category(category_name, category_dict, numeric_values, linguistic_properties):
    """
    Generic handler for selecting an item from any category dictionary.
    
    Args:
        category_name (str): Name of the category (e.g., "noun", "verb")
        category_dict (dict): The dictionary of options for this category
        numeric_values (list): List to append the numeric key
        linguistic_properties (list): List to append the chosen property
    """
    if not category_dict:
        print(f"[ERROR] No dictionary available for {category_name}. Returning to previous menu.")
        return
    # print("DEBUG: i'm in")
    
    while True:
        # remove 0 from options list
        removed_zero = category_dict.pop("0", None)
        
        print(f"\nDEBUG: Entered handle_category with {category_name}, dict has {len(category_dict)} items")
        print(f"\nChoose a {category_name}:")
        print_dict_options(category_dict)
        choice = input("Type option (or q to quit): ")
        
        if choice.lower() == "q":
            print(f"Returning from {category_name} menu.")
            return "back"  # go back one level
        
        if choice in category_dict and choice != "0":
            prop = category_dict[choice]
            numeric_values.append(choice)
            linguistic_properties.append(prop)
            print(f"Added {category_name}: {prop} ({choice})")
            
            if removed_zero is not None:
                # if this dict has a higher layer that is not a choosable option, recall the removed 0
                dict_part = removed_zero
            else:
                dict_part = prop
            
            # see if this selection has its own dict
            dict_name = f"{to_dict_name(dict_part)}_dict"
            # print(f"DEBUG: dict_name = {dict_name}")
            next_dict = globals().get(dict_name)
            
            if next_dict:
                # recursive step: 
                result = handle_category(dict_part, next_dict, numeric_values, linguistic_properties)
                if result == "done":
                    # leaf reached → bubble all the way up
                    return "done"
                # if result == "back", stay in this menu and let user continue
            else:
                print(f"No further dictionary found for {prop}. Returning up.")
                return "back"  # go back one level
        
        else:
            print(f"Invalid {category_name} choice. Try again.")

# --- ENTRY POINT ---
numeric_values = []
linguistic_properties = []
category_name = "part of speech"
category_dict = pos_dict

if "pos_dict" not in globals() or not pos_dict:
    print("[FATAL] pos_dict is missing or empty — cannot start.")
else:
    # print(f"DEBUG: About to handle category {category_name}")
    handle_category(category_name, category_dict, numeric_values, linguistic_properties)

print("\nFinal Results:")
print("Numeric values:", numeric_values)
print("Linguistic properties:", linguistic_properties)
