# Runetrader

Automated Grand Exchange Trading Platform for OSRS

## About

This project aims to fully automate every aspect of trading buy/sell price margins in old school Runescape. This is done not by a WindowHook, but rather a primitive mouse and keyboard handler using pyautogui and a custom wrapper for it.

We use both image and optical character recognition to locate and save positions of both statically and dynamically placed buttons. These coordinates are then saved as a json file, to avoid unnecessary analysis on startup. 

The saved coordinates are all passed through a dynamic coordinate calculator, making the Runescape window position and sizing irrelevant.

Currently the bot earns about 400k GP an hour with a 5 mil capital. Running 20 accounts at once would net you 36 USD an hour assuming that the market doesnt get crashed by running the bot.
