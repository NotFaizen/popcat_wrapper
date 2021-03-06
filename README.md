# popcat_wrapper

## Community
Join [our server](https://discord.gg/UFsejAWMmJ) if you want to have fun or need any help!

## Installation
```
pip install popcat-wrapper
```
## Examples

### Randomfacts command, no input example:
```py
import discord
from discord.ext import commands
from popcat_wrapper import popcat_wrapper as pop
bot = commands.Bot(command_prefix=">")

@bot.command()
async def randomfacts(ctx):
  res = await pop.randomfacts()

  await ctx.send(res)

bot.run("discord bot token")
```

### Pikachu command, one input example:

```py
import discord
from discord.ext import commands
from popcat_wrapper import popcat_wrapper as pop
bot = commands.Bot(command_prefix=">")

@bot.command()
async def pikachu(ctx):
  text = "String"
  image = await pop.pikachu(text)

  await ctx.send(image)

bot.run("discord bot token")
```

### Drake meme command, more than one text input example: 
```py
import discord
from discord.ext import commands
from popcat_wrapper import popcat_wrapper as pop
bot = commands.Bot(command_prefix=">")

@bot.command()
async def drake(ctx):
  text = "String"
  text2 = "String 2"
  image = await pop.drake(text, text2)

  await ctx.send(image)

bot.run("discord bot token")
```
### Ad command, image input example:
```py
import discord
from discord.ext import commands
from popcat_wrapper import popcat_wrapper as pop
bot = commands.Bot(command_prefix=">")

@bot.command()
async def drake(ctx, member: discord.Member=None):
  if member == None:
    member = ctx.author
  pfp = member.avatar_url_as(size=128)
  image = await pop.ad(pfp)

  await ctx.send(image)

bot.run("discord bot token")
```

### Country command, object input example
```py
from popcat_wrapper import popcat_wrapper as pop

color = "ffcc99"
res = await pop.country(name="canada")

print(res)

```
Output example: 
```yaml
{
 "name": "Canada",
 "domain": ".ca",
 "calling_codes": "1",
 "capital": "Ottawa",
 "region": "Northern America",
 "population": "36,155,487",
 "area": "9,984,670 Square KM",
 "flag": "https://api.popcatdev.repl.co/countries/canada/flag",
 "currency": {
  "short": "CAD",
  "name": "Canadian dollar",
  "symbol": "$"
 }
}
```
If you want to get data from a specific property (for example domain), you need to replace `pop.country(name="canada")` with `pop.country(name="canada", property="domain")`. You may have noticed that there is a sub object within the main one, you may ask "How do i get data from a property inside the sub object?"; here's how:

You use `pop.country(name="canada", property="currency.propertyname")`. 

For example: `pop.country(name="canada", property="currency.symbol")`.

This method applies to Playstore, iTunes, WouldYouRather, RandomMeme, instagramUser, car, npm, banner, country, weather, github and Colorinfo.

### Welcome card
```py
import discord, aiohttp, asyncio
from discord.ext import commands
from popcat_wrapper import popcat_wrapper as pop
bot = commands.Bot(command_prefix=">")

@bot.command()
async def welcomecard(ctx):
  image = await pop.welcomecard(background,text1,text2,text3,)

  await ctx.send(image)

bot.run("discord bot token")
```

## Endpoints
You can get a full list of the possible API endpoints [Here](https://api.popcatdev.repl.co)
But here is the list:

- `drake(text1, text2)`
- `pooh(text1, text2)`
- `ship(image1, image2)`
- `colorify(image, color)`
- `biden(text)`
- `pikachu(text)`
- `drip(image)`
- `clown(image)`
- `ad(image)`
- `blur(image)`
- `invert(image)`
- `greyscale(image)`
- `jokeoverhead(image)`
- `mnm(image)`
- `translate(text, language)`
- `reverse(text)`
- `alert(text)`
- `caution(text)`
- `mock(text)`
- `facts(text)`
- `encode(text)`
- `decode(binary)`
- `doublestruck(text)`
- `texttomorse(text)`
- `playstore(app, property)`
- `itunes(song, property)`
- `npm(name, property)`
- `instagramUser(user, property)`
- `car(property)`
- `colorinfo()`
- `welcomecard(background, text1, text2, text3, avatar)`
- `joke()`
- `randommeme()`
- `fact()`
- `_8ball()`
- `wanted(image)`
- `simp(image)`
- `lulcat(text)`
- `weather(location, property)`
- `opinion(image, text)`
- `pet(image)`
- `url_shortener(url, extension)`
- `screenshot(url)`
- `github(user, property)`
- `whowouldwin(image1, image2)`

## Credits
Made with <3 (and python) by reset#0002 and NotFaizen#2005

Join Our Discord Server! [Link](https://dsc.gg/popcatcom)


