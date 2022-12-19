import urllib.request
site = urllib.request.urlopen('https://msk.spravker.ru/avtoservisy-avtotehcentry/').read().decode()
print(site)