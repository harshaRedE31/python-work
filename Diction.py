#dictionarie used to store data values in key value pairs , they are unordered, mutable, no duplicate keuys, keys canot be listtypele
info = {
  "key": "valeue",
  "name": "harsa",
  "age": 21,
  "isSigmaMAle": True,
  "hobbies": ["watche movies", "playing chess"]
}
# print(info)
# print(type(info))
# print(info["isSigmaMAle"])
# print(list(info.keys()))
# print(len(list(info.keys())))
# print(info.values())
# print(list(info.values()))
print(info.items())
pairs = list(info.items())
print(pairs[0])
print(info.get("name"))
info.update({"city":"Banglore","state":"Karnataka"})
print(info)


student ={
  "nam":"arsh",
  "subs":{
    "phy":99,
    "chem":98
  }
}
# print(student["subs"]["phy"])