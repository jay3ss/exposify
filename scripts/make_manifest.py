"""Writes the manifest.json file for the extension"""
import json

from config import Config


keys = [key for key in Config.__dict__.keys() if not key.startswith('_')]
manifest_json = {}
for key in keys:
    manifest_json[key] = getattr(Config, key)

with open('list.txt', 'r') as f:
    site_list = f.read()

url_list = []
for site in site_list.split('\n'):
    url_list.append(f'*://*.{site}/*')

manifest_json['content_scripts'][0]['matches'] = url_list

with open('../manifest.json', 'w') as f:
    json.dump(manifest_json, f)
