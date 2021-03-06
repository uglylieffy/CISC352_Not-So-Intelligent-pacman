# solutions.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

'''Implement the methods from the classes in inference.py here'''

import util
from util import raiseNotDefined
import random
import busters
from util import manhattanDistance
def normalize(self):
    """
    Normalize the distribution such that the total value of all keys sums
    to 1. The ratio of values for all keys will remain the same. In the case
    where the total value of the distribution is 0, do nothing.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> dist.normalize()
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
    >>> dist['e'] = 4
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
    >>> empty = DiscreteDistribution()
    >>> empty.normalize()
    >>> empty
    {}
    """
    "*** YOUR CODE HERE ***"
    # get sum of all items in dictionary
    total = sum(self.values()) 
    # For an empty distribution or a distribution where all of the values are zero, 
    # do nothing.
    if total != 0 and self is not None:
        for key,value in self.items():
            # method modifies the distribution directly, 
            # rather than returning a new distribution.
            self[key] = value/total
    # raiseNotDefined()

def sample(self):
    """
    Draw a random sample from the distribution and return the key, weighted
    by the values associated with each key.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> N = 100000.0
    >>> samples = [dist.sample() for _ in range(int(N))]
    >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
    0.2
    >>> round(samples.count('b') * 1.0/N, 1)
    0.4
    >>> round(samples.count('c') * 1.0/N, 1)
    0.4
    >>> round(samples.count('d') * 1.0/N, 1)
    0.0
    """
    "*** YOUR CODE HERE ***"
    # get random number between 1 to 0
    rdm = random.random()
    increment = 0
    # get sum of all items in dictionary
    total = sum(self.values()) 
    # For an empty distribution or a distribution where all of the values are zero, 
    # do nothing.
    # if total != 0 and self is not None: 
    for key, value in self.items():
        distribution = value/total
        if distribution != 0 and self is not None: 
            compare = distribution + increment
            if compare > rdm and rdm >= increment:
                #Draw a random sample from the distribution and return the key
                return key
            increment += distribution

    #raiseNotDefined()




def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
    """
    Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
    """
    "*** YOUR CODE HERE ***"
    #when we capture a ghost and send it to the jail location
    if ghostPosition == jailPosition:
        if noisyDistance == None:
            #So, if the ghost???s position is the jail position, 
            #then the observation is None with probability 1,
            return 1
        else:
            #everything else with probability 0
            return 0
        
    if noisyDistance == None:
        return 0
    #find distance between ghost & pacman
    trueDistance = manhattanDistance(ghostPosition, pacmanPosition)
    #obP =  P(noisyDistance | pacmanPosition, ghostPosition)
    obP = busters.getObservationProbability(noisyDistance, trueDistance)
    return obP

    #raiseNotDefined()



def observeUpdate(self, observation, gameState):
    """
    Update beliefs based on the distance observation and Pacman's position.

    The observation is the noisy Manhattan distance to the ghost you are
    tracking.

    self.allPositions is a list of the possible ghost positions, including
    the jail position. You should only consider positions that are in
    self.allPositions.

    The update model is not entirely stationary: it may depend on Pacman's
    current position. However, this is not a problem, as Pacman's current
    position is known.
    """
    "*** YOUR CODE HERE ***"
    #obtain Pacman???s position using gameState.getPacmanPosition()
    pacmanPosition = gameState.getPacmanPosition()
    jailPosition = self.getJailPosition()
    #self.allPositions is a list of the possible ghost positions, including the jail position
    print("all positions:" ,self.allPositions)
    for ghostPosition in self.allPositions:
        print("self",self)
        print("ghost position:",ghostPosition)
        print("observation:",observation)
        print("pacMan position:",pacmanPosition)
        print("jail position:",jailPosition)
        prob = self.getObservationProb(observation, pacmanPosition, ghostPosition, jailPosition)
        self.beliefs[ghostPosition] = prob * self.beliefs[ghostPosition]
    self.beliefs.normalize()
    #raiseNotDefined()
    #self.beliefs.normalize()


def elapseTime(self, gameState):
    """
    Predict beliefs in response to a time step passing from the current
    state.

    The transition model is not entirely stationary: it may depend on
    Pacman's current position. However, this is not a problem, as Pacman's
    current position is known.
    """
    "*** YOUR CODE HERE ***"
    raiseNotDefined()