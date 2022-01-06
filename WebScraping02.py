from bs4 import BeautifulSoup
from plyer import notification
import requests
import time


if __name__ == "__main__":
    while True:
        try:
            url = requests.get("https://timesofindia.indiatimes.com/").text
            soup = BeautifulSoup(url, 'html.parser')
            articals = soup.find('div', attrs={'class': '_1CfcV'})
            art = articals.find('div', class_='col_l_6').text
            notification.notify(
                title = "** LATEST NEWS UPDATE  IS HERE !!**",
                message = (art),
                timeout = 10)

        except Exception as e:
            notification.notify(
                title = "** LATEST NEWS UPDATE  IS HERE !!**",
                message = (' THERE MUST BE SOME PROBLEM WITH WEBSITE '),
                timeout = 10)

        time.sleep(10800)
