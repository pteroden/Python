"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    good = []
    bad = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for i in range(3):
            reader.next()['productionStartYear']

        for line in reader:
            if line['productionStartYear'] != "NULL":
                try:
                    if 1886 < int(line['productionStartYear'].split("-")[0]) < 2014:
                        line['productionStartYear'] = int(line['productionStartYear'].split("-")[0])
                        good.append(line)
                    else:
                        bad.append(line)
                except:
                    bad.append(line)
            else:
                bad.append(line)

    def write(output_file, header, data):
        with open(output_file, "w") as output:
            writer = csv.DictWriter(output, delimiter=",", fieldnames = header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    write(output_good, header, good)
    write(output_bad, header, bad)



def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()