from math import floor


class AmicableNumbers():
    """
    Amicable number is a concept that join two numbers with this
    characteristics
    both are two numbers where sum of divisors is equal to the other number

    https://en.wikipedia.org/wiki/Amicable_numbers
    """
    #  divisors is a lambda funciton used to collect all divisors for a number

    def divisors_sum_collector(self, top_value: int):
        assert isinstance(top_value, int), "Value should be an integer value"
        divisors_f = lambda n:  [d for d in range(1, floor((n/2)+1)) if (n%d == 0)]
        divisors_sum_collector = {value: sum(divisors_f(value)) for value in range(1,top_value)}
        return divisors_sum_collector

    def amicables_finder(self, divisors_sum: dict):
        amicables = []
        numbers = divisors_sum.keys()
        for c_number in list(numbers):
            if c_number in divisors_sum.keys():
                _current_summatory = divisors_sum[c_number]
                if _current_summatory in numbers:
                    _possible_ammicable = divisors_sum[_current_summatory]
                    if (
                        _possible_ammicable == c_number
                        and
                        c_number != _current_summatory
                    ):
                        amicable_relation = (c_number,  _current_summatory)
                        amicables.append(amicable_relation)
                        try:
                            divisors_sum.pop(c_number)
                            divisors_sum.pop(_current_summatory)
                        except KeyError as ke:
                            print(ke)
        return amicables

    def get_amicables(self, top_value):
        divisors_sum = self.divisors_sum_collector(top_value)
        return self.amicables_finder(divisors_sum)


if __name__ == '__main__':
    from pprint import pprint
    an = AmicableNumbers()
    _  = an.get_amicables(100000)
    pprint(_)
            
     
