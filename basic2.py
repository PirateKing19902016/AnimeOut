import certifi
import urllib3
from bs4 import BeautifulSoup

link = "https://www.animeout.xyz/inuyashiki/"

http = urllib3.PoolManager( cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET', link)
page_soup = BeautifulSoup(r.data, "html.parser")

all_a=page_soup.findAll("a")
link_list=[]
for direct_download in all_a:
    if direct_download.text == "Direct Download":
        #print(direct_download.attrs['href'])
        link_list.insert(len(link_list), direct_download.attrs['href'])

excess = "http://public.animeout.xyz/"
mod_link_list = []
for link in link_list:
    mod_link = excess + link[7:]
    mod_link_list.insert(len(mod_link_list), mod_link)


for link in mod_link_list:
    print(link)

