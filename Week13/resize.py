from PIL import Image

# open the image
image = Image.open('gus.png')

# set new size (width, height)
new_size = (40, 90)

# change the image size 
resized_image = image.resize(new_size, Image.BICUBIC)

# saving the new image with the new name
resized_image.save('gus_resized.png')

print("The image size changed successfully!")