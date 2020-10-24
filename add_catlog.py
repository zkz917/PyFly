import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["ipig"]

mycol = mydb["catalogs"]

mydict = [
    {"name": "求助", "id": 2},
    {"name": "话题", "id": 3},
    {"name": "资源", "id": 4},
    {"name": "招聘", "id": 5},
    {"name": "爱好", "id": 6},
    {"name": "科学", "id": 7},

]

x = mycol.insert_many(mydict)

mycol1 = mydb["passageways"]

mydict1 = [
    {"name": "中国农业大学", "url": "www.cau.edu"},
    {"name": "爱猪联盟", "url": 'http://www.ypccau.com'},

]

x1 = mycol1.insert_many(mydict1)