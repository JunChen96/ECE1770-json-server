import json
  
# Opening JSON file
# with open('db.json') as json_file:
#     data = json.load(json_file)
  
#     # Print the type of data variable
#     print("Type:", type(data))
  
data = {}
d = {
    "id": 0,
    "description": "1th Waltz by Mike Paer.",
    "image": "https://i.ibb.co/7YGYgpb/waltz.jpg",
    "name": "Waltz 1",
    "animation_url": "https://www.mboxdrive.com/Mike%20Paer%20-%20Waltz.mp3"
  }

lst = []
for i in range(50):
	d["id"] = i
	d["description"] = str(i) + "th Waltz by Mike Paer."
	d["name"] = "Waltz " + str(i)
	lst.append(d)


data['tokens'] = lst

print(data['tokens'])

with open('new.json', 'w') as fp:
	json.dump(data, fp)



'''
[
  {
    "id": 0,
    "description": "Demo NFT - Bahen Building, the building of Engineering and Computer Science",
    "external_url": "https://junchen96.github.io/",
    "image": "https://i.ibb.co/J5K5Nd6/bahen.jpg",
    "name": "Bahen NFT ",
    "animation_url": "https://www.mboxdrive.com/Mike%20Paer%20-%20Waltz.mp3"
  },
  {
    "id": 1,
    "description": "/UofT NFT by CJ",
    "external_url": "https://junchen96.github.io/",
    "image": "https://i.ibb.co/GpT4gSS/UofT.jpg",
    "name": "Kyle NFT 2",
    "animation_url": "https://www.mboxdrive.com/Mike%20Paer%20-%20Waltz.mp3"
  },
  {
    "id": 2,
    "description": "1th Waltz by Mike Paer. First music track nft minted on Kyle Token(KYT).",
    "external_url": "https://junchen96.github.io/",
    "image": "https://i.ibb.co/7YGYgpb/waltz.jpg",
    "name": "Waltz 1",
    "animation_url": "https://www.mboxdrive.com/Mike%20Paer%20-%20Waltz.mp3"
  },
  {
    "id": 3,
    "description": "2th Waltz by Mike Paer. First music track nft minted on Kyle Token(KYT).",
    "external_url": "https://junchen96.github.io/",
    "image": "https://i.ibb.co/7YGYgpb/waltz.jpg",
    "name": "Waltz 2",
    "animation_url": "https://www.mboxdrive.com/Mike%20Paer%20-%20Waltz.mp3"
  }
]
'''