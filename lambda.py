def order(sentence):
    if not sentence:
        return ""  # Return an empty string for an empty input
    
    # Split the sentence into words
    words = sentence.split()

    # Sort the words based on the numbers present in each word
    sorted_words = sorted(words, key=lambda x: [int(char) for char in x if char.isdigit()])
    

    # Join the sorted words into a string
    result = " ".join(sorted_words)

    return result

# Examples
result1 = order("is2 Thi1s T4est 3a")
print(result1)  # Output: "Thi1s is2 3a T4est"

result2 = order("4of Fo1r pe6ople g3ood th5e the2")
print(result2)  # Output: "Fo1r the2 g3ood 4of th5e pe6ople"

result3 = order("")
print(result3)  # Output: ""