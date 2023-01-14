from DSO import *

class Pcs64i(DSO):

    _parallel = None
    _numSamples = 4096
    _preTriggerSize = 1024

#    _outBuffer=[[],[]]

    _buffer = [[],[]]

    def __init__(self):
        pass

    def setParallel(self, parallel):
        self._parallel = parallel