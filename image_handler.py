import requests
import pprint
from PIL import Image
from io import BytesIO


def get_image_from_name():
    params={
        'key':'AIzaSyBKV4ru8MuUJmvo3JRf-XhzcwYyBf6bx8M',
        'cx':'015680093206351405511:notwdjcaeve',
        'q':'lush bath bombs Harajuku'}
    data = requests.get('https://www.googleapis.com/customsearch/v1?',
                        params).json()
    image_url = data['items'][0]['pagemap']['product'][0]['image']
    print(image_url)
    return image_url


def get_image_colour(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    colors_values = img.getcolors(256)
    for c in colors_values:
        print(c)


if __name__ == '__main__':
    get_image_colour(get_image_from_name())