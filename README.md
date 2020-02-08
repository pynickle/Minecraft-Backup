## Backup For Minecraft Worlds

The project makes backup for Minecraft worlds on nutstore(jianguoyun). It depends on [nswebdav](https://github.com/vanbas/nswebdav) package.

## How To Use

First, you should install nswebdav package on [github.com/vanbas/nswebdav](https://github.com/vanbas/nswebdav).

Second, you should add an third-party application on [safety page](https://www.jianguoyun.com/#/safety)

Third, add your account, third-party application password and the Minecraft world location in your computer which you want to backup in config.json like this:
```json
{
    "login": "<account>",
    "password": "<password>",
    "dirpath": [
        "<.../saves/...>",
        "<.../saves/...>"
    ]
}
```

At last, you can run the main.py program and find your zip backup in the Minecraft folder.