from PIL import Image

im = Image.open("assets/images/streamworld.png")
im1 = im.resize((300, 300))
im1.save("assets/images/streamworld1.png")
