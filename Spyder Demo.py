# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 04:27:57 2018

@author: huangjingwei
"""



def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def get_next_target(page):
    start_link = page.find('<a href=')
#    if start_link == -1:
#        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote
#url, end_endpos = get_next_target 
        
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
     
  
#print get_page('https://www.douban.com/people/65585379/')
print print_all_links(get_page('https://www.douban.com/people/65585379/'))


