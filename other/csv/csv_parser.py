import csv
import os
import re


def parse_txt(text):
    regex = '(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}) (\d+\.\d+\.\d+\.\d+) (\d+).*(\d+) ([\w/]+)'
    match = re.findall(regex, text)
    return (match)


current_dir = os.getcwd()
files_dir = current_dir + '\\files'
checked_files = [x for x in os.listdir(files_dir) if x[:2] == 'sw']
files = list(map(lambda x: files_dir + '\\' + x, checked_files))
switch_names = list(map(lambda x: x[:x.index('_')], os.listdir(files_dir)))
csv_headers = ['switch', 'mac', 'ip', 'vlan', 'interface']
with open((current_dir + '\\parsed_text.csv'), 'wt') as out:
    writer = csv.writer(out)
    writer.writerow(csv_headers)
    for el, name in zip(files, switch_names):
        with open(el, 'rt') as f:
            info = parse_txt(f.read())
            for i in info:
                out_row = list(i)
                out_row.insert(0, name)
                writer.writerow(out_row)
