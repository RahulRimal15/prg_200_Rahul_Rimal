marks=[]

for i in range(20):
    mark = int(input(f"Enter marks of Student {i + 1}: "))
    marks.append(mark)

for i in range(20):
    print(f"Student {i + 1}")
    print("Marks:", marks[i])

    if marks[i]>=90:
        print("Distinction")
    elif marks[i]>=75:
        print("First Division")
    elif marks[i]>=60:
        print("Second Division")
    elif marks[i]>=35:
        print("Third Division")
    else:
        print("Fail")