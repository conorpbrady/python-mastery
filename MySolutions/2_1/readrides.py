# readrides.py
import csv
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
if __name__  == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('../../Data/ctabus.csv')
    print('Tuples | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.clear_traces()
    rows = read_rides_as_dict('../../Data/ctabus.csv')
    print('Dict | Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
