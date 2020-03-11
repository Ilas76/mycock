from PIL import Image
import asyncio
import os

def scale_image(input_image_path,output_image_path,width=None,height=None):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size



def plus_background(input, output):
    card = Image.new("RGBA", (512, 512), (0,0,0))
    img = Image.open(input).convert("RGBA")
    x, y = img.size
    k = int(((512-x)/2))
    card.paste(img, (k, 0), img)
    card.save(output, format="png")

def result(input, output):

    i = str(str(input)+"del.png")
    scale_image(input_image_path=input ,output_image_path=i,width=512, height=512)
    plus_background(i, output)
    os.remove(i)
