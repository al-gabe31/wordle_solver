

def bitwise_and(input_bits:list[int], compare_bits:list[int]) -> list[int]:
    #! check that both have the same length
    if len(input_bits) != len(compare_bits):
        raise ValueError(f'ERROR - both input_bits [{len(input_bits)}] and compare_bits [{len(compare_bits)}] need to have the same length')

    output_bits:list[int] = []

    for index in range(len(input_bits)):
        if input_bits[index] == 1 and input_bits[index] == compare_bits[index]:
            output_bits.append(1)
        else:
            output_bits.append(0)

    return output_bits

def bitwise_xor(input_bits:list[int], compare_bits:list[int]) -> list[int]:
    #! check that both have the same length
    if len(input_bits) != len(compare_bits):
        raise ValueError(f'ERROR - both input_bits [{len(input_bits)}] and compare_bits [{len(compare_bits)}] need to have the same length')

    output_bits:list[int] = []

    for index in range(len(input_bits)):
        if (input_bits[index] == 1 and compare_bits[index] == 0) or (input_bits[index] == 0 and compare_bits[index] == 1):
            output_bits.append(1)
        else:
            output_bits.append(0)

    return output_bits

def letter_bits(input_word:str, target_letter:str) -> list[int]:
    #! validate inputs
    if input_word is None:
        raise ValueError(f'ERROR - input_word cannot be None')
    if target_letter is None:
        raise ValueError(f'ERORR - target_letter cannot be None')
    if not input_word.isalpha():
        raise ValueError(f'ERROR - input_word [{input_word}] should only contain letters')
    if len(target_letter) != 1:
        raise ValueError(f'ERORR - target_letter [{target_letter}] must have a length of 1')
    if not target_letter.isalpha():
        raise ValueError(f'ERROR - target latter must be a letter')

    #* normalizing inputs
    input_word = input_word.upper()
    target_letter = target_letter.upper()

    output_bits:list[int] = []

    for letter in input_word:
        if letter == target_letter:
            output_bits.append(1)
        else:
            output_bits.append(0)

    return output_bits

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
    color_feedback = ['B' for i in range(5)]
    input_dict = {}
    compare_dict = {}

    for letter in input_word:
        if letter not in input_dict:
            input_dict[letter] = letter_bits(input_word, letter)
    for letter in compare_word:
        if letter not in compare_dict:
            compare_dict[letter] = letter_bits(compare_word, letter)

    for letter in input_dict.keys():
        #* checking for GREENS
        if letter in compare_dict:
            and_result = bitwise_and(input_dict[letter], compare_dict[letter])
            green_bits = bitwise_and(input_dict[letter], and_result)

            for index, bit in enumerate(green_bits):
                if bit == 1:
                    color_feedback[index] = 'G'

        #* checking for YELLOWS
        if letter in compare_dict:
            unclaimed_copies = sum(compare_dict[letter]) - sum(bitwise_and(input_dict[letter], compare_dict[letter])) #* the number of copies for a letter in compare_dict that have yet to be claimed by a green match
            xor_result = bitwise_xor(input_dict[letter], compare_dict[letter])
            yellow_bits = bitwise_and(input_dict[letter], xor_result)

            #! going throuch each yellow bit and determining if there are enough copies left to keep it
            for bit_index, bit in enumerate(yellow_bits):
                if bit == 1 and unclaimed_copies > 0: #* there are copies left
                    unclaimed_copies -= 1
                elif bit == 1 and unclaimed_copies <= 0: #* no copies left
                    yellow_bits[bit_index] = 0

            for index, bit in enumerate(yellow_bits):
                if bit == 1:
                    color_feedback[index] = 'Y'

    return ''.join(color_feedback)

if __name__ == '__main__':
    try:
        print(get_color_feedback('llama', 'allot')) #* YGBBB [FAIL] should be YGYBB
    except ValueError as e:
        print(e)