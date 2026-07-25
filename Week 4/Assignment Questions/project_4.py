text = """
Nepal is a wonderful cnation. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for it's mountains and natural beauty.
"""


def word_frequency(text):

    text = text.lower()

    punctuation = ".,!?;:\n"

    for mark in punctuation:
        text = text.replace(mark, " ")

    words = text.split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # by Rahul Rimal

    sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    print("Top 3 words:\n")

    for word, count in sorted_words[:3]:
        print(word, "-", count, "times")


word_frequency(text)