import requests
import re


if __name__ == '__main__':
    r = requests.get('https://edu.stankin.ru/mod/assign/view.php?id=324317')
    html = r.text
    res = re.findall(
        r'\b(?:https|http|www)[\.\:\/]{1,3}[-a-zA-Z0-9@:%_\+.~#?&\/=]{2,256}\.[a-z]{2,4}\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&\/=]*)?',
        html)
    for i in res:
        print(i)