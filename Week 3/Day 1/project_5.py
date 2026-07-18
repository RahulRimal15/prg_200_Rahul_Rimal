def build_profile(name, **details):
    print("\nStudent Profile")
    print("Name:", name)

    # by Rahul Rimal

    for key, value in details.items():
        print(f"{key}: {value}")


name = input("Enter student name: ")
program = input("Enter program: ")
year= input("Enter year: ")
email = input("Enter email: ")
build_profile(
    name,
    Program=program,
    Year=year,
    Email=email
)