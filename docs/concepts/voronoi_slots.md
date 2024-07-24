# Voronoi slots

By click on {guilabel}`Add voronoi channel` a new voronoi channel is added to the processing list.


:::{figure} images/screenshot_voronoi_channel_settings.png
:class: full-image
:::

:::{sidebar} Voronoi diagram
A Voronoi diagram, also known as a Thiessen polygon or Dirichlet decomposition, represents a decomposition of space into regions that are determined by a given set of points in space, referred to here as centres.
The diagram areas are generated so that the enveloping area of each point is the closest to that point.
Voronoi diagrams can be useful for approximating cell surfaces based on known cell nuclei.

:::{figure} images/voronoi_example.png
:class: full-image

:::

(voronoi-meta)=
## Meta

Similar to the [image channels](image-channels) a user defined name can be set for the channel.

Using the {guilabel}`Channel index` the slot index `[A-F]` which should be associated with this channel can be selected.
Each slot channel index can only be used once and is needed for a unique identification of the channel.
Based on the slot channel index cross-channel measurements, for example, can be conducted on a specific slot channel.

## Voronoi

In order to construct a Voronoi diagram, it is necessary to gather certain fundamental data. 
This information can be obtained from the {guilabel}`Voronoi` settings tab, which is used for the Voronoi diagram construction process.

### Voronoi points channel

A Voronoi diagram is constructed using points in space as the fundamental building blocks.
The {guilabel}`Voronoi points channel` defines the channel which ImageC should use the take the points in space from.
The centre of mass is used as the initial point for the Voronoi construction process, from the valid regions of interest identified within the selected channel.
Make sure the {guilabel}`Voronoi points channel` was added to the processing list as an image channel before. 
Also, make sure the preprocessing and detection settings are correct of this channel.

:::{hint}
Typical {guilabel}`Voronoi points channel` are channels containing nuclei.
:::

### Max voronoi area radius

With setting {guilabel}`Max. voronoi area radius` the area of a Voronoi diagram can be limited by its radius.
This option is particularly beneficial in scenarios where cells must be approximated based on provided nuclei, yet the cell density is exceedingly low.
Remove the value if no are size limitation should be done.

### Overlay mask channel

ImageC offers the option to overlay and intersect a calculated Voronoi diagram with another surface.
This option is particularly beneficial in scenarios where a cell area channel exists.
The intersection of the calculated Voronoi grid with the cell area channel results in a more accurate cell approximation, as any areas that are not part of the actual terrain are removed.


## Object filter

Similarly, the application of object filters to the [image channels](image-channels) it is also a possibility for voronoi slots.
Object filter in voronoi slots are applied to the calculated Voronoi diagram areas.
Beside the option to exclude voronoi diagram areas based on its size two more advanced options, {guilabel}`Exclude areas at the edges` and {guilabel}`Exclude areas without center` are available.

### Exclude areas at the edges

When this filter is active, all areas that touch the edge of the image are marked as invalid.

### Exclude areas without center

The Voronoi diagram is computed based on a set of points which are the centres of the computed Voronoi diagram areas.
When using the Voronoi diagram in combination with a {guilabel}`Overlay Mask Channel`, it can happen that after applying the mask, areas are left that don't have a centre point anymore.
Enabling this filter will invalidate all areas that do not contain a point from the source point set.

:::{hint}
It is recommended to enable this option if nuclei are used as a set of points and cell areas as a clipping mask. Applying this filter option will filter out all left areas that do not contain nuclei.
:::