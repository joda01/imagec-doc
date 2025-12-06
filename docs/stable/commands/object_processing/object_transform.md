---
layout: docu
redirect_from:
- /docs/commands/object-transform
title: Object transform
---

<a href="{{ site.baseurl }}/images/commands/object-transform-screenshot.png" data-lightbox="image"><img src="{{ site.baseurl }}/images/commands/object-transform-screenshot.png" style="width: 30%" alt="Loading ..."/></a>

The object transform command takes existing objects and transform the size or shape of these objects.
The resulting objects can either be assigned to a new class or override the existing objects.

Actually five transform functions are supported:

### Scale

Scale changes the size of the objects depending on the given factor.
A factor of `2` for example doubles the sizes of the given objects.

### Min. circle

Draws a fitting circle around each object with the given radius as minimum circle size.

### Draw circle

Draws a circle with fixed size around each object.

### Fit ellipse

Draws a fitting ellipse around each object.
Optionally a scaling factor for the ellipse can be defined.