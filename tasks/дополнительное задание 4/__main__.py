import re
import urllib.request
import csv

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry"
response = urllib.request.urlopen(url)
text = response.read().decode()

names = r"(?:title-link\">)(?P<title>[^<]*)"
locations = r"(?:location\">)(?P<address>[^<]*)"
phones = r"(?:Телефон(?:.*[\s]*)[^\d]*)(?P<phone>[^<]*)"
working = r"(?:Часы работы(?:.*\s*[^>]*).)(?P<work>[^<]*)"

found_names = re.findall(names, text)
found_locations = re.findall(locations, text)
found_phones = re.findall(phones, text)
found_working = re.findall(working, text)

print(len(found_phones), len(found_locations))

with open("parsed.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "location", "phone", "work hours"])
    for i in range(len(found_names)):
        row = [found_names[i].strip(), found_locations[i].strip(), found_phones[i].strip(), found_working[i].strip()]
        print(row)
        writer.writerow(row)
