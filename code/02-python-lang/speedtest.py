import datetime
import random

# noinspection SpellCheckingInspection
letters = "abcdefghijklmnopqrstuvwxyz"

count = 1_000_000
people = []

for _ in range(count):
    person = {
        'name': ''.join(random.choice(letters) for _ in range(8)),
        'email': ''.join(random.choice(letters) for _ in range(8)) + '@gmail.com',
        'age': random.randint(30, 60),
    }
    people.append(person)

lookup = {p.get('email'): p for p in people}
target_person = people[len(people)//2]
found_person = None

t0 = datetime.datetime.now()

for p in people:
    if p.get('email') == target_person.get('email'):
        found_person = p
        break

dt1 = datetime.datetime.now() - t0
print(f'List found {found_person['name']} {found_person['email']} in {dt1.total_seconds()*1000:,.3f} ms')

t1 = datetime.datetime.now()
target_person = lookup.get(target_person.get('email'))
dt2 = datetime.datetime.now() - t1

print(f'Dict found {found_person['name']} {found_person['email']} in {dt2.total_seconds()*1000:,.3f} ms')

print(f'Speed up is {dt1.total_seconds()/dt2.total_seconds():,.1f}x')
