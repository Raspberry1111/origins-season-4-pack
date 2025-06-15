import json



data = None
with open("modrinth.index.json", "r") as f:
    data = json.loads(f.read())


files = []

for i in data["files"]:
    files += i["downloads"]
    # if len(i["downloads"]) > 1:
        # print(i["downloads"])

print("\n".join(files))
