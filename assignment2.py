class Beagle:
    girth = [41, 6]
    height = [37, 4]
    weight = [10, 2]

class Corgi:
    girth = [53, 9]
    height = [27, 3]
    weight = [12, 2]

class Husky:
    girth = [66, 10]
    height = [55, 6]
    weight = [22, 6]

class Poodle:
    girth = [61, 9]
    height = [52, 7]
    weight = [26, 8]

# Returns the probability for some dog breed
def P(breed):
    if breed == 'beagle': return 0.30
    if breed == 'corgi': return 0.21
    if breed == 'husky': return 0.14
    if breed == 'poodle': return 0.35
    return 0

def naive_bayes_classifier(input):
  # input is a three element list with [girth, height, weight]

  # most_likely_class is a string indicating the most likely class, either "beagle", "corgi", "husky", or "poodle"
  # class_probabilities is a four element list indicating the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  return most_likely_class, class_probabilities


def fuzzy_classifier(input):
  # input is a three element list with [girth, height, weight]

  # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
  # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  return highest_membership_class, class_memberships
