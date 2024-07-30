import csv

def read_csv(fn, delimiter):
    with open(fn, mode = "r", newline = "") as csv_f:
        counter = -1
        for line in csv_f:
            row = line.strip().split(delimiter)
            if counter == -1:
                print(f'{ " | ".join(row)}')
            else:
                print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
            counter += 1
        print(f"{counter} lines")

def write_csv(fn, header, row):
    with open(fn, mode = "w", newline = "") as csv_f:
        writer = csv.writer(csv_f, delimiter=",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

# read_csv("./Files/names.csv", ",")
write_csv("./Files/names2.csv", ["name", "lastname", "age", "sex"], ["Foo", "Fighter", "82", "male"])