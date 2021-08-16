import requests as r
from PIL import Image

url = "https://cdn.discordapp.com/avatars/577009668266917937/a_0f9bb20bfe09e60a7159eaac1ce555d4.gif?size=2048"
url2 = "https://cdn.discordapp.com/avatars/551786741296791562/2d5f6241ac5106f0f7f1a93daeb58fb9.webp?size=2048"

def clown(image):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/drip?image={x}"

	return url
	
print(clown(url2))