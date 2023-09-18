import tableformat
import csv

class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, num_shares):
        self.shares -= num_shares
        return self.shares

def read_portfolio(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            records.append(Stock(row[0], int(row[1]), float(row[2])))
    return records

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    header = '---------'
    print('%10s %10s %10s' % (header, header, header))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

def main():
    portfolio = read_portfolio('../../Data/portfolio.csv')
    tableformat.print_table(portfolio, ['name', 'shares', 'price'])

if __name__ == '__main__':
    main()
