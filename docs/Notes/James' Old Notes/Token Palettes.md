When queried, the palette follows the decision tree to find a suitable block given a set of conditions. If no suitable blocks are found, the search fails with an error and uses a structure block.
- The **return value** is a block or list of blocks (for a texture)
- A **texture token** may take a named parameter and apply a function to it to determine the distribution of blocks it should return
- A **material token** takes an ordered collection of conditions and a material or texture token or a value, and contains material properties
- A feature token acts like a material token, but fails if its own condition is not met

![[Pasted image 20240419143155.png]]