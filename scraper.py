import re

file1 = open('src.html', 'r')

text1 = file1.read().replace('\n', '').replace('\r', '').replace('</a>', '</a>\n')
text = '\n'.join(re.findall(f',? <a href=\"/artist/.*?\">(.+?)</a>', text1))
#text = text1.split('\n')

f = open('cleaned.html', 'w')
f.write(text)
f.close

artists = []
artist = ""

for line in range(len(text)):
    oa = re.search(r", <a href=\"/artist/.*?\">(.+?)</a>", text[line])
    if oa:
        artist = f'{artist}, {oa.group(1)}'

    a = re.search(r"<a href=\"/artist/.*?\">(.+?)</a>", text[line])
    if artist != "" and a and (not oa or line == len(text) - 2):
        artists.append(artist)
        artist = ""

    if artist == "" and a:
        artist = a.group(1)

tracks = re.findall(r"<a .*? href=\"/track/.*?\">(.+?)</a>", text1)

print('\n'.join(tracks))
print(f'Tracks: {len(tracks)}\n')
print('\n'.join(artists))
print(f'Artists: {len(artists)}\n')

total = zip(artists, tracks)

print('\n'.join(map(lambda x: f'{x[0]} - {x[1]}'.replace("&#x27;", "'"), total)))
print(f'Songs: {len(tracks)}')
