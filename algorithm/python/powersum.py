from __future__ import print_function

counter=0

def powersum(given, power):
    global counter
    def executer(start, given, power, trace):
        global counter
        if given == 0:
            print(trace)
            counter += 1
            return True

        if given < 0:
            return False

        if pow(start, power) > given:
            return False

        for next in range(start, given+1):
            minus = pow(next, power)           
            executer(next+1, given-minus, power, trace + [next])

    counter=0
    executer(1, given, power, [])
    return counter



def main():
    print(powersum(100,2))

main()
