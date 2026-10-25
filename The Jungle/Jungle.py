from Animals import Animal, Jaguar, Human, Lemur, MissingData, WrongType, SpeciesRule
jungle=list()
fruits=100
x=102
names=["Rex", "Jara", "Rory", "Jaz", "Leo", "Elly", "Merle", "Luna", "Sam", "Emma", "Ben", "Chloe"]
sounds=["Roar", "GRR", "meow", "Hello!", "purr", "rrawr!"]
randomizer=["67"]
for i in range(x):
    j=hash(randomizer[i])%20
    k=hash(randomizer[i])%12
    l=hash(randomizer[i])%6
    randomizer.append(str(hash(randomizer[i])))
    
    if hash(randomizer[i])%101<41:
        try:
            jungle.append(Jaguar(names[k], j, sounds[l]))
        except WrongType:
            continue
        except SpeciesRule:
            continue
        except MissingData:
            continue
    elif hash(randomizer[i])%101<81:
        try:
            jungle.append(Lemur(names[k], j, sounds[l]))
        except WrongType:
            continue
        except SpeciesRule:
            continue
        except MissingData:
            continue
    else:
        try:
            jungle.append(Human(names[k], j, sounds[l]))
        except WrongType:
            continue
        except SpeciesRule:
            continue
        except MissingData:
            continue

for i in range(len(jungle)):
    print(jungle[i])

print(len(jungle))

for animal in jungle:
    if type(animal)==Lemur:
        fruits=animal.daily_task(fruits)
    else:
        animal.daily_task(jungle)

print(len(jungle))
print(fruits)