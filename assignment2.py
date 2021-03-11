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
    short  = [0, 0, 25, 40]
    medium = [25, 40, 50, 60]
    tall   = [50, 60, 100, 100]

class Weight:
    # classification = [a, b, c, d]
    light  = [0, 0, 5, 15]
    medium = [5, 15, 20, 40]
    heavy  = [20, 40, 100, 100]

# Input is a three element list with [girth, height, weight]
def naive_bayes_classifier(input):
    # Format num as a float
    def pFormat(num): return float("{:.8f}".format(float(num)))

    # Returns the Naive Bayes probability for a specified dog breed given the following formula:
    # P(girth = char[0] | breed) * P(height = char[1] | breed) * P(weight = char[2]| breed) * P(breed)
    def pNaiveBayes(breed, chars):
        return pFormat(stats.norm.pdf(chars[0], breed.girth[0], breed.girth[1])
                     * stats.norm.pdf(chars[1], breed.height[0], breed.height[1])
                     * stats.norm.pdf(chars[2], breed.weight[0], breed.weight[1])
                     * breed.probability)

    # Returns the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_probabilities(input):
        # Get the probabilities for each class, then return them as a list
        pBeagle = pNaiveBayes(Beagle, input)      # P(Beagle | input)
        pCorgi  = pNaiveBayes(Corgi, input)       # P(Corgi | input)
        pHusky  = pNaiveBayes(Husky, input)       # P(Husky | input)
        pPoodle = pNaiveBayes(Poodle, input)      # P(Poodle | input)

        total = pBeagle + pCorgi + pHusky + pPoodle
        return [pBeagle/total, pCorgi/total, pHusky/total, pPoodle/total]

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

# Input is a three element list with [girth, height, weight]
def fuzzy_classifier(input):
    # Gougen t-norm for fuzzy and
    def t(x,y): return x*y
    # Gougen s-norm for fuzzy or
    def s(x,y): return x+y-x*y

    # Godel t-norm for fuzzy and
    #def t(x,y): return max(x,y)
    # Godel s-norm for fuzzy or
    #def s(x,y): return min(x,y)

    # Returns the fuzzy membership function for a given characteristic and its a, b,c d values
    def f(x, char):
        if ((x <= char[0]) or (char[3] <= x)) : return 0
        elif ((char[0] < x) and (x < char[1])) : return (x-char[0])/(char[1]-char[0])
        elif ((char[1] <= x) and (x <= char[2])) : return 1
        elif ((char[2] < x) and (x < char[3])) : return (char[3]-x)/(char[3]-char[2])

    # Returns the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    def class_memberships(input):
        # if (height = medium and ((girth = small) or (weight = light))) : return beagle
        mBeagle = t(f(input[1], Height.medium), s(f(input[0], Girth.small), f(input[2], Weight.light)))
        # if (girth = medium and height = short and weight = medium) : return corgi
        mCorgi  = t(f(input[0], Girth.medium), t(f(input[1], Height.short), f(input[2], Weight.medium)))
        # if (girth = large and height = tall and weight = medium) : return husky
        mHusky  = t(f(input[0], Girth.large), t(f(input[1], Height.tall), f(input[2], Weight.medium)))
        # if ((girth = medium) or (height = medium) and weight = heavy) : return poodle
        mPoodle = t(s(f(input[0], Girth.medium), f(input[1], Height.medium)), f(input[2], Weight.heavy))
        return [mBeagle, mCorgi, mHusky, mPoodle]

    # Returns the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    def highest_membership_class(input):
        # Store the index of the maximum from class_probabilities
        maximum = np.argmax(class_memberships(input))
        # Return the corresponding breed
        if maximum == 0 : return 'beagle'
        elif maximum == 1 : return 'corgi'
        elif maximum == 2 : return 'husky'
        else : return 'poodle'

    return highest_membership_class(input), class_memberships(input)
