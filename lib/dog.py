#!/usr/bin/env python3

class Dog:

    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        print("A dog is born!")
    
    def bark(self):
        print("Woof!")
    
    def name(self, name):
        print(f"The dog's name is {name}")

    def breed(self, breed):
    #     assert self.breed == "Dalmation"
        self.breed = breed
    #     print(f"This dog is a {breed}")

# fido = Dog("Fido")

# snoopy = Dog("Snoopy")