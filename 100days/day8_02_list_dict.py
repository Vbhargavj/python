travel_log = [
    {
        "country": "India",
        "Visits": 12,
        "cities": ["Junagadh", "ahmedabad", "vadodara"]
    },
    {
        "country": "Junagadh",
        "Visits": 5,
        "cities": ["januda", "malia", "gir"]
    },
]


def add(country, Visits, cities):
    cou = {}
    cou["country"] = country
    cou["Visits"] = Visits
    cou["cities"] = cities
    travel_log.append(cou)


add("japan", 100, ["jnu", "bha", "era"])
add("januda", 5, ["khorasha", "sukhpur", "shantipara"])

for i in range(0, 4):
    print("The country is : "+travel_log[i]["country"] + " In Which total ",
          travel_log[i]["Visits"], " visited cities are ", travel_log[i]["cities"])
