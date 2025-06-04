---
layout: docu
redirect_from:
- /docs/dev/building
title: Building
---

ImageC is written in the C++ programming language and uses the Linux operating system.
During the build process, it is compiled for Linux, Windows and macOS.

For developing [VSCode](https://code.visualstudio.com/) and a Docker devcontainer is used.
The devcontainer is actually only tested for Linux operating system.

> Warning If you want to try developing under Windows, you can try Docker for Windows together with the Windows Subsystem for Linux (WSL). 
> However, we do not provide any support or guarantee that it works.

**Preparation**

1. Download [VSCode](https://code.visualstudio.com/)
2. Clone ImageC repo `https://github.com/joda01/imagec.git`
3. Open the cloned directory using VSCode.
4. Install `Dev Containers` extension and Reopen open the project in container.

**First time to build**

ImageC uses [Conan](https://conan.io/) build system.
The artifacts needed for building are stored in our ImageC artifactory.
First time you want to build, please contact us and request access to the artifactory.

1. Request artifactory request support@imagec.org
2. Execute `./build_linux.sh --init` and enter your received token to login at the artifactory.
3. Execute `./build_linux.sh --make`
4. Execute `./build_linux.sh --build`

The build artifacts are placed into `./build/build/output`

