import os
import pandas as pd

main_dir_path = './spamassassindataset'
dir_list = os.listdir(main_dir_path)

data_list = []

ham_count = 0
spam_count = 0

os.chdir(main_dir_path)
for i_dir in dir_list:
    os.chdir("./" + i_dir)
    file_list = os.listdir()

    spam_detect = 1 if i_dir.split('_', 1)[1].find("ham") == -1 else 0 #spam 1, ham 0

    for file_path in file_list:
        try:
            with open(file_path, 'r', encoding='ISO-8859-1') as file:
                content = file.read()
                data_package = [content, spam_detect]
                data_list.append(data_package)
                if spam_detect == 1:
                    spam_count = spam_count + 1
                elif spam_detect == 0:
                    ham_count = ham_count + 1
        except Exception as e:
            print("Error: " + file_path + " \nException: "  + repr(e) )
            exit(1)

    os.chdir("../")
os.chdir("../")

df = pd.DataFrame(data_list, columns=['Content', 'Label'])
df.to_csv("spamassassin_dataset.csv", encoding='utf-8', index=False)

exit(0)