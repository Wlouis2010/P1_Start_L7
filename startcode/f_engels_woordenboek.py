woordenboek = {{
    "naam": "name",
    "leeftijd": "age",
    "groen": "green",
    "huis": "house",
    "vriend": "friend",
    "geluk": "happiness",
    "snel": "fast",
    "familie": "family",
    "leraar": "teacher",
    "boek": "book",
    "auto": "car",
    "eten": "food",
    "school": "school",
    "mooi": "beautiful",
    "water": "water",
    "zon": "sun",
    "kat": "cat",
    "hond": "dog",
    "muziek": "music",
    "film": "movie",
    "werk": "work",
    "spel": "game",
    "computer": "computer",
    "telefoon": "phone",
    "straat": "street",
    "taal": "language",
    "zee": "sea",
    "berg": "mountain",
    "boom": "tree",
    "bloem": "flower",
    "brief": "letter",
    "winkel": "shop",
    "vriendin": "girlfriend",
    "broer": "brother",
    "zus": "sister",
    "ouder": "parent",
    "kind": "child",
    "geld": "money",
    "klein": "small",
    "groot": "big",
    "oud": "old",
    "nieuw": "new",
    "hoog": "high",
    "laag": "low",
    "schoon": "clean",
    "vies": "dirty",
    "makkelijk": "easy",
    "moeilijk": "difficult",
    "warm": "warm",
    "koud": "cold",
    "licht": "light",
    "donker": "dark",
    "slaap": "sleep",
    "droom": "dream",
    "nacht": "night",
    "dag": "day",
    "ochtend": "morning",
    "middag": "afternoon",
    "avond": "evening",
    "maand": "month",
    "jaar": "year",
    "week": "week",
    "moment": "moment",
    "uur": "hour",
    "minuut": "minute",
    "seconde": "second",
    "liefde": "love",
    "vrede": "peace",
    "kracht": "strength",
    "woorden": "words",
    "zinnen": "sentences",
    "tafel": "table",
    "stoel": "chair",
    "venster": "window",
    "deur": "door",
    "dak": "roof",
    "vloer": "floor",
    "kamer": "room",
    "keuken": "kitchen",
    "badkamer": "bathroom",
    "slaapkamer": "bedroom",
    "woonkamer": "living room",
    "tuin": "garden",
    "fiets": "bicycle",
    "trein": "train",
    "vliegtuig": "airplane",
    "boot": "boat",
    "bus": "bus",
    "garage": "garage",
    "dorp": "village",
    "regen": "rain",
    "ster": "star",
    "maan": "moon",
    "vuur": "fire",
    "ijs": "ice",
    "lucht": "air",
    "wind": "wind",
    "weekend": "weekend",
    "feest": "party",
    "vakantie": "holiday",
    "reis": "journey",
    "wandeling": "walk",
    "fietstocht": "bike ride",
    "spelletje": "game",
    "dans": "dance",
    "lied": "song",
    "verhaal": "story",
    "gedicht": "poem",
    "schilderij": "painting",
    "tekening": "drawing",
    "beeld": "statue",
    "foto": "photo",
    "camera": "camera",
    "tv": "television",
    "radio": "radio",
    "krant": "newspaper",
    "tijdschrift": "magazine",
    "webpagina": "webpage",
    "email": "email",
    "adres": "address",
    "postcode": "postal code",
    "stad": "city",
    "land": "country",
    "wereld": "world",
    "continent": "continent",
    "planeet": "planet",
    "universum": "universe",
    "verjaardag": "birthday",
    "jubileum": "anniversary",
    "herdenking": "memorial",
    "seizoen": "season",
    "lente": "spring",
    "zomer": "summer",
    "herfst": "autumn",
    "winter": "winter",
    "kleur": "color",
    "rood": "red",
    "blauw": "blue",
    "geel": "yellow",
    "oranje": "orange",
    "roze": "pink",
    "paars": "purple",
    "zwart": "black",
    "wit": "white",
    "grijs": "gray",
    "bruin": "brown",
    "dier": "animal",
    "vogels": "birds",
    "insect": "insect",
    "paard": "horse",
    "koe": "cow",
    "varken": "pig",
    "kip": "chicken",
    "schaap": "sheep",
    "geit": "goat",
    "konijn": "rabbit",
    "hert": "deer",
    "beer": "bear",
    "wolf": "wolf",
    "leeuw": "lion",
    "tijger": "tiger",
    "olifant": "elephant",
    "giraffe": "giraffe",
    "kangoeroe": "kangaroo",
    "aap": "monkey",
    "vis": "fish",
    "dolfijn": "dolphin",
    "walvis": "whale",
    "haai": "shark",
    "octopus": "octopus",
    "krab": "crab",
    "garnalen": "shrimp",
    "zeester": "starfish",
    "pinguïn": "penguin",
    "zebra": "zebra",
    "nijlpaard": "hippopotamus",
    "krokodil": "crocodile",
    "slang": "snake",
    "schildpad": "turtle",
    "leguaan": "iguana",
    "kameleon": "chameleon",
    "hagedis": "lizard",
    "spin": "spider",
    "mug": "mosquito",
    "vlieg": "fly",
    "bij": "bee",
    "vlinder": "butterfly",
    "mier": "ant",
    "kever": "beetle",
    "worm": "worm",
    "rups": "caterpillar",
    "libel": "dragonfly",
    "sprinkhaan": "grasshopper",
    "wesp": "wasp",
    "miereneter": "anteater",
    "arend": "eagle",
    "uil": "owl"





    }

             }
gekozen = input("Welk woord wil je vertalen: ")
gekozen1 = gekozen.lower()
if gekozen1 in woordenboek:
    print(woordenboek[gekozen1])
else:
    print("dit woord staat niet in ons woordenboek")

