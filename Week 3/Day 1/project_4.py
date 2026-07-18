def average_score(*marks):
    total = sum(marks)
    average = total / len(marks)

    # by Rahul Rimal

    return average


number_of_subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(number_of_subjects):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

result = average_score(*marks)
print("Average Score:", result)