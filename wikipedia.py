from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text

browser = webdriver.Chrome()
browser.get('https://www.wikipedia.org')


def get_article_count_text(article_count, article_lang):
    ml = []
    # for el in range(len(article_count)):
    for i in range(len(article_lang)):
        x = ''
        for j in article_count[i].text:
            if j.isdigit():
                x += j
            else:
                continue
        art_list = x + ' - ' + article_lang[i].text
        ml.append(art_list)
    return ml

def get_sorted_by_count(x):
    for el in x:
        el = el.split()
        x.sort(key=el[0])
    return x

def get_max_count(article_count_list, n):
    ml = []
    for i in range(0,n):
        ml.append(article_count_list[i])
    return ml

def main():
    article_count = browser.find_elements(By.CSS_SELECTOR, '.central-featured-lang>a>small')
    article_lang = browser.find_elements(By.CSS_SELECTOR, '.central-featured-lang>a>strong')

    article_count_list = get_article_count_text(article_count, article_lang)
    article_count_list.sort(reverse=True, key=lambda el: el.split())
    print(get_max_count(article_count_list, 5))
    
    browser.close()

print(main())






