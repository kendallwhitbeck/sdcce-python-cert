# Fundamental theorem of arithmetic
# Quantum computer model
# Product of primes:
# 2^5 * 3^2 * 5^1 would be: P(2,5) * P(3,2) * P(5,1)
#
# Usage concept:  PP().synthesis({(2,5),(3,2),(5,1)})
# {(2,5),(3,2),(5,1)}   <----   PP().desynthesis(44680)

import math
import primePy # https://www.geeksforgeeks.org/primepy-module-in-python/
from primePy import primes

# Product of Primes class.
class PP:
    """
    This is the class documentation.
    Line 1
    Line 2
    """
    def __init__(self, prime, exponent):
        """ Constructor method """
        try:
            self.prime = int(prime)
            self.exponent = int(exponent)
            self.value = int(math.pow(self.prime, self.exponent))
        except:
            print("caught.")
            pass
        else:
            pass
        finally:
            pass

    def __str__(self):
        """ return string for an PP object state. """
        str = "The state of this object is {}^{}".format(self.prime, self.exponent)
        return str

    def __call__(self):
        result = 1474800
        return result

    # Two objects summed together (e.g.): PP(2,5) + P(73,1)
    def __sum__(self, *args):
        """ Sum two PP objects. """
        # Something recursive here...
        if args == 1:
            return 1
        else:
            return 1 + self.__sum__(args)

    # Two objects together (e.g.): PP(2,5) * PP(73,1)
    def __mul__(self, *args):
        """ Multiplies two PP objects. """
        rslt = int(0)

        try:
            # Assume args[0] is the same PP class
            self.value *= args[0].value
            if self.prime == args[0].prime:
                self.exponent += args[0].exponent
            else:
                self.value *= int(math.pow(args[0].prime, args[0].exponent))

            print(" {}^{} * {}^{}".format(self.prime, self.exponent, args[0].prime, args[0].exponent))
        except:
            print("Exception here..")
            pass
        else:
            print("Exception else here..")
            pass
        finally:
            print("Exception finally here..")
            return self

        try:
            # Assume args is a set of tuples
            # print("Not the same class")
            self.value *= args
            print(args)

        except:
            pass
        else:
            pass
        finally:
            return self

    pass

class Oscillator:
    def __init__(self, frequency):
        """ Construct an oscillator with a given frequency. """
        # Eq f = 1/ (2 *math.pi * math.sqrt(self.capacitance * self.inductance))
        self.frequency = frequency

        # Calculate inductance and capacitance from frequency
        self.inductance = 1
        self.capacitance = 1

        # Model some resistance
        self.resistance = 1

        # Calculate the sine wave model.
        # self.wave_function = math.sin(xt-kw)

        str = "Created {}Hz oscillator, L={:.2f},C={:.2f}".format(self.frequency, self.inductance, self.capacitance)
        print(str)
        pass

    def fab(self):
        pass
        return self

# Two oscillators form a quantum digit.
class QuantumDigit:
    def __init__(self, oscillator_a, oscillator_b):
        """ Construct a quantum digit with two oscillators. """
        self.oscillator_a = oscillator_a
        self.oscillator_b = oscillator_b
        pass

    def display(self):
        print("Displaying quantum digit")
        pass

    def fab(self):
        pass
        return self

# Zero crossing detectors count zero-crossings transitions for a single oscillator.
class ZeroCrossingDetector:
    def __init__(self, oscillator):
        """ Construct a zero crossing detector for an oscillator. """
        self.oscillator = oscillator
        self.up_count = 0
        self.dn_count = 0
        pass

    # Interval, such as between 0 and 2pi
    def detect(self, start_interval, stop_interval):
        # Create a response curve.
        # Count the number of zero crossings...
        self.up_count = self.oscillator.frequency
        self.dn_count = -self.oscillator.frequency
        pass

class QuantumComputer:
    def __init__(self, calibration_freq):
        """ Construct a quantum computer with all prime states up\
        to the calibration frequency. """
        print("Creating QC at {}Hz:".format(calibration_freq))
        self.states = list(primes.between(0, calibration_freq))
        self.oscillator_bank = list()
        self.zero_crossing_detector_bank = list()
        print(self.states)
        pass

    def get_quantum_states(self):
        """ Returns the set of prime states. """
        print("Retrieving prime oscillator states:")
        for frequency in self.states:
            print(frequency, end="; ")
        print("")
        return self.states

    def start_oscillators(self, oscillator_set):
        """ Start the oscillators for the quantum computer. """
        # Create sine waves for all frequencies
        print("Starting prime oscillator states:")
        for frequency in oscillator_set:
            # Add an oscillator object to oscillator bank
            self.oscillator_bank.append(Oscillator(frequency))
            print(frequency, end="; ")
        print("")
    pass

    # Sensitivity check on prime states
    def orthogonal_states(self):
        self.zero_crossing_detector_bank = list()
        for osc in self.oscillator_bank:
            #print(osc.frequency)
            self.zero_crossing_detector_bank.append(ZeroCrossingDetector(osc))
            self.zero_crossing_detector_bank[-1].detect(0, 2*math.pi)
        return len(self.oscillator_bank)

    def synthesis(self, *args):
        # *args should be a list of tuples, where each
        # tuple is a prime base, to a exponent.
        print("synthesis: ")
        for arg in args:
            print(arg)

    def desynthesis(self, integer):
        # integer is a large integer which will be broken
        # into a product of primes (prime index)
        print("desynthesis: ")
        print(integer)
        pass

    pass

    # Input
    def sense(self):
        pass

    # Read states
    def perceive(self):
        pass

    # Network
    def feel(self):
        pass

    # Reflection
    def react(self):
        pass

    # Emission
    def respond(self):
        pass

    # Particle Wave behaviors
    def incident(self):
        pass

    def absorbed(self):
        pass

    def reflected(self):
        pass

    def emitted(self):
        pass


class SomeDatabase:
    # This is called a constructor, because it's our opportunity to set
    # or construct all the tables, lists, data structures, memory allocation,
    # Create user accoutns
    def __init__(self, a, b):
        self.a = a
        self.b = b
        pass

    def add():
        pass


def main():
    # Custom classe, created a custom object from the class
    N = PP(1,2) * PP(13,2)
    print(type(N))
    print(N.__dir__())
    # We can look through all the variables within the class, and do something..
    print(N.__mul__.__doc__)
    print(N.__sum__.__doc__)
    print(N.__init__.__doc__)
    print(N.__doc__)
    r = N()
    print(r)
    print(N())
    #print(N()) This one is doing the acutal printing.



    #N = PP(1,2) * PP(2,3)   # PP(1,2).__mul__(PP(2,3))
    #N() * P(2,5)
    #M = PP(2,3) * (PP(5,2) * PP(2,5))

    # This is really trying to print a object which has other variables within it.
    #print(N)


    #print(M)
    #print(M())

    #L = N * M

    #print(L)
    #print(L())

    # Create a quantum computer based on a quartz crystall oscillator reference.
    #crystal_freq_hz = 32768
    #qc = QuantumComputer(crystal_freq_hz)
    #states = qc.get_quantum_states()
    #qc.start_oscillators(states)

    # Perform error check, that no primes overlap. Count unique states.
    #print(qc.orthogonal_states())

    # Compose (synthesize) and decompose (desynthesize) integers.

    #Synthesize an integers based on  Create a product of primes
    #I = qc.synthesis(PP(2,1)*PP(3,1), PP(5,1)*PP(7,1))
    #print(I)

    # Decompose an integer I, into its prime factors
    #qc.desynthesis(I)


main()

