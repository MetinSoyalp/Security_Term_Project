from email import message_from_string
import re
import pandas as pd

df = pd.read_csv("./1_processed_datasets/spamassassin_dataset.csv")

email = df.iloc[0, 0]

msg = message_from_string(email)

from_address = msg.get('From')
to_address = msg.get('To')
subject = msg.get('Subject')
date = msg.get('Date')

body = msg.get_payload()

keys = msg.keys()

print(keys)

#print("From:", from_address)
#print("To:", to_address)
#print("Subject:", subject)
#print("Date:", date)
#print("Body:\n", body)

