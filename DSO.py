from enum import IntEnum
from abc import ABC, abstractmethod

class TimeBase(IntEnum):
    TB1s = 0
    TB500ms = 1
    TB200ms = 2
    TB100ms = 3
    TB50ms = 4
    TB20ms = 5
    TB10ms = 6
    TB5ms = 7
    TB2ms = 8
    TB1ms = 9
    TB500us = 10
    TB200us = 11
    TB100us = 12
    TB50us = 13
    TB20us = 14
    TB10us = 15
    TB5us = 16
    TB2us = 17
    TB1us = 18
    TB500ns = 19
    TB200ns = 20
    TB100ns = 21
    TB50ns = 22
    TB20ns = 23
    TB10ns = 24

class VoltsDiv(IntEnum):
    VD50v = 0
    VD20v = 1
    VD10v = 2
    VD5v = 3
    VD2v = 4
    VD1v = 5
    VD500mv = 6
    VD200mv = 7
    VD100mv = 8
    VD50mv = 9
    VD20mv = 10
    VD10mv = 11
    VD5mv = 12
    VD2mv = 13
    VD1mv = 14

class CouplingModel(IntEnum):
    DC=0
    GND=1
    AC=2

class DSO(ABC):
    _mOutBuffer = [[],[]]
    def __init__(self):
        pass

    @abstractmethod
    def setTimeBase(self, timeBase: int):
        pass

    @abstractmethod
    def setVoltsDif(self, voltsDiv: int):
        pass

    @abstractmethod
    def setTriggerEnabled(self, triggerEnabled: int):
        pass

    @abstractmethod
    def setTriggerChannel(self, triggerChannel: int):
        pass

    @abstractmethod
    def setTriggerRaising(self, triggerRaising: bool):
        pass

    @abstractmethod
    def setTriggerLevel(self, triggerLevel: int):
        pass

    @abstractmethod
    def setCouplingMode(self, channel: int, couplingMode: int):
        pass

    @abstractmethod
    def setChannelEnable(self, channel: int, enabled: bool):
        pass

    def lock():
        pass

    def unlock():
        pass

    def data(self, channel: int, i: int):
        return self._outBuffer[channel][i]
