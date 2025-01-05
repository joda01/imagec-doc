# Installation

## Which ImageC download do I need?

:::{hint}
It is recommended to use ImageC under Linux for best stability and performance.
:::


On **Linux** use `imagec-x64-linux-bundle.zip` from the [GithHub release](https://github.com/joda01/imagec/releases) page.

On **Windows** use `imagec-x64-win-bundle.zip` form the [GithHub release](https://github.com/joda01/imagec/releases) page. 

On **macOs** use `imagec-arm64-macos-bundle.zip` form the [GithHub release](https://github.com/joda01/imagec/releases) page. 

:::{hint}
For mac only arm based CPUs (M1, M2, M3) are supported.
:::

## Download & install

There are signed and unsigned versions available for ImageC.
Each major version is signed and marked the the label `[signed]` in the title of the [GithHub release](https://github.com/joda01/imagec/releases).
If you use an unsigned version you may need to take a few extra steps to get it to run:

- On **Linux**, download and extract the `.zip` file
  - You'll probably have to use {command}`chmod u+x /path/to/ImageC/imagec.sh` to make the launcher executable
  - Launch the application by typing {command}`./path/to/ImageC/imagec.sh` from your terminal.
- On **Windows**, if you downloaded the `.zip` file, extract it and then double-click on the {program}`imagec.exe` to launch the application
  - If you see a warning, choosing {guilabel}`More info` and {guilabel}`Run anyway` should let you proceed
- On **Windows**, if you want to use a signed version, download the {program}`imagec-x64-win-signed.exe` from a release with title `[signed]`.
  - Copy the downloaded `exe` into the folder beside the `imagec.exe`.
  - Double-click on the {program}`imagec-x64-win-signed.exe` to launch the application
- On **macOs** imagec must be added to the white list of allowed unsigned applications by typing following command {command}`xattr -dr com.apple.quarantine imagec.app`.



