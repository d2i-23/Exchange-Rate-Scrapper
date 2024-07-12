# Exchange-Rate-Scrapper

This program scapes exchange values of crypto currencies from google finance. 

To start the program, create a python virtual environment as instructed from the guide: https://docs.python.org/3/library/venv.html

```
python -m venv c:\path\to\myenv\bitScan
```

Once the environment is inside this folder, type the following commands:

```
cd c:\path\to\myenv\bitScan\.venv\Scripts

activate
```

This will activate the environment, and to install the needed libraries and commands, enter: 

```
python install.py
```

When the installations are complete, go to main.py and adjust these variables to your liking 

**cryptoList** - dictionary that contains the exchange item and the corresponding link from google finance to scrape

**minuteWait** - what is the interval of which the exchange rates are changed (ex, 10 means check every 10 minutes)

**time** - to specify the timezone logged (Check https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568 for available timezone options)

**fileName** - csv file where the values will be saved to

Start the process through: 

```
python main.py
```
Terminate the program whenever you are satisfied with the entries on the entry csv that stores the periodic exchange values. 
