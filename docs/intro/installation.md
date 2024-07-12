# Installation

## Which imageC download do I need?

### imageC for Linux

It is recommended to use imageC under Linux for best stability and performance.

### imageC for Windows

On **Windows**, you have two options when downloading imageC:

* **Windows installer (msi)** use this if you want to install imageC, so that it appears in the {guilabel}`Start` menu like most apps
* **Windows portable (exe)** use this if you want to just unzip a folder containing imageC, and run it from there - with no further installation needed

(imageC-versions-for-mac)=
### imageC for Mac

Because of licensing issues, imageC is not available for Mac yet.



## Download & install

There are signed and unsigned versions available for imageC.
Each major version is signed and marked the the label `[signed]` in the title of the [GithHub release](https://github.com/joda01/imagec/releases).
If you use an unsigned version you may need to take a few extra steps to get it to run:

- On **Linux**, download and extract the `.zip` file
  - You'll probably have to use `chmod u+x /path/to/imageC/imagec.sh` to make the launcher executable
  - Launch the application by typing `./path/to/imageC/imagec.sh` from your terminal.
- On **Windows**, if you downloaded the `.zip` file, extract it and then double-click on the `imagec.exe` to launch the application
  - If you see a warning, choosing {guilabel}`More info` and {guilabel}`Run anyway` should let you proceed
- On **Windows**, if you want to use a signed version, download the `imagec-x64-win-signed.exe` from a release with title `[signed]`.
  - Copy the downloaded `exe` into the folder beside the `imagec.exe`.
  - Double-click on the `imagec-x64-win-signed.exe` to launch the application
- On **macOS**, right-click the `.pkg` file, then choose 'Open' (you might need to do this twice)
  - If you're using an M1/M2/M3 Mac, please check out the [notes on Apple silicon](apple-silicon)

See {ref}`Troubleshooting` for more information.


