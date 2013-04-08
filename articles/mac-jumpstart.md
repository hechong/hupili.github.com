---
layout: page
title: MAC Jumpstart (esp for former Linux users)
group: article
tagline: 
---
{% include JB/setup %}

## Forewords

I switched to MAC Book Pro since Feb 28, 2013.
Three days later, I brought the MBP with me and went home for a week.
It's a nice journey.
Although I have no experience of MAC before, 
I managed to change my working environment to MAC during the week **on leave**.
It is fun working with MAC...
There are also some traps for former Linux users.
This article intends to help new users to jumpstart.

   * Most of the tips are not step-by-step guide. 
   Instead, I love those general principles, 
   which can help people better explore the system. 
   Bearing those principles in mind, 
   one can enjoy the process of discovery. 

## Basic Gestures for Touchpad

Touch:

   * Single point touch: 
   Move the pointer. 
   * Two points touch: 
   scroll up/down; scroll left/right; zoom in/out. 
   Try it out yourself with different apps. 
   * Three points touch: 
   left/right -- switch between multiple desktops;
   up == F3 -- multi-desktop view.
   * Four fingers scratch: Launchpad. 
   * [hot corner](http://heresthethingblog.com/2013/01/18/mac-control-desktop-hot-corners/)
   is a somewhat obsolete (prior to multi-touch pad is available) but useful component. 
   The gesture is: move your mouse pointer from any direction to the corner; stay there for some time. 
   (not "flick" or "shove" as was said in some posts)

Click:

   * Press the bottom of touchpad is equivalent to "single left click". 
   (using the windows language). 
   * "right click": 
   press the bottom longer; 
   `control`+click;
   use two fingers press the bottom.

## Basic Keyboard Shortcuts

   * People who come from Windows or Linux should first note the "Apple Key", i.e. `command`. 
   If you have `control+xxx` in your impression from previous experience, try `command+xxx`. 
   e.g. `command+c` for copy, `command+v` for paste, `command+s` for save, etc. 
   This single tip can help you get back half of the efficiency.
   * Treat `command` as `ctrl` and `option` as `alt`.
   Many operation applies with this simple mapping. 
   e.g. Use `command` and mouse to select non-consecutive texts.
   e.g. Use `option` and mouse to select a vertical block. 
   * Use `command+option+esc` to force quit an application
   (like `alt+f4` in many other systems).
   * When a menu is active, 
   usually you can press `option` to get more options
   (show previously missing ones or change to another set of options). 

## Terminal Configuration

With the default iTerm, former Linux users can get their work down very quickly. 
However, the default settings are not so satisfactory. 

   * If you can not input non-ascii characters in VIM,
   see [this post](http://superuser.com/questions/21292/how-to-use-utf-8-in-vim-on-mac-os-x).
   quote as follows for your convenience:

> In Terminal.app go the the Terminal (main) menu and choose Window Settings. 
> Select Emulation from the popup menu, un-check the item "Escape non-ASCII characters". 
> Then select Display from the popup menu, set Character Set Encoding to Unicode (UTF-8), if desired. 
> Click on "Use settings as Default."

   * Choose a better colored theme so that you can code comfortably.
   * Change the window size.
   * ... (more to come)

If you just want to get sth. done quickly and smoothly, 
feel free to use my 
[terminal configuration]({{site.base_links.github}}/utility/tree/master/mac/Terminal).
It was adapted from [IR_Black](http://toddwerth.com/2011/07/21/the-original-ir_black-for-os-x-lion/).
All the above improvements are included.

## Input Method (Chinese)

   * Squirrel. 
   Commonly recognized as the best Chinese IME for MAC. 
   It also has Linux and Windows ports.
   * Use `control+\`` to call the quick config panel of Squirrel. 
   Choose "Traditional --> Simplified" if you want to input simplified Chinese. 

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

## Must-install App

   * CheatSheet: 
   Press `command` longer and a cheat sheet for keyboard shortcuts will prompt. 
   Hotkeys make MAC more efficient. 

## Energy Saving Configurations

MBP's default configuration suits most people. 
One thing I'm not satisfied is that there is no default convenient screen lock mechanism
(like `win+L` in Windows and `ctrl+alt+L` in Unbuntu). 
Some solutions:

   * `control+shift+eject`. This puts MAC to sleep. 
   One drawback is that Internet connection will be lost. 
   * Use "hot corner" to activate screen saver. 
   This is much better if you leave seats frequently for a few minutes. 

In security and privacy configuration, require password from screen saver or sleep immediately. 

## Backup 

Time Machine is good enough for most people:

   * See the discussion of  
   [backup habit](http://creativetechs.com/tipsblog/access-files-from-other-time-machine-backups/).
   It also points to other software that can make a bootable backup. 
   * You can also browse files 
   [from other machine's backup](http://creativetechs.com/tipsblog/access-files-from-other-time-machine-backups/).

## Automator

In "Automator", you can create "workflows", "services", etc. 
It can be used to customize your MAC to a large degree. 
Generally speaking, you can:

   * Get actions and data from GUI.
   * Trigger a shell script. 
   * Put data to some GUI components, e.g. clipboard. 

As a programmer, you should have realized that you can do nearly everything now. 
Strongly recommend you give it a try.
To see what I have, check out my 
[utility/mac/Services](https://github.com/hupili/utility/tree/master/mac/Services).

## Customized Keyboard Shortcuts

### Manual Configuration

To set global hotkeys:

   * 1. In "System Preference"--"Keyboard", 
   you can set hotkeys for (only) **application menu items**. 
   * 2. Other App like "Alfred" or "Quicksilver" provide global hotkey management. 
   See 
   [this thread](http://apple.stackexchange.com/questions/24063/create-global-shortcut-to-run-command-line-applications)
   for a list of such apps.

When I seek for solutions, I prefer system default ones and portable ones first.
Applying it to the demand here, I avoid any app and do the following:

   * Create a service, as is shown above. 
   (**the shell scripts are portable to other systems**)
   * Bind the service to a hotkey via: "System Preference"--"Keyboard".
   (**system default**)

### Programmatical Configuration

There are posts relating to 
[programmatically add keyboard shortcuts](http://stackoverflow.com/questions/7219134/programmatically-add-keyboard-shortcut-to-mac-system-preferences)
via `defaults` command. 
One can also operate 
[plist](http://support.apple.com/kb/TA24670?viewlocale=en_US&locale=en_US)
directly. 
However, I did not find `NSUserKeyEquivalents` in "~/Library/Preferences/.GlobalPreferences.plist".
I'll come back to update it when I have a good solution. 
With programmatical configuration, we can:

   * Backup our keyboard shortcuts in a portable way. 
   * Fast (and probably temporarily) customize another system. 

## File Operations

### Copy Full Path Into "Open File" Dialog

   * `command+shift+g` or `/` or `~` to open the 
   "Go to directory" input box. 

[source](http://apple.stackexchange.com/questions/26819/enter-a-filename-in-the-file-open-dialog)

## Some Common Questions

### Battery Do Not Charge to 100%

This is normal as is said in one 
[official post](http://support.apple.com/kb/TS1909?viewlocale=en_US&locale=en_US). 
It is said in this way battery life will be longer 
because they avoid short term charge/discharge. 
More knowledge of 
[batteries](http://www.apple.com/batteries/).

### Suggested Battery Use Pattern

Note that MBP's built-in battery is really powerful and convenient. 
See [this post](https://discussions.apple.com/thread/1764220?threadID=1764220) for a detailed discussion. 
Although the post is old, it is not completely outdated. 
Good as a reference. 

Summary for me:

   * No over discharge.
   * Better not to always connect to AC adapter.
   * 1-2 times / week full charge cycle.
   * 2-3 months for a calibration.

