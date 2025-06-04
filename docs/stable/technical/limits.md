---
layout: docu
redirect_from:
- /docs/technical/limits
title: Resources and Limits
---

Minimum hardware requirements.
More is always better ;) ...

Component    | Minimum          
-----------  |----------        
CPU          |64 bit, 1 GHz dual core (preferred > 2 GHz)
RAM          |2 GB of free RAM  (+0.5 GB for each additional CPU core)
Storage      |500 MB free storage for installation
Screen       |Minimum recommended resolution 1528x980
Graphic card |(optional) Nvidia graphical card with CUDA support.

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


