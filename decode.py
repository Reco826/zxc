import requests
en_data = input("Enter text decode => : ")
print()
print('='*60)
print()
import requests

cookies = {
    '__test': '6c444b06c5080ab3ce337ae675806c10',
}

headers = {
    'Host': 'eslamhacker0.infinityfreeapp.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '182',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://eslamhacker0.infinityfreeapp.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Sec-GPC': '1',
    'Accept-Language': 'ar-EG,ar;q=0.5',
    'Referer': 'http://eslamhacker0.infinityfreeapp.com/Decrypted.php',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Cookie': '__test=6c444b06c5080ab3ce337ae675806c10',
}

data = {
    'Decrypted': en_data,
    'submit': '',
}

response = requests.post('http://eslamhacker0.infinityfreeapp.com/Decrypted.php', cookies=cookies, headers=headers, data=data)
#print(response.text)

from bs4 import BeautifulSoup

response_text = response.text


soup = BeautifulSoup(response_text, 'html.parser')
#print(soup)
response_div = soup.find_all('div')[0]

response_value = response_div.find_all('font')[1]
z=response_value.text
print(z)
