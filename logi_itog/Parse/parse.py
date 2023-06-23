import os
import re
import json

def reader(filename):
    ip_regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    date_regexp = r'\d{1,2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path) as f:
        log = f.read()
        ips_list = re.findall(ip_regexp, log)
        dates_list = re.findall(date_regexp, log)
    
    data = {
        "IPs": ips_list,
        "Dates": dates_list
    }

    json_data = json.dumps(data, indent=4)
    with open('logs.json', 'w') as json_file:
        json_file.write(json_data)

    print("Data written to logs.json")

if __name__ == '__main__':
    reader('apach.log')
