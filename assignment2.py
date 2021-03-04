import numpy as np
import scipy.stats as stats
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
    # P(girth = char[0] | breed) * P(height = char[1] | breed) * P(weight = char[2]| breed) * P(breed)
    def pNaiveBayes(breed, chars):
        return (stats.norm.pdf(chars[0], breed.girth[0], breed.girth[1])
              * stats.norm.pdf(chars[1], breed.height[0], breed.height[1])
              * stats.norm.pdf(chars[2], breed.weight[0], breed.weight[1])
              * breed.probability)

    # Returns the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_probabilities(input):
        pBeagle = "{:.16f}".format(pNaiveBayes(Beagle, input))       # P(Beagle | input)
        pCorgi  = "{:.16f}".format(pNaiveBayes(Corgi, input))        # P(Corgi | input)
        pHusky  = "{:.16f}".format(pNaiveBayes(Husky, input))        # P(Husky | input)
        pPoodle = "{:.16f}".format(pNaiveBayes(Poodle, input))       # P(Poodle | input)
        return [pBeagle, pCorgi, pHusky, pPoodle]

    # Returns the most likely class, either "beagle", "corgi", "husky", or "poodle"
    def most_likely_class(input):
        maximum = np.argmax(class_probabilities(input))
        if maximum == 0 : return 'beagle'
        elif maximum == 1 : return 'corgi'
        elif maximum == 2 : return 'husky'
        else : return 'poodle'

    return most_likely_class(input), class_probabilities(input)

# Testing
#print (pNaiveBayes(Corgi, [59, 32, 17]))
# Testing
#print(pCharacteristic(Beagle.probability, Beagle.girth[0], Beagle.girth[1]))
# Testing
print(naive_bayes_classifier([59, 32, 17]))


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
