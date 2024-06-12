import csv
import pandas as pd
import matplotlib.pyplot as plt


def first_programme():
    print("Hello World")


def declare_variables():
    a = 1
    string = "This is a string"
    boolean_var = True

    print(type(a))


def string_practice():
    first = "Python"
    second = "bootcamp"

    new = first + second.upper()

    print(new)


def conditional_statements():
    n = 100

    if n <= 10:
        print(str(n) + " is not less than 10")
    else:
        print(str(n) + " is greater than 10")


def loop_practice():
    for i in range(0, 11):
        print(i)

    n = 10

    while n > 0:
        print(n)
        n -= 1


def read_from_csv():
    path = "data/cars.csv"

    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for line in reader:
            print(line)


def read_csv_with_headings():
    path = "data/cars_with_headings.csv"

    with open(path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row)


def write_csv_with_headings():
    path = "data/new_car_record.csv"

    data = {"Manufacturers": "Polestar", "Founded": 2017, "Headquarters": "Gothenburg", "Sales": 54600}
    field_names = data.keys()

    with open(path, 'w', newline='') as csvfile:
        dictwriter = csv.DictWriter(csvfile, field_names)

        dictwriter.writeheader()
        dictwriter.writerow(data)


def draw_bar_chart():
    path = "data/cars_with_headings.csv"

    df = pd.read_csv(path)

    plt.title("Car Sales in 2023")
    plt.xlabel("Manufacturers")
    plt.ylabel("Sales (in million)")
    plt.bar(df['Manufacturers'], df['Sales'])

    plt.show()


if __name__ == "__main__":
    #first_programme()
    #declare_variables()
    #string_practice()
    #conditional_statements()
    #loop_practice()
    #read_from_csv()
    #read_csv_with_headings()
    #write_csv_with_headings()
    draw_bar_chart()



