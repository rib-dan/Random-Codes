
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
    result = []
    if len(sequence) == 1:
        #base case
        #Return list of permutations with base case
        return [sequence]
    else:
        #cut the first character of the string and calls get_permutation again
        base = get_permutations(sequence[1:])
        
        #check all the words in the list of permutation
        for word in base:
            #Check all the letters in each word
            for i in range(len(word)):
                #Adds the letter in all the permutations
                aux = word[0:i]+ sequence[0]+word[i:]
                #Verifies for duplicates
                if aux not in result:
                    result.append(aux)
            #Adds the letter at the last position of the permutation
            aux = word+ sequence[0]
            #Verifies for duplicates
            if aux not in result:
                result.append(aux)
        #Return list of permutations
        return(result)
   
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    

    print(get_permutations('abc'))

