requests = [
    "I want to", "I need to", "Need to", "I'd like to", "Want to",
]
actions = [
    "model", "estimate", "predict", "forecast", "project",
]
stats = [
    "", "average ", "median "
]
fields = [
    "number of", "price of", "rate of"
]
subjects = {
    "number of": [
        "pregnancies", "car crashes", "criminal incidents", "trees", "power failures", "wild dogs",
        "students", "professors", "lawyers", "doctors", "firefighters", "police officers"

    ],
    "price of": [
        "cars", "cats", "dogs", "candy", "steak", "beef", "pancakes", "sugar", "bread",
        "water", "houses", "couches", "sofas", "beds", "furniture", "TVs", "cheese", "game consoles",
        "PC parts", "pencils", "pens", "erasers",
    ],
    "rate of": [
        "poverty", "suicide", "college acceptance",
    ]
}
n = 0
final = False
if final:
    separator = "\t"
else:
    separator = "\t~ "
with open("text_data.txt", "w+") as file:
    for request in requests: # "i want to"
        for action in actions: # "predict"
            for stat in stats: # "average"
                for field in fields: # "number of"
                    for subjectType in subjects.keys(): # "items"
                        if field == subjectType:
                            for subject in subjects[subjectType]:
                                target = stat + field + " " + subject

                                # if target[0:3] == "the":
                                #     target = target[3:]

                                file.write(request + " " + action + " the " + target + separator +
                                           target + separator + "!\n")

                                n += 1

            for subjectType in subjects.keys():
                for subject in subjects[subjectType]:
                    file.write(request + " " + action + " " + subject + separator +
                               subject + separator + "!\n")
                    n += 1


print("done; created " + str(n) + " sentences")
