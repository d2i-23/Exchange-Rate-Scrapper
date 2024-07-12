from time import sleep
import pandas as pd 
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

cryptoList = {
    "BTC-USD" : "https://www.google.com/finance/quote/BTC-USD?hl=en", 
    "ETH-BTC" : "https://www.google.com/finance/quote/ETH-BTC?hl=en",
    "XRP-BTC" : "https://www.google.com/finance/quote/XRP-USD?hl=en", 
    "XRP-ETH" : "https://www.google.com/finance/quote/BTC-ETH?hl=en", 
    "XRP-USD" : "https://www.google.com/finance/quote/XRP-USD?hl=en",
    "ETH-USD"  : "https://www.google.com/finance/quote/ETH-USD?hl=en"
}
minuteWait = 10
time = 'America/Toronto'
fileName = "entries.csv"

def collectHTMLValue(url):
    with sync_playwright() as p:
        
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html = page.content()  # Retrieve the HTML content of the page
        browser.close()

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_= "YMlKec fxKbKc")
        
        if div:
            value_str = div.get_text(strip=True)  # Return the HTML content of the div as a string

            cleaned_str = value_str.replace(',', '')

            value_float = float(cleaned_str)

            return value_float
        else:
            return 0
        
def collect(cryptoList, timezone):

    container = {}
    utc_now = datetime.now(pytz.utc)
    timeZone = pytz.timezone(timezone)
    toronto_time = utc_now.astimezone(timeZone)

    formatted_time = toronto_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    container["time"] = [formatted_time]
    
    for key, value in cryptoList.items():
        container[key] = [collectHTMLValue(value)]

    return container

def main():

    seconds = minuteWait * 60

    dataHold = pd.DataFrame()

    try: 
        print("Starting collecting process...")

        while True:
            content = collect(cryptoList, time)

            for key, value in content.items():
                print(key, value[0])
            print("\n")

            dataHold = pd.concat([dataHold, pd.DataFrame(content)], axis = 0)

            dataHold.to_csv(fileName)

            print("CSV Updated \n")

            sleep(seconds)

    except KeyboardInterrupt:

        print("Ending process...")

    finally:
        # Perform cleanup or final tasks when the process ends
        print("Ended Program")
        

if __name__ == "__main__":
    
    main()