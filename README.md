# SteamworksPy

This is a fork of [philippj/SteamworksPy](https://github.com/philippj/SteamworksPy). Modify to be used in [CN-DST-DEVELOPER/ModUploader](https://github.com/CN-DST-DEVELOPER/ModUploader)

## How to install with pip

You can simply install with follow command

```bash
pip install git+https://github.com/zxcvbnm3057/SteamworksPy.git@master
```

## How to build

You should Prepare following files before build :

- Copy `steam_api64.dll` and `steam_api64.lib` from `sdk\redistributable_bin\your_operating_system` in [`steamworks_sdk.zip`](https://partner.steamgames.com/downloads/steamworks_sdk.zip) to `library\sdk\redist`
- Copy all files from `sdk\public\steam` to `library\sdk\steam`
- Modify path of `VsDevCmd.bat` in file `build_win_64.bat` to meet your VS install.

Then you can run `build_win_64.bat your_vs_version` to build the library

## Some Notes

While I am still tinkering away with this, here are some things to note:

- Require steam_appid.txt in the same dictionary of your python scrpit - Stating your games app id or any other valid app id given the account owns a license
- The library will only function if the Steam client is running and logged in. Otherwise you will encounter exceptions.
- Do not install Python from the Microsoft App Store. Make sure to [download and install it from Python's main site.](https://www.python.org/)

For more information you can read [README.md](https://github.com/philippj/SteamworksPy#readme) on upstream.

## Usage

There is an examply usage of this module.

- [CN-DST-DEVELOPER/ModUploader](https://github.com/CN-DST-DEVELOPER/ModUploader)
