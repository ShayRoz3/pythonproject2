import random
import urllib.request
def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.png'
    urllib.request.urlretrieve(url, full_name)

download_web_image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/200px-PNG_transparency_demonstration_1.png')