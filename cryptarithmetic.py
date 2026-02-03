from itertools import permutations

def solve_cryptarithmetic():
    word1 = input("Enter the first word (e.g., SEND): ").upper()
    word2 = input("Enter the second word (e.g., MORE): ").upper()
    result_word = input("Enter the result word (e.g., MONEY): ").upper()
    letters = sorted(set(word1 + word2 + result_word))
    if len(letters) > 10:
        print("Error: Too many unique letters. Maximum allowed is 10.")
        return
    for perm in permutations(range(10), len(letters)):
        digit_assignment = {letter: digit for letter, digit in zip(letters, perm)}
        if digit_assignment[word1[0]] == 0 or digit_assignment[word2[0]] == 0 or digit_assignment[result_word[0]] == 0:
            continue
        def word_to_number(word):
            return sum(digit_assignment[letter] * (10 ** (len(word) - i - 1)) for i, letter in enumerate(word))

        num1 = word_to_number(word1)
        num2 = word_to_number(word2)
        result_num = word_to_number(result_word)
        if num1 + num2 == result_num:
            print("Solution found:")
            for letter in letters:
                print(f"{letter} = {digit_assignment[letter]}")
            return
    print("No solution found.")
solve_cryptarithmetic()
