import argparse

parser = argparse.ArgumentParser(description='trying to complete a task')
parser.add_argument('-c', '--city', help='write a city', required=True)
parser.add_argument("input_file", default=None, help=("Input file to read"))
parser.add_argument("output_file", default=None, help=("Output file to read"))

args = parser.parse_args()

def capitalize(string):
    string = string.upper()
    return string

def task_CLI(city, input_file, output_file):
    with open(input_file, encoding='utf-8') as first_file:
        for line in first_file:
            result = ('Where are you?' + '\n' + city + '\n' + capitalize(line) + '\n')
    
    with open(output_file, mode='w', encoding='utf-8') as new_file:
        new_file.write(result)
       
task_CLI(args.city, args.input_file, args.output_file)
