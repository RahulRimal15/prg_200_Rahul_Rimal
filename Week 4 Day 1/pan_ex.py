import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braud, Mr.Owen Harris",
            "Allen, Mr.William Henry",
            "Bonnell, Miss Elizabeth",     
        ],
        "Age": [22,35,57],
        "Sex": ["male","male","female"],
    }

)

print("Maximum age is:", df["Age"].max())

print(df)

age=pd.Series([22,35,57],name="Age")
print(age)

print("Minimum Age:", age.min())
print("Maximum Age:", age.max())
print("Average Age:", age.mean())

