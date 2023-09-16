# readport.py

import csv
from collections import Counter, defaultdict

def read_rides_as_dict(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            obj = {
                    'route': row[0],
                    'date': row[1],
                    'daytype': row[2],
                    'rides': int(row[3])
                    }
            records.append(obj)
    return records

def number_riders(rows, route, date):
   return sum([row['rides'] for row in rows if row['route'] == route and row['date'] == date])

def main():
    rows = read_rides_as_dict('../../Data/ctabus.csv')
    print("1. How many bus routes exist in Chicago?")
    print(len({ row['route'] for row in rows }))
    print("2. How many people rode the number 22 bus on February 2, 2011?  What about any route on any date of your choosing?")
    print(number_riders(rows, '22', '02/02/2011'))
    print("3. What is the total number of rides taken on each bus route?")
    totals = Counter()
    for row in rows:
        totals[row['route']] += row['rides']
    print(totals)
    print("4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?")

    rides = defaultdict(Counter)
    for row in rows:
        year = row['date'][-4:]
        rides[year][row['route']] += row['rides']
    delta = rides['2011'] - rides['2001']
    for route, delta in delta.most_common(5):
        print(route, delta)

if __name__ == '__main__':
    main()
