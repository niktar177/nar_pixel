from PIL import Image

def nar_pixel(name, x, y):
    try:
        # Открываем изображение
        with Image.open(name) as img:
            # Проверяем координаты
            if x < 0 or x >= img.width or y < 0 or y >= img.height:
                raise ValueError(f"Координаты ({x}, {y}) выходят за пределы изображения "
                               f"({img.width}x{img.height})")
            
            # Получаем цвет пикселя
            pixel = img.getpixel((x, y))
            
            # Конвертируем в HEX в зависимости от режима изображения
            if img.mode == 'RGBA':
                # Для RGBA: 4 значения (R, G, B, A)
                return f'#{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}{pixel[3]:02x}'
            elif img.mode == 'RGB':
                # Для RGB: 3 значения (R, G, B)
                return f'#{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}'
            elif img.mode == 'L':
                # Для Grayscale: одно значение, дублируем для RGB
                return f'#{pixel:02x}{pixel:02x}{pixel:02x}'
            elif img.mode == 'LA':
                # Для Grayscale с альфа-каналом
                return f'#{pixel[0]:02x}{pixel[0]:02x}{pixel[0]:02x}{pixel[1]:02x}'
            elif img.mode == 'P':
                # Для палитровых изображений конвертируем в RGB
                rgb_pixel = img.convert('RGB').getpixel((x, y))
                return f'#{rgb_pixel[0]:02x}{rgb_pixel[1]:02x}{rgb_pixel[2]:02x}'
            else:
                # Для других режимов конвертируем в RGB
                rgb_pixel = img.convert('RGB').getpixel((x, y))
                return f'#{rgb_pixel[0]:02x}{rgb_pixel[1]:02x}{rgb_pixel[2]:02x}'
                
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{name}' не найден")
    except Exception as e:
        raise Exception(f"Ошибка при обработке изображения: {str(e)}")



