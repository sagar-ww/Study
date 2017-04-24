from numpy import *
class NeuralNet(object):
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((3,1)) -1

    def __
