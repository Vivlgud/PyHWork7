# from import_export import read_data
# from function import print_data

def search_data (word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None