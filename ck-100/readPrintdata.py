from readFunctions import *

import sys
import time
import math
import re
import pickle

import numpy as np

from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# Store data in arrays
user = []
item = []
rating = []
rating_test = []

# Load the movie lens dataset into arrays
d = Dataset()
d.load_users("u.user", user)
d.load_items("u.item", item)
# d.load_ratings("u2.base", rating)
# d.load_ratings("u2.test", rating_test)

n_users = len(user)
n_items = len(item)
print n_users
print n_items

