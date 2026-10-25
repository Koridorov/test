from Animals import Jaguar, Human, Lemur, MissingData, WrongType, SpeciesRule

jungle=[Human("Rory", 8, "meow"), Human("Chloe",6,"hello"), Lemur("Jaz", 7, "meow")]

for animal in jungle:
    animal.daily_task(jungle)
