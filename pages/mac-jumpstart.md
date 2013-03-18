---
layout: page
title: MAC Jumpstart (esp for former Linux users)
tagline: 
---
{% include JB/setup %}

## Forewords

## Basic Gestures for Touchpad

   * Single point touch: 
   Move the pointer. 
   * Two points touch: 
   scroll up/down; scroll left/right; zoom in/out. 
   Try it out yourself with different apps. 
   * Three points touch: 
   left/right -- switch between multiple desktops;
   up == F3 -- multi-desktop view.
   * Four fingers scratch: Launchpad. 

## Tools to Help Linux Geek Jumpstart

   * [homebrew](https://github.com/mxcl/homebrew/wiki/Installation).
   It is sth. like `apt-get`, `yum`, `rpm`, etc. 
   No doubt to be the first thing you want to install. 
   It is well documented. 
   Just two notes:
   1) Use `brew doctor` to test your environment; 
   2) Use `brew update` frequently. 
   * XCode. 
   When installing `homebrew`, you should have already installed 
   "XCode" or "Command Line Tools for XCode". 
   CLI tools suffice for most Linux users. 
   It is like `build-essential` under Ubuntu. 
   * `brew install coreutils`. 
   You will find many things (format, options, etc) different in UNIX... 
   To maintain your Linux use pattern, `GNU/coreutils` is necessary. 
   Note, in order not to overrider UNIX default commands, 
   brew will install those commands with a name prefixed by "g". 
   You may want to soft link those commands somewhere and put its directory 
   in front of your `$PATH` in order to override UNIX commands. 

## Must Install App

   * CheatSheet: 
   Press `command` longer and a cheat sheet for keyboard shortcuts will prompt. 
   Hotkeys make MAC more efficient. 

## File Operations

### Copy Full Path Into "Open File" Dialog

   * `command+shift+g` or `/` or `~` to open the 
   "Go to directory" input box. 

[source](http://apple.stackexchange.com/questions/26819/enter-a-filename-in-the-file-open-dialog)

