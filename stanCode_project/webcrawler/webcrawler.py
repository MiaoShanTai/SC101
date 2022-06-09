"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('tbody')[0].find_all('tr')
        lst = []
        for tag in tags[0:-1]:
            for td in tag.find_all('td'):
                lst.append(td.text)
        male = 0
        for i in range(2, len(lst), 5):
            ans = ''
            for j in lst[i]:
                if j != ',':
                    ans += j
            male += int(ans)
        print('Male Number:',male)
        female = 0
        for i in range(4, len(lst), 5):
            ans = ''
            for j in lst[i]:
                if j != ',':
                    ans += j
            female += int(ans)
        print('Female Number:', female)


if __name__ == '__main__':
    main()
