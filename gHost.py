import requests as rq
import string

def main():
    letters = [c for c in string.printable if c not in "#/?"]
    url = "http://192.169.2.100:16094/"

    while True:
        for i in letters:
            req = rq.get(url+i)
            if req.status_code == 200:
                url = url+i
                print(url)
            else:
                pass    

if __name__ == "__main__":
    main()
