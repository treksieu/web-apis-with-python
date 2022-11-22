import requests
from PIL import Image 
import io 

file = {"image": open("sample.jpg","rb")}
headers = {"type":"multipart/image"}

URL ="http://127.0.0.1:5000"
filter ="emboss"

response = requests.post(f"{URL}/{filter}",headers=headers, files=file)
response.raise_for_status


image = Image.open(io.BytesIO(response.content))
image.save("response.jpg","JPEG")
image