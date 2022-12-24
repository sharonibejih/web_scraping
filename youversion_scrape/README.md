# Scraper for YouVersion Languages for NLP Tasks
[YouVersion](https://www.bible.com/) is a bible app that has different bible versions and languages.

This project is focused on scraping bible corpus from YouVersion across different languages - currently Igbo. 


#### Disclaimer
- The code in the notebook unfortunately, did not work across all (a few) books and chapters. So, it might have to be improved.
- The copyright for webscraping YouVersion, to use as a dataset, is not clearly [stated](https://help.youversion.com/l/en/article/o8t2xmy9q2-copyright). 

### How to reproduce this for other languages

1. Choose a version from here:
https://www.bible.com/versions

In this project, I worked with this: https://www.bible.com/versions/77-igbob-bible-nso 

2. When you open the version of your choice, like mine for example, the first two links you will see are: Read Version and Audio Version. Select the Read Version and that's mostly it. It should look similar to this, for Genesis 1: https://www.bible.com/bible/77/GEN.1.IGBOB 

3. The url format used in this project `url = f"https://www.bible.com/bible/77/{book_abbrv}.{chpt}.{version}"` is the same across all versions. Simply ensure that the `version` variable defined at the beginning of the notebook is changed to fit into yours. Mine is `IGBOB`.


### To-Dos to contribute to
1. Improve the webscraper for books and chapters that return `YouVersion uses cookies to personalize your experience. By using our website, you accept our use of cookies as described in our Privacy Policy.` instead of the actual bible content.

2. Convert the codes to an API.


### License
This project is licensed under the terms of the Creative Commons license family.
