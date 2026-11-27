#Import libraries
import io
from PIL import Image
import pytesseract
import requests


def main():
    url = "http://[IP]:16036/image.php"
    session = requests.Session() #Get session
    response = session.get(url)
    response.raise_for_status()
    cookies_dict = response.cookies.get_dict() #get cookies as a dictionary
    #print(cookies_dict)

    image = Image.open(io.BytesIO(response.content)) #Open image
    image.save("code.png") # save it to recognize
    text = pytesseract.image_to_string(image, config='--psm 10') # recognize the image
    print("CODE:", text.strip()) # print the code to be sure of our actions

    body = {
        "answer": text.strip()
    } # put the code to the body of request

    post = requests.post(url, cookies=cookies_dict, data=body) # send it back 
    print("COOKIE:",cookies_dict) 
    
    print("CODE STATUS:", post.status_code) # look for good status
    print("CONTENT:", post.headers) # get content 


if __name__ == "__main__":  # main func
    main()
