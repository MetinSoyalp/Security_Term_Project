import re
import pandas as pd

separate_re = r'(?m)^From ([^\n]+)\n^Return-Path: ([^\n]+)((?:\n(?!From ).*)*)'

file_path = './nazario/phishing-2015.txt'
file_content = ""

try:
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        file_content = file.read()
except Exception as e:
    print("Error: " + file_path + " \nException: "  + repr(e) )
    exit(1)

email_list = re.findall(separate_re, file_content)

data_list = []

for i_mail in email_list:
    content = "From " + i_mail[0] + "\n"
    content = content + "Return-Path: " + i_mail[1]
    content = content + i_mail[2]

    data_list.append([content, 1])

df = pd.DataFrame(data_list, columns=['Content', 'Label'])
df.to_csv("nazario_2015_dataset.csv", encoding='utf-8', index=False)

