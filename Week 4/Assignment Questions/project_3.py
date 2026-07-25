bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan",
    "Bhadra", "Ashwin", "Kartik", "Mangsir",
    "Poush", "Magh", "Falgun", "Chaitra"
]

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]


def convert_date(date_str, from_cal, to_cal):

    if from_cal == to_cal:
        return date_str

    year, month, day = date_str.split("-")

    year = int(year)
    month = int(month)

    if from_cal == "AD" and to_cal == "BS":
        year = year + 56

    elif from_cal == "BS" and to_cal == "AD":
        year = year - 56

    # by Rahul Rimal

    return str(year) + "-" + month.__str__().zfill(2) + "-" + day


for customer in customers:

    converted = convert_date(
        customer["date"],
        customer["cal"],
        customer["need"]
    )

    if customer["style"] == "full" and customer["need"] == "BS":

        year, month, day = converted.split("-")
        month_name = bs_months[int(month) - 1]

        print(customer["name"], "| Original:",
              customer["date"], customer["cal"],
              "| Converted:", day + " " + month_name + ",",
              year, "BS")

    else:

        print(customer["name"], "| Original:",
              customer["date"], customer["cal"],
              "| Converted:", converted,
              customer["need"])