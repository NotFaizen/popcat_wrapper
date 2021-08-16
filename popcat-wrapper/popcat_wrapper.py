import requests as r

# /country endpoint 
def country(name, property=None):
	x = r.get(f'https://api.popcatdev.repl.co/countries/{name}')
	"""Gives info on the provided country. The name field is the country name and the property field is which attribute of the country you want (eg: currency, flag, etc)

	properties: name, domain, calling_codes, capital, region, population, area, flag, currency.name, currency.short, currency.symbol"""
	if property == None:
		return x.json()
	elif property == "currency.name":
		return x.json()['currency']['name']
	elif property == "currency.symbol":
		return x.json()['currency']['symbol']
	elif property == "currency.short":
		return x.json()['currency']['short']
	else:
		return x.json()[f'{property}']

# /banner endpoint
def banner(ID):
	x = r.get(f'https://api.popcatdev.repl.co/banners/{ID}')
	"""Returns a user's banner"""

	return x.json()['banner']

# /npm endpoint
def npm(name,property=None):
	x = r.get(f"https://api.popcatdev.repl.co/npm?q={name}")
	"""Returns info on any package registered on npmjs.org. The name field is the name of the package you want info about

	properties: name, version, description, keywords, author, author_email, last_published, maintainers, repository, downloads_this_year"""

	if property == None:
		return x.json()
	else:
		return x.json()[f'{property}']

# /fact endpoint
def fact(property=None):
	x=r.get("https://api.popcatdev.repl.co/fact")
	if property == None:
		return x.json()
	else:
		return x.json()[f'{property}']

# /instagram endpoint
def instagramUser(user, property=None):
	x = r.get(f"https://api.popcatdev.repl.co/instagram?user={user}")
	if property == None:
		return x.json()
	else:
		return x.json()[f'{property}']

# /drake endpoint
def drake(text1, text2):
	# local vars
	x = text1.replace(" ", "+")
	y = text2.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/drake?text1={x}&text2={y}"

	# not local vars?
	return url

# /pooh endpoint
def pooh(text1,text2):
	# local vars i suppose?
	x = text1.replace(" ", "+")
	y = text2.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/pooh?text1={x}&text2={y}"

	# EZ Clap copy pasta :OMEGALUL:
	return url

# /ship endpoint
def ship(user1,user2):
	# not local vars lol
	x = user1.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	y = user2.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/ship?user1={x}&user2={y}"

	return url

# /colorify endpoint
def colorify(image, color):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/colorify?image={x}&color={color}"

	return url

# /biden endpoint
def biden(text):
	x = text.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/biden?text={x}"

	return url

# /joke endpoint
def joke(property=None):
	x = r.get('https://api.popcatdev.repl.co/joke')
	if property == None:
		return x.json()
	else:
		return x.json()[property]

# /pikachu endpoint
def pikachu(text):
	x = text.replace(" ", "+")
	url = f"https://api.popcatdev.repl.co/pikachu?text={x}"

	return url

# /drip endpoint
def drip(image):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url = f"https://api.popcatdev.repl.co/drip?image={x}"

	return url

def clown(image):
	x = image.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")
	url f"https://api.popcatdev.repl.co/drip?image={x}"

	return url