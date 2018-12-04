# Lexi Wiki

## Compare inline links across multilanguages

### Insert Words - translate.py
In translate.py, users can input English, German, Italian, and Arabic words in order, into their respective array.

### Get Links - wiki.py
In wiki.py, words from translate.py are cycled through in order and put into the function get_save_data.
From there, a folder is created with the chosen english word.
Then, the script scrapes the respective wikipedia page based on the language of origin.
During this time, the scraper collects inline wikipedia links that are exclusive to Wikipedia.
Furthermore, the scraper ignores image files.
The collected URLs are saved into a spreadsheet, named with the language [ar, en, it, de] prefix as well as the translated word.

### Get Final CSV file - get_sum_diff.py
Once the links are collected, get_sum_diff.py can be ran to consolidate the information.
During this process, all 4 files in each folder is saved into a combo spreadsheet.
To accomplish this in an organized fashion, each link is tagged with its respective language, page it was found on, translated word, and id.
The id reflects the order in which the link appeared on the web page.

### See the results
With the links numbered, users can put their created spreadsheet into google.sheets.
Upon viewing here, simply click the d column and alter the order by SORT A-Z.
By doing so, links will appear in order of their appearance on the web page.
Thus making it possible to compare the order of links across various versions of a wiki page.