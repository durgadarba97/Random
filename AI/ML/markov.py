import random

# creating a markov chain
class Markov:
    def __init__(self):

        # here we create an adjacency list representation of the markov chain
        self.transition_matrix = {}

        # start states is a list of probabilities for the start states
        self.start_state = []

        # end states is a list of probabilities for the end states
        self.end_state = []

    def add_transition(self, from_state, to_state, probability):
        if(from_state not in self.transition_matrix):
            self.transition_matrix[from_state] = {}
        
        if(to_state not in self.transition_matrix[from_state]):
            self.transition_matrix[from_state][to_state] = 0
        
        self.transition_matrix[from_state][to_state] += probability
    
    def add_start_state(self, state, probability):
        self.start_state.append((state, probability))
    

    # I dont really understand this function
    def predict_next_state(self, state):
        # get the probabilities for the next state
        probabilities = self.transition_matrix[state]
        # get the total probability
        total = sum(probabilities.values())
        # get a random number between 0 and the total probability
        random_number = random.uniform(0, total)
        # keep track of the probability
        probability = 0
        # for each state
        for key, value in probabilities.items():
            # add the probability of the current state to the probability
            probability += value
            # if the random number is less than the probability
            if(random_number < probability):
                # return the state
                return key
        # if we get here, something went wrong
        return None

    def print_transitions(self):
        
        for key, value in self.transition_matrix.items():
            print(key, value)


# I'll come back to this later.
# TODO:
# 1. Create a Markov chain with a given order.
# 2. Add a word to the Markov chain.
# 3. Get the next word in the Markov chain.
# 4. Get the probability of a word in the Markov chain.
# 5. Get the probability of a sequence of words in the Markov chain.

markov = Markov()
markov.add_transition('a', 'b', 0.5)
markov.add_transition('a', 'c', 0.5)
markov.add_transition('b', 'd', 0.5)
markov.add_transition('b', 'e', 0.5)
markov.add_transition('c', 'f', 0.5)
markov.add_transition('c', 'g', 0.5)
markov.add_transition('d', 'h', 0.5)

markov.print_transitions()
