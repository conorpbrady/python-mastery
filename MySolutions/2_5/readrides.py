# readrides.py
import csv
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, i):
        if isinstance(i, slice):
            records = []
            if i.step is None:
                step = 1
            else:
                step = i.step
            for ii in range(i.start, i.stop, step):
                record = {
                        'route': self.routes[ii],
                        'day': self.dates[ii],
                        'daytype': self.daytypes[ii],
                        'rides': self.numrides[ii]
                        }
                records.append(record)
            return records

        elif isinstance(i, int):
            return {
                    'route': self.routes[i],
                    'date': self.dates[i],
                    'daytype': self.daytypes[i],
                    'rides': self.numrides[i]
                    }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['day'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            record = {
                    'route': row[0],
                    'day': row[1],
                    'daytype': row[2],
                    'rides': row[3]
                    }
            records.append(record)

    return records

def main():
    rows = read_rides_as_dicts('../../Data/ctabus.csv')
    r = rows[0:10]
    print(len(r))

if __name__ == '__main__':
    main()
