from __future__ import print_function


def powersum(given, power):
    def executer(start, given, power, trace, counter):
        if given == 0:
            print(trace)
            counter[0] = counter[0] + 1
            return True

        if given < 0:
            return False

        if pow(start, power) > given:
            return False

        for item in range(start, given+1):
            minus = pow(item, power)
            executer(item+1, given-minus, power, trace + [item], counter)

    counter = [0]
    executer(1, given, power, [], counter)
    return counter



def main():
    print(powersum(100,2))

main()
