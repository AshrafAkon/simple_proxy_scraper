#the algorithms that I used there just get the work done. you are always welcome to make it better. 
#this script is used to scrap working proxy from https://free-proxy-list.net/ 
#what you do with the proxy is in your concern
from selenium import webdriver
import time
import urllib.request as request
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
url = 'http://bot.whatismyipaddress.com/'   

def give_proxy(n):
    if n <= 10:
        proxy_driver = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options) #replace ./chromedriver.exe to ./chromedriver for debian linux
        proxy_driver.get("https://free-proxy-list.net/")
        raw_proxy = proxy_driver.find_element_by_id("proxylisttable").text.split("\n")[1:11]
        proxy_driver.quit()
        simplified_proxy = []

        for i in raw_proxy:
            a = i.split(" ")
            simplified_proxy.append(a[0]+":"+a[1])
        
        fresh_proxy = []
        
        for proxy_host in simplified_proxy:    
            if len(fresh_proxy) <= n:
                try:
                    req = request.Request(url)
                    req.set_proxy(proxy_host, 'http')

                    response = request.urlopen(req)
                    working_proxy = response.read().decode('utf-8')

                    if working_proxy == proxy_host.split(":")[0]:
                        print("proxy Connected")
                        fresh_proxy.append(proxy_host)
                        print(len(fresh_proxy))
                    else:
                        print("proxy not connected")
                except:
                    print("pao")

            if len(fresh_proxy) == n:
                print("done")
                break

            print(len(fresh_proxy))
        if len(fresh_proxy) > 0:
            return fresh_proxy
        else:
            print("no fresh proxy\n")

