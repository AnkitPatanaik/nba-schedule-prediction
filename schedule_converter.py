import csv

filename = '2022_2022_NBA_Schedule.txt'
# filename = 'test.txt'
HEADERS = ["GAME", "DAY", "DATE", "VISITOR", "HOME", "LOCAL_TIME", "EASTERN TIME"]

def read_file():
    schedule = []

    with open(filename) as file:
        for line in file:
            one_line = line.rstrip()
            split = one_line.split()
            relevant_info = split[0:7]
            schedule.append(relevant_info)
    print(schedule)
    return schedule

def write_to_csv(data):
    with open('out/schedule.csv', 'w') as target:
        writer = csv.writer(target)
        writer.writerow(HEADERS)
        writer.writerows(data)

schedule_data = read_file()
write_to_csv(schedule_data)
