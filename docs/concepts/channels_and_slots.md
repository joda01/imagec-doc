(channels-and-slots)=
# Channels and Slots

ImageC distinguish between two types of pipeline elements: {guilabel}`Channels` and {guilabel}`Slots`.
Both can be added in ImageC's [overview panel](overview-panel).
ImageC is actually limited to a maximum of {{max_channels}} channels and {{max_slots}} slots.

:::{note}
In the course of an analysis, the channels are subjected to processing prior to the slots.
:::

The processing order of channels and slots is defined as following:
1. Reference Spot channels
2. Spot, Nucleus, Cell and Background channels in parallel
3. Voronoi slot channels
4. Intersection slot channel 

:::{figure} images/screenshot_channels.png
:class: full-image
OME channel information at the right-hand side
:::


## Channels

:::{sidebar} Image channels

An image may comprise one or more C (channels), with each channel in turn consisting of a series of T (time) stacks, and these in turn consisting of a series of Z stacks.

ImageC is able to process up to 10 channels C with any number of images in the Z stack using the Max. intensity projection algorithm.
Time stacks are not yet supported.
If an image with time stack is processed ony the first image of the T stack is used.


:::{image} images/image_channels.drawio.svg
:class: full-image
:::

:::

A channel is invariably associated with a channel in an image in the range of `0` to `9`.
The OME metadata of an image provides information regarding the number of channels present within the image and the number of Z and potentially T stacks assigned to each channel.

In order to facilitate the configuration of the channel, the OME meta date, inclusive of the channel data, is displayed on the right-hand side of the overview panel.



## Slots

A slot is defined as a kind of virtual channel. It is not a physical entity within an image; rather, it is generated based on the information contained in the image channels.
Slots are identified by an index in the range of `A` to `F`.

In the actual release {{ env.config.release }} of ImageC two types of slots are available: {guilabel}`Voronoi` and {guilabel}`Intersection`.


:::{note}
The input of a slot channel is the output of an image channel!
:::

:::{caution}
It is imperative that each channel and slot index is unique, as is each channel and slot name.
Otherwise an error occurs when trying to start the analysis.
:::