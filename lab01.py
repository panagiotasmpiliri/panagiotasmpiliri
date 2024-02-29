import requests  # εισαγωγή της βιβλιοθήκης
    
def more(text):
    count = 0
    for l in text.split('\n'):
        print(l)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = 'http://python.org/'  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)
    
