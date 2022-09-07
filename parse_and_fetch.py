#
#  Minecraft assets downloader
#

import json
import os
import shutil

import requests


ASSETS_BASE_URL = 'http://resources.download.minecraft.net'


def download_objects(url, obj_hash):
    print(f'> Downloading {url} ...')

    filename = f'objects/{obj_hash[:2]}/{obj_hash}'

    if os.path.exists(filename):
        return
    try:
        os.makedirs(f'objects/{obj_hash[:2]}')
    except FileExistsError:
        pass
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


if __name__ == '__main__':
    with open('1.19.json', 'r') as f:
        assets = json.load(f)
    for obj_name in assets['objects'].keys():
        obj_hash = assets['objects'][obj_name]['hash']
        download_objects(f'{ASSETS_BASE_URL}/{obj_hash[:2]}/{obj_hash}', obj_hash)
