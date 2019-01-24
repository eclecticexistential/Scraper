from PIL import Image
import requests
from io import BytesIO
import io
import os

response = requests.get('https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fassets1.ignimgs.com%2F2017%2F06%2F20%2Fstreetfightermk-1280-1497998503464_1280w.jpg&f=1')
img = Image.open(BytesIO(response.content))
img.save('image.jpg')
with open('image.jpg','rb') as img_file:
	reader = img_file.read()
	b = bytearray(reader)
	print(b[0])
	### save binary image data to db here ###
	imageStream = io.BytesIO(b)
	imageFile = Image.open(imageStream)
	imageFile.show()
os.remove('image.jpg')