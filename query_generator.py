requests = [
    "I want to", "I need to", "Need to", "I'd like to", "Want to", "I demand to",
    "I desire to"
]
actions = [
    "model", "estimate", "predict", "forecast", "project", "understand"
]
fields = {
    "quantitative": [
        "", "the number of", "the average number of", "the median number of",
    ],
    "categorical": [

    ],
    "price":[
        "the price of",
    ]
}
subjects = {
    "quantitative": [
        "pregnancies", "car crashes", "criminal incidents", "trees", "power failures",

    ],
    "categorical": [

    ],
    "price":[
        "cars", "cats", "dogs", "candy", "steak", "beef", "pancakes", "sugar", "bread",
        "water"
    ]
}
n = 0
final = False
if final:
    separator = "\t"
else:
    separator = "\t~ "
with open("text_data.txt", "w+") as file:
    for request in requests:
        for action in actions:
            for fieldType in fields.keys():
                for subjectType in subjects.keys():
                    if fieldType == subjectType:
                        for field in fields[fieldType]:
                            for subject in subjects[subjectType]:
                                if field == "":
                                    target = subject
                                else:
                                    target = field + " " + subject

                                file.write(request + " " + action + " " + target + separator +
                                           target + separator + "!\n")
                                n += 1

print("done; created " + str(n) + " sentences")
