print("###################################")
print("TASK POKEMON")

class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
#Create a dictionary where pkmntype matches its info

        pkmntypes_info = {"water": "wet", "fire": "fiery", "grass": "grassy", }

#Verifies the level of Pokemon

        if self.level <= 20:
            level_info = "weak"
        elif 20 <= self.level <= 50:
            level_info = "fair"
        else:
            level_info = "strong"
            
#A variable which prints the info about Pokemon

        text = "{}, a {} and {} Pokemon.".format(self.name, pkmntypes_info[self.pkmntype], level_info)
        return text

print("###################################")
print("TASK ANYTHING")

import re
import math

class anything():
#Overloading of system functions
    def __init__(self, thing):
        pass
#thing < comp - OK in any case
    def __lt__(self, comp):
        return True
#thing <= comp - OK in any case
    def __le__(self, comp):
        return True
#thing == comp - OK in any case
    def __eq__(self, comp):
        return True
#thing != comp - OK in any case
    def __ne__(self, comp):
        return True
#thing > comp - OK in any case
    def __gt__(self, comp):
        return True
#thing >= comp - OK in any case
    def __ge__(self, comp):
        return True

print("###################################")
print("TASK FRACTIONS")

class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    #Function that looks for G.C.D - greatest common divisor
    def gcd(self, num, den):
        while num % den != 0:
            num_orig = num
            den_orig = den
            num = den_orig
            den = num_orig % den_orig
        return den

    #Function that trasforms output
    def __str__(self):
        output = str(self.top) + "/" + str(self.bottom)
        return output

    # Function that sums fractories
    #Shortens our final fraction (5/10 = 1/2)
    def __add__(self, other):
        res_top = self.top * other.bottom + self.bottom * other.top
        res_bottom = self.bottom * other.bottom     
        gcd_num = self.gcd(res_top, res_bottom)
        return Fraction(res_top//gcd_num, res_bottom//gcd_num)

    # Equality test
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

