import pymongo
import xml.etree.ElementTree as ET

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.PreCog_DB

# create collections
tags_col = db["tags"]
badges_col = db["badges"]
posts_col = db["posts"]
users_col = db["users"]
votes_col = db["votes"]

# Paths to files
tags_tree = ET.parse("../stackoverflow.com/Tags.xml")
badges_tree = ET.parse("../stackoverflow.com/Badges.xml")
posts_tree = ET.parse("../stackoverflow.com/Posts.xml")
users_tree = ET.parse("../stackoverflow.com/Users.xml")
votes_tree = ET.parse("../stackoverflow.com/Votes.xml")

# target elements
tags = tags_tree.findall('row')
badges = badges_tree.findall('row')
posts = posts_tree.findall('row')
users = users_tree.findall('row')
votes = votes_tree.findall('row')


# insert TAGS
for elem in tags:
    data = [{}]
    for attr in elem.attrib:
        data[0][attr] = elem.attrib[attr]
    print(data[0]["Id"])

    x = tags_col.insert(data)

# insert BADGES
for elem in badges:
    data = [{}]
    for attr in elem.attrib:
        data[0][attr] = elem.attrib[attr]
    print(data[0]["Id"])

    x = badges_col.insert(data)

# insert POSTS
for elem in posts:
    data = [{}]
    for attr in elem.attrib:
        data[0][attr] = elem.attrib[attr]
    print(data[0]["Id"])

    x = posts_col.insert(data)

# insert USERS
for elem in users:
    data = [{}]
    for attr in elem.attrib:
        data[0][attr] = elem.attrib[attr]
    print(data[0]["Id"])

    x = users_col.insert(data)

# insert VOTES
for elem in votes:
    data = [{}]
    for attr in elem.attrib:
        data[0][attr] = elem.attrib[attr]
    print(data[0]["Id"])

    x = votes_col.insert(data)
