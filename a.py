def count_sign_changes(sequence):
    changes = 0

    for i in range(1, len(sequence)):
        if sequence[i - 1] * sequence[i] < 0:
            changes += 1

    return changes

def average_numbers(sequence):
    negative_sum = 0
    negative_count = 0
    non_negative_sum = 0
    non_negative_count = 0

    for num in sequence:
        if num < 0:
            negative_sum += num
            negative_count += 1
        else:
            non_negative_sum += num
            non_negative_count += 1

    if negative_count > 0:
        average_negative = negative_sum / negative_count
        print(f"Среднее арифметическое отрицательных чисел: {average_negative}")

    if non_negative_count > 0:
        average_non_negative = non_negative_sum / non_negative_count
        print(f"Среднее арифметическое неотрицательных чисел: {average_non_negative}")

def analyze_text(text):
    words = text.split()
    word_counts = {}
    max_word = ""
    max_word_length = 0

    for word in words:
        clean_word = word.strip('.,!?"\'').lower()

        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

            if len(clean_word) > max_word_length:
                max_word_length = len(clean_word)
                max_word = clean_word

    most_common_word = max(word_counts, key=word_counts.get)

    print(f"Наиболее часто встречающееся слово: {most_common_word}")
    print(f"Самое длинное слово: {max_word}")

# Пример использования
sequence_input = input("Введите последовательность чисел, разделенных пробелами, и заканчивающуюся 0: ")
sequence = list(map(int, sequence_input.split()))
result = count_sign_changes(sequence)
print(f"Количество смен знака: {result}")

sequence_for_average_input = input("Введите последовательность чисел, разделенных пробелами, и заканчивающуюся -1000: ")
sequence_for_average = list(map(float, sequence_for_average_input.split()))
average_numbers(sequence_for_average)

text_input = input("Введите текст: ")
analyze_text(text_input)
