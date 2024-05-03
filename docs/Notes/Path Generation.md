
## Planning
Current generation process returns an (ordered?) sequence of coordinates.
## Model
A model should be a macroscopic representation of the path network.
A graph is well-suited for this purpose.

I'd suggest, as part of the planning process or post-planning, linking all adjacent blocks together into a large graph which can then be processed further.
Each node of this pre-processing graph would only contain the coordinates of the block
### Node
Nodes of the graph would represent points of transition. This might include, but is not limited to:
1. Junctions (e.g. where three or more district cells meet; where routs join a main route)
	- Might be detected based on number of adjacent coordinates?
2. Change in direction (rounded to 16ths of a circle)
3. (Change in medium)
	1. Dirt/grass
	2. Sand
	3. Water
	4. Ice
4. (Change in incline)

It might include the following properties:
- [ ] Any number of vertices
- [ ] Its position
- [ ] (A name)

### Vertex

Verteces connect two nodes and represent longer stretches of paths (e.g. of the same type/direction)

They might include the following properties:
- [ ] Its nodes
- [ ] Its direction (rounded to 16ths of a circle)
- [ ] A list of positions making up the path
- [ ] A dict to be populated with properties by other systems
- [ ] (A name)