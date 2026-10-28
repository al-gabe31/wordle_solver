

def get_color_feedback(input_word:str, compare_word:str) -> str:
    """
    Takes in 2 inputs: input_word and compare word, and outputs the 5 color pattern
    Example: Input ==> "PAPER" & Compare ==> "HARPS" where Output ==> YGBBY
    Reason:
        - First "P" is in the wrong spot
        - Letter "A" is in the correct spot
        - Compare word only has 1 "P" therefore the 2nd "P" in input will be 'blank' (or 'B')
        - Compare word doesn't have an 'E'
        - 'R' is in the wrong spot
    """
    
    #! input validation
    #! #1: both input and compare words are not null
    if input_word is None or compare_word is None:
        raise ValueError(f'ERROR: Input word {input_word} and compare word {compare_word} cannot be None')
    
    #* capitalizing both variables
    input_word = input_word.upper()
    compare_word = compare_word.upper()
    
    #! #2: both input and compare words are 5 letters
    if len(input_word) != 5 and len(compare_word) != 5:
        raise ValueError(f'ERROR: Input word {input_word} [{len(input_word)}] and compare word {compare_word} [{len(compare_word)}] both need to be length 5')

    #! #3: both input and compare words need to only contain letters
    if not input_word.isalpha() or not compare_word.isalpha():
        raise ValueError(f'ERROR: Input word {input_word} and compare word {compare_word} should only contain letters')



    #* algorithm to determine color feedback
    color_feedback = ['X' for i in range(5)]
    input_dict = {}
    compare_dict = {}

    for index, letter in enumerate(input_word):
        if letter not in input_dict:
            input_dict[letter] = []

        input_dict[letter].append(index)
    for index, letter in enumerate(compare_word):
        if letter not in compare_dict:
            compare_dict[letter] = []

        compare_dict[letter].append(index)



    #* checking each letter in input_dict and getting its corresponding color feedback
    for key in input_dict.keys():
        print(f'CURR KEY = {key}')
        for i in range(len(input_dict[key])):
            print(f'input_dict: {input_dict}')
            print(f'compare_dict: {compare_dict}')

            curr_index = input_dict[key][0]

            if key not in compare_dict or len(compare_dict[key]) == 0:
                color_feedback[curr_index] = 'B' #! letter not found in compare word
                input_dict[key] = input_dict[key][1:] #* removing leading index
                print(f'color_feedback {color_feedback}\n')
                continue

            compare_index = -1 if len(compare_dict[key]) == 0 else compare_dict[key][0]

            if curr_index != compare_index:
                color_feedback[curr_index] = 'Y' #! letter in wrong spot
                input_dict[key] = input_dict[key][1:] #* removing leading index
                compare_dict[key] = compare_dict[key][1:] #* removing leading index
                print(f'color_feedback {color_feedback}\n')
                continue

            if curr_index == compare_index:
                color_feedback[curr_index] = 'G' #! letter in correct spot
                input_dict[key] = input_dict[key][1:] #* removing leading index
                compare_dict[key] = compare_dict[key][1:] #* removing leading index
                print(f'color_feedback {color_feedback}\n')
                continue

    #! #4: checking that all spots in color_feedback were populated
    if 'X' in ''.join(color_feedback):
        raise ValueError(f'ERROR: color_feedback {"".join(color_feedback)} cannot have unpopulated spots')

    return ''.join(color_feedback)

if __name__ == '__main__':
    try:
        input_word = 'llama'
        compare_word = 'allot'
        color_feedback = get_color_feedback(input_word, compare_word)

        print(color_feedback)
    except ValueError as e:
        print(e)