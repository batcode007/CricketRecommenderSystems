"""
Scripts to help load the movielens dataset into Python classes
"""
import re

# Read data/README to get more info on these data structures
class User:
    def __init__(self, id,name, age, sex, zip):
        self.id = int(id)
        self.name = name
        self.age = int(age)
        self.sex = sex
        self.zip = zip
        self.avg_r = 0.0

# Read data/README to get more info on these data structures
class Item:
    def __init__(self, id, name, age, Indian, Pakistani, SouthAfrican, Australian, WestIndian, SriLankan, Bowler, \
    Batsmen, WicketKeeper):
        self.id = int(id)
        self.name = name
        self.age = int(age)
        self.Indian = int(Indian)
        self.Pakistani = int(Pakistani)
        self.SouthAfrican = int(SouthAfrican)
        self.Australian = int(Australian)
        self.WestIndian = int(WestIndian)
        self.SriLankan = int(SriLankan)
        self.Bowler = int(Bowler)
        self.Batsmen = int(Batsmen)
        self.WicketKeeper = int(WicketKeeper)

# Read data/README to get more info on these data structures
class Rating:
    def __init__(self, user_id, item_id, rating):
        self.user_id = int(user_id)
        self.item_id = int(item_id)
        self.rating = int(rating)

# The dataset class helps you to load files and create User, Item and Rating objects
class Dataset:
    def load_users(self, file, u):
        f = open(file, "r")
        text = f.read()
        entries = re.split("\n+", text)
        for entry in entries:
            e = entry.split('|', 5)
            if len(e) == 5:
                u.append(User(e[0], e[1], e[2], e[3], e[4]))
        f.close()

    def load_items(self, file, i):
        f = open(file, "r")
        text = f.read()
        entries = re.split("\n+", text)
        for entry in entries:
            e = entry.split('|', 12)
            if len(e) == 12:
                i.append(Item(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], \
                e[11]))
        f.close()

    def load_ratings(self, file, r):
        print 'check1'
        f = open(file, "r")
        text = f.read()
        print 'check2'
        entries = re.split("\n+", text)
        for entry in entries:
            print 'check3'
            e = entry.split('|', 3)
            if len(e) == 3:
                print 'check4'
                r.append(Rating(e[0], e[1], e[2]))
        f.close()