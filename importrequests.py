import requests
from PIL import Image 
import io 

file = {"image": open("sample.jpg","rb")}
headers = {"type":"multipart/image"}

URL ="https://treky.herokuapp.com/"

filter ="blur"

response = requests.post(f"{URL}/{filter}",headers=headers, files=file)
response.raise_for_status


image = Image.open(io.BytesIO(response.content))
image.save("response.jpg","JPEG")
image