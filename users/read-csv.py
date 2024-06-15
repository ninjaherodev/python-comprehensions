import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
        return data
           
if __name__ == '__main__':
   data = read_csv('./users/data.csv')
   print(data)