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

print("Load Config Successfully")

dav = NutstoreDav()
dav.config(auth_tuple=(login, password))

time = strftime(" %Y-%m-%d,%H-%M-%S")
for path in dirpath:
    target = os.path.basename(path) + time + ".zip"

    f = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        fpath = root.replace(path, '')
        for file in files:
            f.write(os.path.join(root, file), os.path.join(fpath, file))
    f.close()

    print(f"Make {target} Zipfile Successfully")

    with open(target, "rb") as f:
        dav.mkdir("/Minecraft")
        dav.upload(f.read(), "/Minecraft/" + target)

dav.close()

print("Backup successfully!")
os.system("pause")
