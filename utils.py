from aiohttp import ClientSession

def replaced(msg):
  return msg.replace(" ", "+")

def pngImage(URL):
  x = URL.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png").replace("png?size=2048", "png").replace("webp","png").replace("jpg","png").replace("gif","png")

  return x
  
def cleanImage(URL):
  x = URL.replace("jpg","png").replace("gif","png").replace("webp","png")

































































def secretmsg():
  return "If you're getting this message, that means you have found the easter egg / secret; you are cool, believe it! (DM NotFaizen#3463 with screenshot proof for a cookie)"