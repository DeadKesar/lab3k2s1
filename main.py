import requests
import re


if __name__ == '__main__':
    r = requests.get('https://edu.stankin.ru/mod/assign/view.php?id=324317')
    html = r.text
    print(html)