import csv

list1 = [["Top Gun", "Risky Business", "Minority Report"],
         ["Titanic", "The Revenant", "Inception"],
         ["Training Day", "Man on Fire", "Flight"]]

with open("9_3.csv", "w") as f:
    w = csv.writer(f, delimiter = ",")

    for v in list1:
        w.writerow(v)


