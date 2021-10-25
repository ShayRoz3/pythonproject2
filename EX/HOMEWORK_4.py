import random
n = random.randint(1,1000)
print(n)
#choose a random number

#import urllib.request(url = local_pic,
#local_pic = urllib.request("https://she-codes.org/wp-content/uploads/2018/11/cropped-unnamed-1-1.png/")
#my_file = n + local_pic + ".png"

import urllib.request
image_url =  "https://she-codes.org/wp-content/uploads/2018/11/cropped-unnamed-1-1.png/"
urllib.request.urlretrieve(url=image_url, filename='266.png')

