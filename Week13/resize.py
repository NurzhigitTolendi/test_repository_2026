from PIL import Image

# Открываем изображение
image = Image.open('homelander.png')

# Указываем новый размер (ширина, высота)
new_size = (1200, 2700)

# Изменяем размер изображения, используя метод бикубической интерполяции для лучшего качества
resized_image = image.resize(new_size, Image.BICUBIC)

# Сохраняем измененное изображение под новым именем
resized_image.save('homelander_resized2.png')

print("Размер изображения успешно изменен!")