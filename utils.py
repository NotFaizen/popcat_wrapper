def replaced(msg):
  return msg.replace(" ", "+")

def pngImage(URL):
  x = URL.replace("webp?size=2048","png").replace("gif?size=2048","png").replace("webp?size=4069","png").replace("png?size=4069","png")

  return x