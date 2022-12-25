import os
import zipfile

def main():
    while True:
        zipped_levels_path = input('Enter the path of the folder where the zipped levels are located:    ')
        if not os.path.exists(zipped_levels_path):
            print('Invalid path')
        else:
            break

    while True:
        to_unzip_path = input('Enter the path to your BeatSaber custom levels folder:    ')
        if not os.path.exists(to_unzip_path):
            print('Invalid path')
        else:
            break

    if zipped_levels_path[-1] != '/': zipped_levels_path += '/'
    if to_unzip_path[-1] != '/': to_unzip_path +=  '/'

    try:
        levels = os.listdir(zipped_levels_path)
        len_levels = len(levels)
        for i in range(len(levels)):
            level = levels[i]
            if level[-4:] != '.zip': continue
            print(f'({i + 1} / {len_levels}) Unzipping {zipped_levels_path + level}...')
            with zipfile.ZipFile(zipped_levels_path + level, 'r') as f:
                f.extractall(to_unzip_path + level[:-4])

    except:
        print('An unknown error has occured')
        return False

    input('\n\n\nOperation successful. Press enter to close this program...    ')
    return True

while True:
    if main(): break