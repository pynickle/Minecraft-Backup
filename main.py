import os
from time import strftime
import json
import zipfile
from nswebdav.sync import NutstoreDav

with open("config.json", "r", encoding="utf-8") as f:
    res = json.load(f)

login = res["login"]
password = res["password"]
dirpath = res["dirpath"]

dav = NutstoreDav()
dav.config(auth_tuple=(login, password))

time = strftime(" %Y-%m-%d,%H-%M-%S")
target = os.path.basename(dirpath) + time + ".zip"

f = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(dirpath):
    fpath = root.replace(dirpath, '')
    for file in files:
        f.write(os.path.join(root, file), os.path.join(fpath, file))
f.close()

with open(target, "rb") as f:
    dav.mkdir("/Minecraft")
    dav.upload(f.read(), "/Minecraft/" + target)

dav.close()

print("Backup successfully!")
