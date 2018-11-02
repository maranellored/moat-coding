################################################################################
##
##  A module that helps implement the incr_dict function.
##
##  The incr_dict function helps nest multiple dictionaries inside the original
##  dictionary. The nested dictionaries are controlled by the sequence that is
##  provided in the input. The function maps a count to the last element of the
##  sequence.
##  Uses the reduce function to repeatedly apply the nesting function on the
##  dictionary. For setting an element, we nest all but the last element of the
##  sequence as a dictionary and finally add the last element with a count.
##
##  dct = {}
##  incr_dict(dct, ('a', 'b', 'c'))
##  dct = {'a': {'b': {'c': 1}}}
##
##  ** NOTE **
##  If an element in the dictionary is mapped to a count, (For e.g. in the above
##  example 'c' is mapped to 1), trying to replace the element with a new
##  sequence of nested dictionaries is invalid.
##
##  incr_dict(dct, ('a', 'b', 'c', 'd')) is invalid after the above example.
##
################################################################################


def __create(dct, sequence):
    return reduce(lambda dct, key: dct.setdefault(key, {}), sequence, dct)

def __get(dct, sequence):
    return reduce(dict.__getitem__, sequence, dct)

def incr_dict(dct, sequence):

    current_value = 0
    try:
        current_value = __get(dct, sequence)
    except KeyError, e:
        # The required value doesnt exist in our dictionary
        # Can add this sequence with count 1
        pass

    __create(dct, sequence[:-1])[sequence[-1]] = current_value+1
