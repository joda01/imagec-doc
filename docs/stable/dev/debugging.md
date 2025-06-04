---
layout: docu
redirect_from:
- /docs/dev/debugging
title: Debugging
---

ImageC is written in C++ and compiled into a binary that is executed directly on your CPU.
While such programmes offer the highest possible performance, they have the disadvantage that, in the event of a programme error, the programme simply crashes and closes.

Even though we test ImageC, it is still possible that we have overlooked an error, causing the programme to crash in certain situations.
To help us identify the cause of the crash, ImageC can be started in debug mode. Once started in debug mode, ImageC generates a crash report that can be made available to us.

Once the program crashes please send the `debug.txt` to support@imagec.org.

## Linux

1. Open a terminal window
2. Change directory to the installation folder of ImageC `cd ⟨imagec_install_directory⟩`{:.language-sql .highlight} 
3. Start ImageC with following command `./imagec > debug.txt`


## Window

1. Open Windows Powershell as Administrator.
2. Change directory to the installation folder of ImageC `cd ⟨imagec_install_directory⟩`{:.language-sql .highlight} 
3. Start ImageC with following command `Start-Process -RedirectStandardOutput debug.txt imagec.exe`

## macOS

1. Open a terminal window
2. Change directory to the installation folder of ImageC `cd ⟨imagec_install_directory⟩`{:.language-sql .highlight} 
3. Start ImageC with following command `./imagec > debug.txt`