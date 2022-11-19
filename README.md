# Add Free Licenses

This repository contains Python code to automatically [add free licenses][steamdb-free-packages] on Steam.

## Requirements

- Install the latest version of [Python 3.X][python-download-url].
- Install the required packages:

```bash
pip install -r requirements.txt
```

- Install [ArchiSteamFarm][github-ASF] (ASF).
- Make sure that [IPC][wiki-ASF-IPC] is toggled ON. This is the default value.

## Usage

```bash
python add_free_licenses.py
```

## References

- [`Luois45/claim-free-steam-packages`][luois45-gpl-repository]: a tracker of free licenses on Steam,
- [`woctezuma/steam-next-fest`][steam-next-fest]: a previous project of mine which makes use of ASF IPC,
- A [Steam guide][steam-guide-no-cost] listing all of the free licenses which increment the library count.

<!-- Definitions -->

[steamdb-free-packages]: <https://steamdb.info/freepackages/>
[python-download-url]: <https://www.python.org/downloads/>
[github-ASF]: <https://github.com/JustArchiNET/ArchiSteamFarm>
[wiki-ASF-IPC]: <https://github.com/JustArchiNET/ArchiSteamFarm/wiki/IPC>
[luois45-gpl-repository]: <https://github.com/Luois45/claim-free-steam-packages>
[steam-next-fest]: <https://github.com/woctezuma/steam-next-fest>
[steam-guide-no-cost]: <https://steamcommunity.com/sharedfiles/filedetails/?id=2827818083>
