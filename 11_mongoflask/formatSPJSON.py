import json

f = open("unformattedSPJSON.json", "r")
#resets to zero
f.seek(0)
data = f.readlines()
data = data[0][1:-1].split("},{")

for idx in range(len(data)):
    print (data[idx])
    toLoad = ("{" + data[idx] + "}")
    data[idx] = json.loads(toLoad)

tempf = open("southpark.json", "w")
tempf.write(json.dumps(data))
