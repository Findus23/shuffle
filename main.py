from config import people
from derangement import get_derangement
from mail import notify

names = list(people.keys())

shuffled = get_derangement(names)
print(shuffled)

i = 0
for name, email in people.items():
    chosen_person = shuffled[i]
    notify(name, email, chosen_person)
    i += 1
