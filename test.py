requests = [
    "I want to", "I need to", "Need to", "I'd like to", "Want to",
]

actions = [
    "model", "estimate", "predict",
]

fields = [
    "the number of", "the average number of", "the median number of", ""
]

subjects = [
    "pregnancies", "car crashes", "criminal incidents", "trees"
]
n=0
with open("text_data.txt", "w+") as file:
    for request in requests:
        for action in actions:
            for field in fields:
                for subject in subjects:
                    target = field + " " + subject
                    file.write(request + " " + action + " " + target + "\t" +
                               target + "\t!\n")
                    n += 1


print("done; created " + str(n) + " sentences")
