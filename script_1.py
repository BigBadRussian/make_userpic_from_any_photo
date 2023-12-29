from PIL import Image


def prepare_image(filename=None):
    """Функция подготавливает изображение к преобразованиям.
    В базовом виде, по заданию, код сдвигает на абсолютное значение, и результат на картинках
    с высоким разрешением будет малозаметен. Так, как количество писклей должно быть целым,
    задачей функции является необходимое и достаточное изменение размера исхзодного изображения до размеров, кратных 50
    """
    if filename:
        image = Image.open(filename)
        if image.mode == "CMYK":
            image = image.convert("RGB")
        width = 50 * round(image.width / 50)
        height = 50 * round(image.height / 50)
        new_size = (width, height)
        image = image.resize(new_size)
        return image
    if not filename:
        return None


def make_red_part(red_image=None):
    crop_coordinates_left_red = (int(red_image.width * 0.1), 0, red_image.width, red_image.height)
    crop_coordinates_middle_red = (int(red_image.width * 0.05), 0, int(red_image.width * 0.95), red_image.height)
    red_image_left = red_image.crop(crop_coordinates_left_red)
    red_image_middle = red_image.crop(crop_coordinates_middle_red)
    red_image_blended = Image.blend(red_image_left, red_image_middle, 0.5)
    return red_image_blended


def make_blue_part(blue_image=None):
    crop_coordinates_right_blue = (0, 0, int(blue_image.width * 0.9), blue_image.height)
    crop_coordinates_middle_blue = (int(blue_image.width * 0.05), 0, int(blue_image.width * 0.95), blue_image.height)
    blue_image_right = blue_image.crop(crop_coordinates_right_blue)
    blue_image_middle = blue_image.crop(crop_coordinates_middle_blue)
    blue_image_blended = Image.blend(blue_image_right, blue_image_middle, 0.5)
    return blue_image_blended


def make_green_part(green_image=None):
    crop_coordinates_green = (int(green_image.width * 0.05), 0, int(green_image.width * 0.95), green_image.height)
    green_cropped = green_image.crop(crop_coordinates_green)
    return green_cropped


def make_new_image():
    image = prepare_image(filename="photo.jpg")
    red_image, green_image, blue_image = image.split()
    new_image = Image.merge("RGB", (make_red_part(red_image), make_green_part(green_image), make_blue_part(blue_image)))
    new_image.save("new_photo_blended.jpg")
    new_image.thumbnail((80, 80))
    new_image.save("new_photo_blended_small_size.jpg")


if __name__ == "__main__":
    make_new_image()
