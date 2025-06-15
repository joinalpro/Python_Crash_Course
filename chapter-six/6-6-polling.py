favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

new_list = ['sarah', 'nasir']

for name in sorted(favorite_languages.keys()):
    print(name.title())
    
    if name in new_list:
        print(name)