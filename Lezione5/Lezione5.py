#Create a Playlist
name: str = 'Road Trip'
songs: set = {'Song 1', 'Song 2'}
playlist: dict = {}
def create_playlist (name, songs):
    playlist[name] = songs
    return playlist
print (create_playlist(name, songs))

def add_like(dictionary, name, liked=True):
    if name in dictionary:
        dictionary[name]["liked"] = liked
    return dictionary

print('\n')

