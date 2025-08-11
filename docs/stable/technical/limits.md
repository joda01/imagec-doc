---
layout: docu
redirect_from:
- /docs/technical/limits
title: Resources and Limits
---

Minimum hardware requirements for **CPU only** variant:

Component    | Minimum          
-----------  |----------        
CPU          |64 bit, 2 GHz dual core
RAM          |2 GB of free RAM  (+0.5 GB for each additional CPU core)
Storage      |500 MB free storage for installation
Screen       |Minimum recommended resolution 1528x980
Graphic card |(optional) Nvidia graphical card with CUDA support.


Minimum hardware requirements for **CUDA variant** variant:

Component              | Minimum          
-----------            |----------        
CPU                    |64 bit, 2 GHz quad core
RAM                    |4 GB of free RAM  (+0.5 GB for each additional CPU core)
Storage                |4 GB free storage for installation
Screen                 |Minimum recommended resolution 1528x980
GPU RAM                |8 GB of free RAM on the graphics card.
CUDA version           |CUDA 12.8 or newer

Supported graphic cards:

| Series / Architecture     | Compute Capability | GeForce Models Included                                                   |
| ------------------------- | ------------------ | ------------------------------------------------------------------------- |
| **RTX 50 (Blackwell)**    | CC 12.0            | 5090, 5080, 5070 Ti, 5070, 5060 Ti, 5060                                  |
| **RTX 40 (Ada Lovelace)** | CC 8.9             | 4090, 4080, 4070 Ti, 4070, 4060 Ti, 4060, 4050                            |
| **RTX 30 (Ampere)**       | CC 8.6             | 3090 Ti, 3090, 3080 Ti, 3080, 3070 Ti, 3070, 3060 Ti, 3060, 3050 Ti, 3050 |
| **RTX 20 (Turing)**       | CC 7.5             | 2080 Ti, 2080, 2070 Super, 2070, 2060 Super, 2060                         |



## Limits

See section [Image formats]({% link docs/stable/fundamentals/image_formats.md %}) for a list of supported image formats.

| Limit                  | Default value | 
|---                     |---            |
| Max classes            | 32            |
| Max image series       | 10            |
| Max image channels     | 10            |
| Max z-stack images     | 65535         |
| Max t-stack images     | 2 billion     |
| Max number of objects  | 1 billion     |
| Max number of pipelines| 65535         |
| Maximum tile size      | 46340x46340   |


