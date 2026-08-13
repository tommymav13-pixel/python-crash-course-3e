def make_album(artist_name, album_title, album_number = None):
        """Return a dictionary of information about an album."""
        album_01 = {'artist': artist_name, 'title': album_title}

        if album_number: 
            album_01['number'] = album_number
        return album_01

album = make_album('metallica', 'master of puppets', 'battery')
print(album)

album = make_album('ed sheeran', 'play', 'a little more')
print(album)

album = make_album('linkin park', 'the emptiness machine', 
                   'the emptiness machine')
print(album)