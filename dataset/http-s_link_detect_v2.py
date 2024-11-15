import re

# The email content as a string
email_content = """
Here are some example links:
www.example.com
ftp://fileserver.com/resource
192.168.0.1/test
127.0.0.1:8080/path
example.com
duskgytldkxiuqc6.onion
https://dgdfg.com
https://dgdfg.net.gdf
http://dgdfg.gfggd
itu.edu.tr
merhaba bu bir cumle. fsdfs
dgd.net@ffsf.com
"""

# Regex to detect all types of URLs
url_pattern = (
    r"((?:https?://|ftp://|www\.)?"  # Optional protocol or "www."
    r"(?:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Domain names like example.com
    r"|[a-zA-Z2-7]{16}\.onion|[a-zA-Z2-7]{56}\.onion|"  # .onion addresses
    r"\d{1,3}(?:\.\d{1,3}){3})"  # IPv4 addresses
    r"(?::\d+)?"  # Optional port
    r"(?:/\S*)?)"  # Optional path
)

# Find all URLs in the email content
urls = re.findall(url_pattern, email_content)

# Print the extracted URLs
for url in urls:
    print(url)
