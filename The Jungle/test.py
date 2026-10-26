from Animals import Jaguar, Human, Lemur, MissingData, WrongType, SpeciesRule

jungle=[Human("Rory", 8, "meow"), Human("Chloe",6,"hello"), Jaguar("Cody", 8, "rawrr")]

for animal in jungle:
    animal.daily_task(jungle)
