import numpy as np
import math

# Types of dogs and their characteristics
class Beagle:
    probability = 0.30
    girth = [41, 6]
    height = [37, 4]
    weight = [10, 2]

class Corgi:
    probability = 0.21
    girth = [53, 9]
    height = [27, 3]
    weight = [12, 2]

class Husky:
    probability = 0.14
    girth = [66, 10]
    height = [55, 6]
    weight = [22, 6]

class Poodle:
    probability = 0.35
    girth = [61, 9]
    height = [52, 7]
    weight = [26, 8]

# Characteristic classifications
class Girth:
    # classification = [a, b, c, d]
    small = [0, 0, 40, 50]
    medium = [40, 50, 60, 70]
    large = [60, 70, 100, 100]

class Height:
    # classification = [a, b, c, d]
    short = [0, 0, 40, 50]
    medium = [25, 40, 50, 60]
    large = [50, 60, 100, 100]

class Weight:
    # classification = [a, b, c, d]
    light = [0, 0, 5, 15]
    medium = [5, 15, 20, 40]
    heavy = [20, 40, 100, 100]

# Input is a three element list with [girth, height, weight]
def naive_bayes_classifier(input):
    # Returns the Naive Bayes probability for a specified dog breed
    # Work in progress - something is off with the numbers
    def pNaiveBayes(breed, chars):
        return ((pCharacteristic(chars[0], breed.girth[0], breed.girth[1]))
             * (pCharacteristic(chars[1], breed.height[0], breed.height[1]))
             * (pCharacteristic(chars[2], breed.weight[0], breed.weight[1]))
             * breed.probability)
    # Testing
    #print (pNaiveBayes(Beagle, [59, 32, 17]))

    # Returns the probability of a characteristic for a specified dog breed
    # Work in progress - not sure what x is supposed to be
    def pCharacteristic(x, mean, sd):
        variance = float(sd)**2
        denom = (2*math.pi*variance)**0.5
        num = math.exp(-(float(x)-float(mean))**2/(2*variance))
        return num/denom
    # Testing
    #print(pCharacteristic(Beagle.probability, Beagle.girth[0], Beagle.girth[1]))

    # Returns the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_probabilities():
      pBeagle = 0       # P(Beagle | input)
      pCorgi = 0        # P(Corgi | input)
      pHusky = 0        # P(Husky | input)
      pPoodle = 0       # P(Poodle | input)
      return [pBeagle, pCorgi, pHusky, pPoodle]

    # Returns the most likely class, either "beagle", "corgi", "husky", or "poodle"
    def most_likely_class():
      return 'unimplemented'

    return most_likely_class, class_probabilities

# Input is a three element list with [girth, height, weight]
def fuzzy_classifier(input):
    # Fuzzy membership function
    def f(x):
        return 'unimplemented'

    # Returns the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    def highest_membership_class():
        return 'unimplemented'

    # Returns the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_memberships():
        return ['beagle', 'corgi', 'husky', 'poodle']

    return highest_membership_class, class_memberships
