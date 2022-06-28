import os
import requests
from urllib.parse import urlparse, quote, unquote
from bs4 import BeautifulSoup as Soup

GET = "GET"
POST = "POST"
store = {}
sesi = requests.session()


def req_json(url, method, *args, **kwargs):
    urlp = urlparse(url)
    global store
    global sesi

    if urlp.hostname not in store:
        store[urlp.hostname] = {}

    if "cookies" not in kwargs and urlp.hostname in store:
        kwargs["cookies"] = store[urlp.hostname] 
    

    if method == GET:
        resp = sesi.get(url, *args, **kwargs)
        while resp.headers.get("location", None) != None:
            url = resp.headers.get("location")
            resp = sesi.get(url, *args, **kwargs)


        store[urlp.hostname] = resp.cookies
        if resp.status_code == 200:
            
            return resp.json()
        else:
            return {}

    elif method == POST:
        resp = sesi.post(url, *args, **kwargs)
        while resp.headers.get("location", None) != None:
            url = resp.headers.get("location")
            resp = sesi.post(url, *args, **kwargs)

        store[urlp.hostname] = {}
        if resp.status_code == 200:
            
            return resp.json()
        else:
            return {}

def req_html(url, method, *args, **kwargs):
    urlp = urlparse(url)
    global store
    global sesi

    if urlp.hostname not in store:
        store[urlp.hostname] = {}

    if "cookies" not in kwargs and urlp.hostname in store:
        kwargs["cookies"] = store[urlp.hostname] 
    

    if method == GET:
        resp = sesi.get(url, *args, **kwargs)
        while resp.headers.get("location", None) != None:
            url = resp.headers.get("location")
            resp = sesi.get(url, *args, **kwargs)


        store[urlp.hostname] = resp.cookies
        if resp.status_code == 200:
            
            return Soup(resp.content.decode("utf-8"), features="lxml")
        else:
            return Soup("", features="lxml")

    elif method == POST:
        resp = sesi.post(url, *args, **kwargs)
        while resp.headers.get("location", None) != None:
            url = resp.headers.get("location")
            resp = sesi.post(url, *args, **kwargs)

        store[urlp.hostname] = {}
        if resp.status_code == 200:
            
            return Soup(resp.content.decode("utf-8"), features="lxml")
        else:
            return Soup("", features="lxml")


get_base = "https://bimasislam.kemenag.go.id/jadwalshalat"
post_kabupaten = "https://bimasislam.kemenag.go.id/ajax/getKabkoshalat"
post_jadwal = "https://bimasislam.kemenag.go.id/ajax/getShalatbln"

cookies = {} 
this = sesi.get(get_base)
cookies = this.cookies


html_base = req_html(get_base, GET, cookies=cookies)
provinsi = {}
for element in html_base.find("select", {"id":  "search_prov"}).find_all("option"):
    provinsi.update({
        element.text: {
            "token": element.get("value"),
            "kabupaten": {},
            }
    }) 
