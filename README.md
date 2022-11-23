# Add Free Licenses

This repository contains Python code to automatically [add free licenses][steamdb-free-packages] on Steam.

![Illustration cover][img-cover]

## Requirements

- Install the latest version of [Python 3.X][python-download-url].
- Install the required packages:

```bash
pip install -r requirements.txt
```

- Install [ArchiSteamFarm][github-ASF] (ASF).
- Make sure that [IPC][wiki-ASF-IPC] is toggled ON. This is the default value.

## Data

To retrieve a list of appIDs which are already tied to your account,
here are a few methods.

<details><summary>1. /dynamicstore/userdata</summary>
<p>

The variable `rgOwnedApps` in the JSON data returned by
the [`/dynamicstore/userdata`][steam-userdata-endpoint] endpoint is
a large yet non-exhaustive list of appIDs owned by your account.
More information can be found on [this unofficial wiki][steam-userdata-wiki].

**NB:** you have to be **authenticated** on Steam in your web-browser in order to use this method.

---

</p>
</details>

<details><summary>2. steamctl apps list</summary>
<p>

[`steamctl`][steamctl-github] is a Python package [available on PyPI][steamctl-pypi].

It allows to print to the terminal
the exhaustive list of appIDs owned by your account.

```bash
pip install pipx
pipx install steamctl
```

```bash
steamctl apps list
```

The output should be formatted as follows: `{appID} {appName}`.

```
[...]
1667640 Imagined Leviathans Demo
1667710 Gladihaters Demo
1667730 Forgotten Journey
1667770 Samurai Shampoo
1667810 Riding Seas Demo
[...]
```

**NB:** you have to be **authenticated** on Steam with `steamctl` in order to use this method.

---

</p>
</details>

<details><summary>3. /games/?tab=all</summary>
<p>

**Caveat:** I recommend **not** to use this procedure
because the list of appIDs is not **exhaustive** ,
e.g. demos are missing.

A procedure built into the script
at [`Luois45`][luois45-gpl-repository]
parses a list of appIDs from
the [`/games/?tab=all`][steam-tab-all] web-page.

**NB:** the "game details" part of your Steam profile have to be public in order to use this method.

---

</p>
</details>

<details><summary>4. /account/licenses/</summary>
<p>

**Caveat:** I recommend **not** to use this procedure
because this retrieves **subIDs** instead of appIDs.

[Instructions][steam-account-licenses-instructions]
at [`Luois45`][luois45-gpl-repository]
suggest to execute JavaScript code in your browser
on the [`/account/licenses/`][steam-account-licenses] web-page.

**NB:** you have to be **authenticated** on Steam in your web-browser in order to use this method.

---

</p>
</details>

Because it is the only method which returns an **exhaustive** list, the recommended method is:

```bash
pip install pipx
pipx install git+https://github.com/woctezuma/steamctl.git@67-fix-charmap
steamctl apps list > data/steamctl_output.txt
```

## Usage

```bash
python add_free_licenses.py
```

## References

- A [Github issue][luois45-appid-issue] which describes some attempts to retrieve owned appIDs,
- [`Luois45/claim-free-steam-packages`][luois45-gpl-repository]: a tracker of free licenses on Steam,
- [`woctezuma/steam-next-fest`][steam-next-fest]: a previous project of mine which makes use of ASF IPC,
- A [Steam guide][steam-guide-no-cost] listing all of the free licenses which increment the library count.

<!-- Definitions -->

[steamdb-free-packages]: <https://steamdb.info/freepackages/>
[img-cover]: <https://github.com/woctezuma/add-free-licenses/wiki/img/cover.png>
[python-download-url]: <https://www.python.org/downloads/>
[github-ASF]: <https://github.com/JustArchiNET/ArchiSteamFarm>
[wiki-ASF-IPC]: <https://github.com/JustArchiNET/ArchiSteamFarm/wiki/IPC>
[steam-userdata-endpoint]: <https://store.steampowered.com/dynamicstore/userdata>
[steam-userdata-wiki]: <https://github.com/Revadike/InternalSteamWebAPI/wiki/Get-Dynamic-Store-User-Data>
[steamctl-github]: <https://github.com/ValvePython/steamctl>
[steamctl-pypi]: <https://pypi.org/project/steamctl/>
[steam-tab-all]: <https://steamcommunity.com/my/id/games/?tab=all>
[steam-account-licenses-instructions]: <https://github.com/Luois45/claim-free-steam-packages/blob/main/docs/instructions-for-users-with-many-packages.md>
[steam-account-licenses]: <https://store.steampowered.com/account/licenses/>
[luois45-appid-issue]: <https://github.com/Luois45/claim-free-steam-packages/issues/166>
[luois45-gpl-repository]: <https://github.com/Luois45/claim-free-steam-packages>
[steam-next-fest]: <https://github.com/woctezuma/steam-next-fest>
[steam-guide-no-cost]: <https://steamcommunity.com/sharedfiles/filedetails/?id=2827818083>
