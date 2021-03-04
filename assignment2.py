import numpy as np
import scipy.stats as stats
import math

# Types of dogs and their characteristics
class Beagle:
    probability = 0.30
    # characteristic = [mean, sd]
    girth  = [41, 6]
    height = [37, 4]
    weight = [10, 2]

class Corgi:
    probability = 0.21
    # characteristic = [mean, sd]
    girth  = [53, 9]
    height = [27, 3]
    weight = [12, 2]

class Husky:
    probability = 0.14
    # characteristic = [mean, sd]
    girth  = [66, 10]
    height = [55, 6]
    weight = [22, 6]

class Poodle:
    probability = 0.35
    # characteristic = [mean, sd]
    girth  = [61, 9]
    height = [52, 7]
    weight = [26, 8]

# Characteristic classifications
class Girth:
    # classification = [a, b, c, d]
    small  = [0, 0, 40, 50]
    medium = [40, 50, 60, 70]
    large  = [60, 70, 100, 100]

class Height:
    # classification = [a, b, c, d]
    short  = [0, 0, 40, 50]
    medium = [25, 40, 50, 60]
    tall   = [50, 60, 100, 100]

class Weight:
    # classification = [a, b, c, d]
    light  = [0, 0, 5, 15]
    medium = [5, 15, 20, 40]
    heavy  = [20, 40, 100, 100]

# Input is a three element list with [girth, height, weight]
# Returns the Naive Bayes probability for a specified dog breed using the following formula:
# P(girth = char[0] | breed) * P(height = char[1] | breed) * P(weight = char[2]| breed) * P(breed)
# Work in progress - something is off with the numbers
def naive_bayes_classifier(input):
    def pNaiveBayes(breed, chars):
        return "{:.16f}".format(stats.norm.pdf(chars[0], breed.girth[0], breed.girth[1])
                              * stats.norm.pdf(chars[1], breed.height[0], breed.height[1])
                              * stats.norm.pdf(chars[2], breed.weight[0], breed.weight[1])
                              * breed.probability)

    # Returns the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_probabilities(input):
        # Get the probabilities for each class, then return them as a list
        pBeagle = pNaiveBayes(Beagle, input)       # P(Beagle | input)
        pCorgi  = pNaiveBayes(Corgi, input)        # P(Corgi | input)
        pHusky  = pNaiveBayes(Husky, input)        # P(Husky | input)
        pPoodle = pNaiveBayes(Poodle, input)       # P(Poodle | input)
        return [pBeagle, pCorgi, pHusky, pPoodle]

    # Returns the most likely class, either "beagle", "corgi", "husky", or "poodle"
    def most_likely_class(input):
        # Store the index of the maximum from class_probabilities
        maximum = np.argmax(class_probabilities(input))
        # Return the corresponding breed
        if maximum == 0 : return 'beagle'
        elif maximum == 1 : return 'corgi'
        elif maximum == 2 : return 'husky'
        else : return 'poodle'

    return most_likely_class(input), class_probabilities(input)

# Testing
print(naive_bayes_classifier([59, 32, 17]))


# Input is a three element list with [girth, height, weight]
def fuzzy_classifier(input):
    # Fuzzy membership function
    def f(x, a, b, c, d):
        if ((x <= a) or (d <= x)) : return 0
        elif ((a < x) and (x < b)) : return (x-a)/(b-a)
        elif ((b <= x) and (x <= c)) : return 1
        elif ((c < x) and (x < d)) : return (d-x)/(d-c)

    # Returns the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    def highest_membership_class(input):
        return 'unimplemented'

    # Returns the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_memberships(input):
        return ['beagle', 'corgi', 'husky', 'poodle']

    return highest_membership_class(input), class_memberships(input)

# Testing
print(fuzzy_classifier([59, 32, 17]))
