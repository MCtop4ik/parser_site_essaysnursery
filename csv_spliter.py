with open('data.csv') as file:
    lines = file.read().splitlines()


def write_line(filename, csv_line):
    with open(filename + '.csv', 'w') as f:
        f.write(csv_line)


for i, line in enumerate(lines):
    write_line(str(i), line)


"""
>sqlite3 -header -csv parser.db "select * from onlinenursingessays;" > tracks.csv
"""
