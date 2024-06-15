import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        total_gastos = 0
        for row in reader:
            total_gastos += int(row[1])
            print(row)
        return total_gastos
        # data = []
        # for row in reader:
        #     iterable =zip(header, row)
        #     country_dict = {key:value for key,value in iterable}
        #     data.append(country_dict)
        # return data
           
if __name__ == '__main__':
   read_csv('./users/salary.csv')
  