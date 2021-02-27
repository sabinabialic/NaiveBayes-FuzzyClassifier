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

# Fuzzy membership function
def f(x):
    return 'unimplemented'

def naive_bayes_classifier(input):
  # input is a three element list with [girth, height, weight]

  # Returns the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  def class_probabilities():
      return ['beagle', 'corgi', 'husky', 'poodle']

  # Reurns the most likely class, either "beagle", "corgi", "husky", or "poodle"
  def most_likely_class():
      return 'unimplemented'

  return most_likely_class, class_probabilities


def fuzzy_classifier(input):
  # input is a three element list with [girth, height, weight]

  # Returns the highest membership class, either "beagle", "corgi", "husky", or "poodle"
  def highest_membership_class():
      return 'unimplemented'

  # Returns the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  def class_memberships():
      return ['beagle', 'corgi', 'husky', 'poodle']

  return highest_membership_class, class_memberships
