from popcat_wrapper import *
import utils
from io import BytesIO
from requests import get

url = "https://cdn.discordapp.com/avatars/551786741296791562/2550e13a9d81e958225d7cd909838c0f.webp?size=2048"
url2 = "https://cdn.discordapp.com/avatars/577009668266917937/a_0f9bb20bfe09e60a7159eaac1ce555d4.gif?size=2048"

card = welcomecard("https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png", "Your mom gay bruh", "jk jk", "lol", url)

def test():
  r = get("https://api.popcat.xyz/quote")
  data = r.json()

  return data

print(test()['quote'])