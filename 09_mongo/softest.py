from bson.json_util import loads

json_str = '[{"name": "Company", "_id": {"$oid": "5899e0aca600741755433908"}, "info": {"email": "test@gmail.com"}}]'
print (type(json_str))

data = loads(json_str)
print(data)
