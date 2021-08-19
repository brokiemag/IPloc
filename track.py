import requests
import folium
import requests
import sys
import webbrowser
import bs4

res=requests.get('https://ipinfo.io/')
data=res.json()
print(data)

