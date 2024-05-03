The goal of our material system is to provide a way for prefabs to receive texturing and weathering effects without building them manually.

# Palettizing 
Each block in a prefab will map to some entry in a palette. To distinguish this role from the material it has, I will call this the block's *function*.

![[2024-04-30_14.33.10.png]]
This wall prefab contains six block types, which map to four different functions. Note that the cobblestone stairs and cobblestone are different expressions of the same function, and similarly so for the wooden fences and door.

### The Palette Swap
When the prefab is pasted into the world, the functions can be mapped to a series of materials as specified by a block palette. We can refer to this as a *palette swap*, since it changes the palette of blocks we are working with, while maintaining their function. 

![[2024-04-30_14.37.00.png]]
The result of palette-swapping the previous prefab to a more desert-suited palette. 

### Block Functions
This is a non-exhaustive list of functions that a palette should cover:
- Primary Wall
- Secondary Wall (*Generally used for decorative elements.*)
- Frame
- Wood (*For required wood elements, like doors*)
- Floor
- Primary Roof
- Secondary Roof

### Palette Generation
Since we want buildings in a settlement to have a vast variety of palettes, it is likely not worth the effort of hand-crafting every possible palette. Rather, we could have a generative approach where we have a list of possible materials that narrows once by district and further by each house into a single palette. For example, a settlement may see a mix of birch, oak, and cobblestone houses, while a poorer district only has birch and oak houses, and a single house in that district may be made of only oak. 


### The Mapping Problem
Some blocks don't map nicely to other sets. For example, there are no stone trapdoors. In the case that we have a *trapdoor (primary wall)* but the primary wall material is stone, we should default to the *(wood)* function instead. For Tudor style timber-frame houses, we may want to use wool for the walls- but wool doesn't have any stair blocks or slabs- so in that case we may want to again map to wood.  


# Materials
Materials will represent a set of blocks that fulfills a certain function. It should be able to build a range of block shapes- such as normal blocks, stairs, slabs, fence/walls, etc- allowing for one material to swap for another easily (though this may not always be the case). 

### Randomization & Noise
One of the first ways to make textures in Minecraft building is by using multiple block types at random. This is excellent for creating depth and variation- but building this effect directly into prefabs would easily inject too much order in the noise as the same patterns repeat.

Instead, I propose we allow for materials that select on of multiple block types according to a noise function.

![[2024-04-30_16.55.42.png]]
An example of a lovely textured road surface on WesterosCraft.

![[2024-04-30_16.59.40.png]]
A textured wall in King's Landing, WesterosCraft.

Blocks could be selected entirely randomly, or based on a range using something like Perlin noise (we could clone https://github.com/salaxieb/perlin_noise/ and make it work with our random hasher). For example, in the road texture example, it make sense to choose a block type based on the distance from the center of the road, with a healthy amount of variance. This could also be achieved by having multiple axes of randomization- such as two axes of weathering- to select the block type. 
### Shading
Randomization also works well in unison with shading, usually where the materials become lighter the higher they are built. You don't want to do this in a perfectly smooth gradient, so combining it with noise is likely best. 

![[2024-04-30_23.08.13.png]]
Shading on a smaller fortification in King's Landing

![[2024-04-30_23.10.17.png]]
The walls of Winterfell- an excellent example of shading and randomization in tandem

To implement shading, I would want to create a map between materials where every material has optional connections to another material that is lighter in color, and another darker. When a material is selected for a wall, a range could be created from the lighter to the darker color that maps somehow from 0 (the lowest point, and darkest) to 1 (the highest point in the building, and lightest).  

For materials that are randomized, we can simply have each individual submaterial take care of the darkening/lightening. We can probably also stick with one base material and one lighter and one darker, though we can play with smoother shading based on the material (this could be calculated by the palette based on how many material nodes it can go lighter and darker).
### Weathering
In addition to the dark/light axis, it's worth having additional nodes for some weathering. Primarily, this would probably be age- which could even wear down the block types at high value, such as a block becoming a stair becoming a slab, etc. This can also be reflected in block type- for example, stone bricks-> cracked stone bricks -> cobblestone -> gravel, etc. 

Moisture is something that has fewer blocks to reflect it, but it would be lovely to use mossy stone blocks, mossy cobblestone, and moss blocks to reflect it. Additionally, we can probably use some more green and blue blocks to reflect this with other stone and wood types. 

We will want to calculate these values based on building parameters, as well as perhaps using the water map for information about moisture (i.e. the lowest layers of blocks near water tiles have high moisture). There is also the option to add randomization for the connections, where aging may randomly create two outcomes for the same block.

### The Mapping Problem Pt 2.
Not all materials will have the right connections to be weathered, lightened, darkened, etc. In this case we have two options- either we simply don't express that parameter and keep with the default block (e.g., we can't darken a material if it has no darker material connection). Alternatively, we can also reach for neighboring alternatives (e.g. we may not have a moist version of polished andesite, but perhaps mossy stone bricks will do)- however, in that case we might as well encode that relationship directly as a connection between the materials. 

So I think in the case that we don't have the option to express a parameter that's fine- but we can be generous with connections so that we can express as many parameters as we can, even if the blocks may not look entirely alike. 
### Nested Materials
To avoid reimplementing connection trees for the same materials, we will likely want to allow for materials to reference each other freely and to be nested in the case of randomized sets of materials. This way we won't have to have many different cobblestone materials each with similar weathering patterns and the like. 
### Material Parameters
- Block type (block, stairs, slab, etc)
- Coordinates for noise
- Height (in relation to the structure as a whole, starting from the lowest ground level)
- Age
- Moisture
- Shade (0 for darkest, 1 for lightest)
# Conclusion
To conclude, I propose we have a set of basic materials- which represent a set of blocks with the same texture- such as cobblestone, oak wood, etc. We may also have composite materials, which randomly choose from a set of other materials. 

Each basic material will have a series of connections that point to another material that may be lighter, darker, older, improved, more moist, or dryer (and perhaps more). When we place blocks from a material, it gets passed parameters which may have it step through these material nodes to find the proper end material.

Prefabs will be made up of a few different sets of blocks that have different functions- e.g. primary wall, secondary wall, etc. We will choose the materials to use for these functions via a palette generation process that narrows in from a range of values at the settlement level, to a smaller range at district level, to a specific material palette per structure. 

When a building is placed, the palette determines the start material for each block, and then we perform a walk based on various parameters. 