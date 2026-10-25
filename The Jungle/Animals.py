from abc import ABC
class MissingData(Exception):
    def __init__(self):
        print(f"Missing the required data to create animal. ")
class WrongType(Exception):
    def __init__(self):
        print(f"The provided data is not the right type. ")
class SpeciesRule(Exception):
    def __init__(self, message=""):
        print(f"The provided data conflicts with species rules. {message}")

class Animal(ABC):

    def __init__(self, name:str, age:int, sound:str):
        if name==None or age==None or sound==None:
            raise MissingData
        elif type(name)!=str or type(age)!=int or type(sound)!=str:
            raise WrongType
        else:
            self.name=name
            self.age=age
            self.sound=sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}.")

    def daily_task(self):
        pass

    def __str__(self):
        return(f"{self.name} the {type(self)} is {self.age} years old and makes the sound {self.sound}")

class Jaguar(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age>15:
            raise SpeciesRule(f"Bad age. {age} not compatible with Jaguar. ")
        elif sound.lower().count("r")<2:
            raise SpeciesRule(f"Bad sound. {sound.capitalize()} not compatible with Jaguar.")

    def daily_task(self, lst:list):
        i=0
        while True:
            i+=1
            try:
                if type(lst[i+lst.index(self)]) is Human or type(lst[i+lst.index(self)]) is Lemur:
                    print(f"{self.name} the {type(self)} hunted down {lst[i+lst.index(self)].name}")
                    lst.pop(i+lst.index(self))
                    break
                elif type(lst[lst.index(self)-i]) is Human or type(lst[lst.index(self)-i]) is Lemur:
                    print(f"{self.name} the {type(self)} hunted down {lst[lst.index(self)-i].name}")
                    lst.pop(lst.index(self)-i)
                    break
            except IndexError:
                if i==len(lst):
                    print (f"{self.name} the {type(self)} has no one to hunt down and went home hungry. ")
                    break
                continue
                     

class Lemur(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age>10:
            raise SpeciesRule(f"Bad age. {age} not compatible with Lemur.")
        elif "e" not in sound:
            raise SpeciesRule(f"Bad sound. {sound.capitalize()} not compatible with Lemur.")

    def daily_task(self, fruits:int):
        if fruits>=10:
            fruits-=10
            print(f"{self.name} the {type(self)} ate 10 fruits. ")
            return fruits
        elif 1<=fruits<10:
            print(f"{self.name} the {type(self)} ate {fruits} fruits. There are no more fruits left. ")
            fruits=0
            return fruits
        else: 
            print(f"{self.name} the {type(self)} has no fruits to eat. It is complaining. ")
            return fruits


class Human(Animal):

    building_count=0

    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age>10:
            raise SpeciesRule(f"Bad age. {age} not compatible with Human.")
        elif "e" not in sound:
            raise SpeciesRule(f"Bad sound. {sound.capitalize()} not compatible with Human.")

    def daily_task(self, lst:list):
        human_index=lst.index(self)
        all_buildings=dict()
        if human_index==0 and type(lst[human_index+1])==Human and type(lst[human_index+2])!=Human:
            Human.building_count+=1
            all_buildings[(f"Building{Human.building_count}")]=(self.name, lst[human_index+1].name)
            print(Human.building_count, all_buildings)
        elif (human_index==len(lst)-1 and type(lst[human_index-1]==Human) and type(lst[human_index+2])!=Human):
            Human.building_count+=1
            all_buildings[(f"Building{Human.building_count}")]=(self.name, lst[human_index-1].name)
            print(Human.building_count, all_buildings)
        elif type(lst[human_index+1])==Human and type(lst[human_index-1])==Human:
            Human.building_count+=1
            all_buildings[(f"Building{Human.building_count}")]=(lst[human_index-1].name, self.name, lst[human_index+1].name)
            print(Human.building_count, all_buildings)
