import json
import os

BASE_DIR = '.'
PLAYLISTS_DIR = os.path.join(BASE_DIR, 'playlists')
FAVORIES_FILE = 'content_favorites.lpl'
FAVORIES_FILE_PATH = os.path.join(BASE_DIR, FAVORIES_FILE)


def read_ipl_file(file_path):
    """
    Reads 'ipl' file and returns data from it

    param: file_path (str): path of ipl file
    """
    try:
        data = json.load(open(file_path))
        return data
    except:
        return None


def write_ipl_file(data, file_path):
    # write data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def append_item(item, file_path):
    """
    Appends item to 'ipl' file items

    param: item (dict): item that was found in favorites file
    param: file_path (str): 'ipl' file path where item needs to be appended
    """
    # read data from ipl file
    data = read_ipl_file(file_path)
    if not data:
        return

    # get all items from the data
    items = data['items']

    # remove already existing entry (if any)
    items = [d for d in items if d['label'] not in [
        item['label'], f'* {item["label"]}', f"*{item['label']}"]]

    # add aesterik to the label
    item['label'] = '* ' + item['label']

    # append item to the items
    items.append(item)

    # replace old items with new items
    data['items'] = items

    # write data back to the file
    write_ipl_file(data, file_path)


def main():
    # load all playlist files (names only)
    playlist_files = os.listdir(PLAYLISTS_DIR)

    # load data from favorites file
    favorites_data = read_ipl_file(FAVORIES_FILE_PATH)

    # get all items from favorites data
    items = favorites_data['items']

    # an empty list to store items that will not be appended
    items_to_keep = []

    # check for each item in favorites data
    for item in items:
        # check if the file exists in playlist files
        if item['db_name'] in playlist_files:
            db_file_path = os.path.join(PLAYLISTS_DIR, item['db_name'])

            # append item to the file
            append_item(item, db_file_path)

        else:
            items_to_keep.append(item)

    # update the items list to only contain items that were not appended
    favorites_data['items'] = items_to_keep

    # write data back to the file
    write_ipl_file(favorites_data, FAVORIES_FILE_PATH)

print("Favorites replaced!")

if __name__ == '__main__':
    main()
