"""Configuration for the project"""


class Config:
    manifest_version = 2
    name = 'Exposify'
    version = '1.0'
    description = ('Adds a red border and a warning to a webpage that '
                   'has been makred as a fake local news site')
    icons = {'48': 'icons/border-48.png'}
    content_scripts = [
        {
            'matches': [],
            'js': ['exposify.js']
        }
    ]
