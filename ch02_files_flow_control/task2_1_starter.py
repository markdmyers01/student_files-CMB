"""

      task2_1_starter.py   -   Baseball player salaries

      Reads data from multiple files.  Determines the top salaries for
      a specified year between 1985 and 2016.

      Salaries.csv file format:  yearID,teamID,lgID,playerID,salary
      People.csv   file format:  playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID

"""
from collections import namedtuple
import os
import sys

# working_dir = './resources/baseball/'
people_filename = './resources/baseball/People.csv'
salaries_filename = './resources/baseball/Salaries.csv'

input_year = 0
salaries = []
players = {}


def salary_sort(sal_record):
    return sal_record.salary


year_str = '2004' # input('Enter a year (1985-2016): ')

# filepath = os.path.join(working_dir, salaries_filename) 
# print(filepath)
try: 
    with open(salaries_filename, encoding='utf-8') as f_sal:
        header = f_sal.readline().strip().split(',') 
        SalaryRecord = namedtuple('SalaryRecord', header) 
        for line in f_sal: 
            data = line.strip().split(',') 
            if year_str == data[0]: 
                try: 
                    data[4] = int(data[4]) 
                except ValueError: 
                    data[4] = 0 
                sal_rec = SalaryRecord(*data) 
                salaries.append(sal_rec)
except IOError as err: 
    print(err, file=sys.stderr) 
    sys.exit()

# people_filepath = os.path.join(working_dir, people_filename) 
try: 
    with open(people_filename, encoding='utf-8') as f_people: 
        for line in f_people: 
            data = line.strip().split(',') 
            player_id, first_name, last_name = data[0], data[13], data[14] 
            players[player_id] = (first_name, last_name) 
except IOError as err: 
    print(err, file=sys.stderr) 
    sys.exit()

salaries.sort(key=salary_sort, reverse=True)

how_many = 10 
print_header = ['Name', 'Salary', 'Year'] 
sal_total = []

print('\033[1m\033[94m{0:35}{1:>20}{2:>10}\033[0m'.format(*print_header))
print('\033[1m\033[94m{0:-<65}\033[0m'.format('')) 

for salary_record in salaries[:how_many]: 
    player_id = salary_record.playerID
    first_name, last_name = players[player_id] 
    name = first_name + ' ' + last_name 
    salary = f'${salary_record.salary:,}' 
    year = salary_record.yearID 
    print(f'\033[93m{name:35}{salary:>20}{year:>10}\033[0m')

    sal_total.append(salary_record.salary)
sum_total = sum(sal_total)
print('\033[1m\033[94m{0:-<65}\033[0m'.format(''))
print('\033[1m\033[94m{0:35}{1:>20}\033[0m'.format('Total Salary:', f'${sum(sal_total):,}'))
print('\n\n')