import requests as r
import utils
import asyncio
from aiohttp import ClientSession
base_url = "https://api.popcat.xyz/"
base = "https://api.popcat.xyz/" 
# /country endpoint 
async def country(name, property=None):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/countries/{name}") as r:
      data = await r.json()

  """Gives info on the provided country. The name field is the country name and the property field is which attribute of the country you want (eg: currency, flag, etc)

  properties: name, domain, calling_codes, capital, region, population, area, flag, currency.name, currency.short, currency.symbol"""
  if property == None:
    return data
  elif property == "currency.name":
    return data['currency']['name']
  elif property == "currency.symbol":
    return data['currency']['symbol']
  elif property == "currency.short":
    return data['currency']['short']
  else:
    return data[f'{property}']

# /banner endpoint
async def banner(ID):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/banners/{ID}") as r:
      data = await r.json()
      return data['banner']

# /npm endpoint
async def npm(name,property=None):
  """Returns info on any package registered on npmjs.org. The name field is the name of the package you want info about

  properties: name, version, description, keywords, author, author_email, last_published, maintainers, repository, downloads_this_year"""
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/npm?q={name}") as r:
      data = await r.json()
      if property == None:
        return data
      else:
        return data[property]

# /fact endpoint
async def randomfact():
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/joke") as r:
      data = await r.json()
      return data['joke']
  
# /instagram endpoint
async def instagramUser(user, property=None):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/instagram?user={user}") as r:
      data = await r.json
      if property == None:
        return data
      else:
        return data[property]

# /drake endpoint
async def drake(text1, text2):
	# local vars
	x = text1.replace(" ", "+")
	y = text2.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/drake?text1={x}&text2={y}"

	# not local vars?
	return url

# /pooh endpoint
async def pooh(text1,text2):
	# local vars i suppose?
	x = text1.replace(" ", "+")
	y = text2.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/pooh?text1={x}&text2={y}"

	# EZ Clap copy pasta :OMEGALUL:
	return url

# /ship endpoint
async def ship(user1,user2):
	# not local vars lol
	x = user1.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	y = user2.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/ship?user1={x}&user2={y}"

	return url

# /colorify endpoint
async def colorify(image, color):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/colorify?image={x}&color={color}"

	return url

# /biden endpoint
async def biden(text):
	x = text.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/biden?text={x}"

	return url

# /joke endpoint
async def joke():
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/fact") as r:
      data = await r.json()
      return data['fact']

# /pikachu endpoint
async def pikachu(text):
	x = text.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/pikachu?text={x}"

	return url

# /drip endpoint
async def drip(image):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/drip?image={x}"

	return url

async def clown(image):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/drip?image={x}"

	return url

async def mock(text):
  msg = utils.replaced(text)
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/mock?text={msg}") as r:
      data = await r.json()
      return data['text']

async def translate(text, language):
  y = text.replace(" ", "+")
  async with ClientSession as cs:
    async with cs.get(f"https://api.popcatdev.repl.co/translate?text={y}&to={language}") as r:
      data = r.json()
      return data['translated']

async def reverse(text):
  text = utils.replaced(text)
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/reverse?text={text}") as r:
      data = r.json()
      return data['text']

async def uncover(image):
  image = utils.pngImage(image)
  url = f"{base_url}uncover?image={image}"
  return url

async def ad(image):
  image = utils.pngImage(image)
  url = f"{base_url}ad?image={image}"
  return url
  
async def blur(image):
  image = utils.pngImage(image)
  url = f"{base_url}blur?image={image}"
  return url

async def invert(image):
  image = utils.pngImage(image)
  url = f"{base_url}invert?image={image}"
  return url

async def greyscale(image):
  image = utils.pngImage(image)
  url = f"{base_url}grayscale?image={image}"
  return url

async def alert(text):
  # text = utils.replaced(text)
  # url = f"{base_url}alert?text={text}"
  return "Deprecated until further notice"

async def caution(text):
  text = utils.replaced(text)
  url = f"{base_url}caution?text={text}"
  return url

async def colorinfo(color,property=None):
  async with ClientSession() as cs:
    async with cs.get(f"https://api.popcat.xyz/color/{color}") as r:
      data = await r.json()
      if property == None:
        return data
      else:
        return data[property]

async def jokeoverhead(image):
  image = utils.pngImage(image)
  url = f"{base_url}jokeoverhead?image={image}"
  return url

async def mnm(image):
  image = utils.pngImage(image)
  url = f"{base_url}mnm?image={image}"
  return url

async def doublestruck(text):
  text = utils.replaced(text)
  url = f"{base_url}doublestruck?text={text}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      return data['text']

async def texttomorse(text):
  text = utils.replaced(text)
  url = f"{base_url}texttomorse?text={text}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      return data['morse']

async def wouldyourather(property=None):
  url = f"{base_url}wyr"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def randommeme(property=None):
  url = f"{base_url}meme"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def itunes(song, property=None):
  song = utils.replaced(song)
  url = f"{base_url}itunes?song={song}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def playstore(app, property=None):
  app = utils.replaced(app)
  url = f"{base_url}playstore?q={app}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      if property == None:
        return data
      else:
        return data[property]

async def binary_encode(text):
  text = utils.replaced(text)
  url = f"{base_url}encode?text={text}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      return data['binary']

async def binary_decode(binary):
  binary = utils.replaced(binary)
  url = f"{base_url}decode?binary={binary}"
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = r.json()
      return data['text']

async def facts(text):
  text = utils.replaced(text)
  url = f"{base_url}facts?text={text}"
  return url

async def _8ball():
  async with ClientSession as cs:
    async with cs.get(f"{base_url}8ball") as r:
      data = await r.json()
      return data['answer']

def welcomecard(background, text1, text2, text3, avatar):
  text1 = utils.replaced(text1)
  text2 = utils.replaced(text2)
  text3 = utils.replaced(text3)
  avatar = utils.pngImage(avatar)

  url = f"{base_url}welcomecard?background={background}&text1={text1}&text2={text2}&text3={text3}&avatar={avatar}"

  return url

async def sadcat(text):
  text = utils.replaced(text)
  url = f"{base_url}sadcat?text={text}"

  return url

async def oogway(text):
  text = utils.replaced(text)
  url = f"{base_url}oogway?text={text}"
  return url

async def communism(image):
  image = utils.pngImage(image)
  url = f"{base_url}communism?image={image}"

  return url

async def car(property=None):
  url = f"{base_url}car"

  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      if property == None:
        return data
      else:
        return data[property]

async def showerthoughts():
  url = f"{base}showerthoughts" 
  async with ClientSession() as cs:
    async with cs.get(url) as r:
      data = await r.json()
      return data['result']

async def quote():
  async with ClientSession() as cs:
    async with cs.get(f"{base}quote") as r:
      data = await r.json()
      return data['quote']



async def secret():
  return utils.secretmsg()