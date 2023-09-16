# readrides.py
import csv
from collections import namedtuple

class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

class RowSlots:
        __slots__ = ['route', 'date', 'daytype', 'rides']
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

RowTuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a string of tuples'''

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
        return records

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

def read_rides_as_class(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            row_c = Row(row[0], row[1], row[2], row[3])
            records.append(row_c)
    return records

def read_rides_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            row_t = RowTuple(row[0], row[1], row[2], row[3])
            records.append(row_t)
    return records

def read_rides_as_class_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            row_c = RowSlots(row[0], row[1], row[2], row[3])
            records.append(row_c)
    return records

if __name__  == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('../../Data/ctabus.csv')
    print('Tuples | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_dict('../../Data/ctabus.csv')
    print('Dict | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_class('../../Data/ctabus.csv')
    print('Class | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_named_tuples('../../Data/ctabus.csv')
    print('Named Tuple | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_class_slots('../../Data/ctabus.csv')
    print('Class Slots | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
