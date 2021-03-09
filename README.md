# Install Requirements
Please ensure to install numpy and scipy with python3 by doing the following commands:
- python3 -m pip install numpy
- python3 -m pip install scipy

Then run the assignment with the following command:
- python3 assignment2.py

# A2 Technical Document Questions
1. Model-based reflex agent
- The agent maintains an internal representation of the environment state
- It knows the typical characteristics for each dog breed
- It knows the probability of each dog breed

2.

3.

4.

5. The Godel t-norm returns the max of inputs (x,y) and s-norm returns the min of inputs (x,y)
- Suppose we have [50, 20, 40] as the input
- Using Godel t-norm and s-norm the output is ['corgi', 0, 1, 0, 1]
- Using Gougen t-norm and s-norm the output is ['poodle', 0, 0, 0, 1]


## Note:
- Probabilities returned in the naive_bayes_classifier are wrong but the output from the most_likely_class function are correct
