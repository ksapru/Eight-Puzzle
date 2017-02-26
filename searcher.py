#
# searcher.py (Final Project)
#
# classes for objects that perform state-space search on Eight Puzzles
#
# name: Sophia Fondell
# email: sfondell@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Danielle Yoseloff
# partner's email: yoseloff@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, init_state, depth_limit):
        '''A method that constructs a new Searcher object
        '''
        self.states = [init_state]
        self.num_tested = 0
        self.depth_limit = depth_limit

   

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def should_add(self, state):
        '''A method that takes a State object called state and returns True
        if the called Searcher should add state to its list of untested states
        and False otherwise
        '''
        if (self.depth_limit != -1) and (state.num_moves > self.depth_limit):
            return False
        elif (state.creates_cycle() == True):
            return False
        else:
            return True

    def add_state(self, new_state):
        '''A method that adds a single State object to the Searcher's list of
        untested states
        '''
        self.states.append(new_state)

    def add_states(self, new_states):
        '''A method that takes a list of State objects called new_states and
        that processes the elements of new_states one at a time as follows
        '''
        for x in range(len(new_states)):
            if self.should_add(new_states[x]) == True:
                self.add_state(new_states[x])
                
    def next_state(self):
        '''chooses the next state to be tested from the list of untested states,
        removing it from the list and returning it
        '''
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self):
        '''A method that performs a full random state-space search, stopping
        when the goal state is found or when the Searcher runs out of untested
        states
        '''
        while len(self.states) != 0:
            tester = self.next_state()
            if tester.is_goal() == True:
                self.num_tested += 1
                return tester
            else:
                self.num_tested += 1
                if tester.creates_cycle() == False:
                    self.add_states(tester.generate_successors())
        return None
    
                
     ### Add your other class definitions below. ###

class BFSearcher(Searcher):
    '''A class for searcher objects that perform the breadth-first search (BFS)
    instead of random search. BFS involves always choosing one of the untested
    states that has the smallest depth
    '''
    def next_state(self):
        '''A method that overrides the next_state method that is inherited from Searcher
        rather than choosing at random from the list of untested states, this version of
        next_state follows FIFO ordering
        '''
        minn = self.states[0]
        for x in range(len(self.states)):
            if self.states[x].num_moves < minn.num_moves:
                minn = self.states[x]
        self.states.remove(minn)
        return minn

class DFSearcher(Searcher):
    '''A class for searcher objects that perform the depth-first search (DFS)
    instead of random search. DFS involves always choosing one of the untested
    states that has the largest depth
    '''
    def next_state(self):
        '''A method that overrides the next_state method that is inherited from Searcher
        rather than choosing at random from the list of untested states, this version of
        next_state follows LIFO ordering
        '''
        m = self.states[-1]
        self.states.remove(m)
        return m
        
class GreedySearcher(Searcher):
    '''A class for searcher objects that perform the Greedy search
    instead of random search. Greedy Search involves an informed search algorithm
    that uses a heuristic function to estimate the remaining cost needed to get
    from a given state to the goal state
    '''
    def __init__(self, init_state, heuristic, depth_limit):
        """ constructor for a GreedySearcher object
        inputs:
            * init_state - a State object for the initial state
            * heuristic - an integer specifying which heuristic
        function should be used when computing the priority of a state
            * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def priority(self, state):
        '''A method that takes a State object called state and that computes
        and returns the priority of that state
        '''
        if self.heuristic == -1:
            heuristic = state.board.num_misplaced()
        elif self.heuristic == 1:
            heuristic = state.board.distance()
        priority = -1 * heuristic
        return priority

    def add_state(self, state):
        '''A method that overrides the add_state method that is inherited from
        Searcher. The method should add a sublist that is a [priority, state]
        paid, where priority is the priority of the state, as determined by
        calling the priority method
        '''
        priority = self.priority(state)
        self.states.append([priority, state])
        
    def next_state(self):
        '''A method that overrides the next_state method that is inherited from
        Searcher. This version of next_state should choose one of the states
        with the highest priority
        '''
        p = max(self.states)
        self.states.remove(p)
        return p[1]

class AStarSearcher(GreedySearcher):
    '''A class for searcher objects that perform A* search. A* is an informed
    search algorithm that assigns a priority to each state based on a heuristic
    function and that selects the best state based on those priorities. However,
    when A* assigns a priority to a state, it also takes into account the cost
    that has already been expended to get to that state
    '''
    def priority(self, state):
        '''A method that takes a state object called state and computes and
        the priority of that state
        '''
        if self.heuristic == -1:
            heuristic = state.board.num_misplaced()
        elif self.heuristic == 1:
            heuristic = state.board.distance()
        moves = state.num_moves
        priority = -1 * (heuristic + moves)
        return priority
    
