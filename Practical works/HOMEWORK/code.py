import re
import shutil
import urllib.request
site = urllib.request.urlopen('https://msk.spravker.ru/avtoservisy-avtotehcentry/').read().decode()
pattern_name = r'class="org-widget-header__title-link">([\w\W]*[^<]?)<\/a>'
with open('avto.txt', mode='r', encoding = 'utf-8') as avto:
    avto = avto.read()
    match = re.findall(pattern_name, avto)
    print(match)
# with open('site.txt')

