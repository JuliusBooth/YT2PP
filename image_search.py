import requests
import shutil
import os
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv('UNSPLASH_API_KEY')

def get_image_from_keyword(keyword):
    if keyword == '':
        return None
    filename = f'image/{keyword}.jpg'
    if os.path.exists(filename):
        return filename
    url = f'https://api.unsplash.com/search/photos?page=1&query={keyword}&client_id={access_key}'
    response = requests.get(url).json()
    results = response['results']
    if len(results) == 0:
        return None
    image_url = results[0]['urls']['full']  # get the url of the first image in results

    response = requests.get(image_url, stream=True)
    
    if response.status_code == 200:
        response.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        print('Image successfully downloaded.')
    else:
        print('Image couldn\'t be downloaded.')

    return filename