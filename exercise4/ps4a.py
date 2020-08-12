# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
from itertools import permutations


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence)==1:
        return sequence
    else:
        list_permutations = []
        #iterate all characters
        for i in sequence:
            rest_elements=[]
            #add character if the character is different to the actual character in the upper loop
            for x in sequence:
                if x != i:
                    rest_elements.append(x)
                    #print(x)
            #print (rest_elements)
            #call the same function with the rest of elements
            pemutations_recursive = get_permutations(rest_elements)
            print (pemutations_recursive)
            #concatenate the letter of the upper loop with the one receive in the permutation
            for t in pemutations_recursive:
                list_permutations.append(i + t)

    return list_permutations






    # #Using no recursion
    # list_permutations=[]
    # perm= permutations(sequence)
    # for i in list(perm):
    #     list_permutations.append(i)
    # return list_permutations




    #pass #delete this line and replace with your code here

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    #pass #delete this line and replace with your code here
