# Runetrader

Automated Grand Exchange Trading Platform for OSRS

## About

This project aims to fully automate every aspect of trading buy/sell price margins in old school Runescape. This is done not by a WindowHook, but rather a primite mouse and keyboard handler using pyautogui and a custom wrapper for it.

We use both image and optical character recognition to locate and save positions of both statically and dynamically placed buttons. These coordinates are then saved as a json file, to avoid unnecessary analysis on startup. 

The saved coordinates are all passed through a dynamic coordinate calculator, making the Runescape window position and sizing irrelevant.

