from PIL import Image

i = Image.open('solids.png')
imgSize = i.size
rawData = i.tobytes()
img = Image.frombytes('L', imgSize, rawData)
img.save('lmode.png')
i.close()

i2 = Image.open('lmode.png')
