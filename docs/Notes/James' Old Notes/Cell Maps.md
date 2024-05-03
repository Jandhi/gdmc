#optimisation
Cell maps are (2D/3D) grids of geographically mapped cells with a cell size of 2^n m/cell.
The grid of cells is always centered around (0,0)

New grids are created dynamically upon request, and are informed by recursively lower levels.
Changes to lower levels may also invalidate higher levels depending on the modified level.
The values associated with each cell are populated and updated only when accessed

Maps are always accessed through a set of coordinates and a level

| Level | Cell size |                     |
| ----- | --------- | ------------------- |
| 0     | 1         | Single block        |
| 1     | 2         |                     |
| 2     | 4         |                     |
| 3     | 8         |                     |
| 4     | 16        | Chunksized          |
| 5     | 32        |                     |
| 6     | 64        |                     |
| 7     | 128       |                     |
| 8     | 256       |                     |
| 9     | 512       |                     |
| 10    | 1024      | GDMC large map size |
| ...   |           |                     |

## Mapset

A mapset is a class that contains and manages cell map information.
It takes 

## Primary maps
Primary maps represent aspects of the world which are directly taken from game data without any further strategies applied.

| Name  | Information | Format | Source |
| ----- | ----------- | ------ | ------ |
| Biome |             |        |        |
|       |             |        |        |
|       |             |        |        |

## Secondary maps
Tertiary maps are based solely on information from the primary maps, and provide an intermediate step, or "interpretation", of the world.

| Name | Information | Format | Source |
| ---- | ----------- | ------ | ------ |
|      |             |        |        |
|      |             |        |        |
|      |             |        |        |

## Tertiary maps
Tertiary maps are based on primary and secondary or other tertiary maps, making them highly complex and volatile to change.

| Name   | Information | Format | Source |
| ------ | ----------- | ------ | ------ |
| Beauty |             |        |        |
| Value  |             |        |        |
| Danger |             |        |        |
|        |             |        |        |

## Navigation map
Navigation maps shall be created for a given mode of transport when demanded, including but not limited to:
1. Travel on foot
2. Travel on horseback
3. Travel on wheels
4. Travel by boat
5. Travel by minecart

Pathfinding takes a starting cell and final cell as an input (coordinates, level)
### Connectivity map
Each cell stores navigational information on which sides of each cell, when approached from the orthogonally adjacent cell, connect to which other sides. This is achieved through a value for each side, representing full, partial, unexplored or no access. In the case of partial access, sub-cells must be checked to ensure access.
- No access
- Unexplored (may apply pathfinding)
- Partial access (must query subcells to be certain)
	- In
	- Out
	- Both
- Full access
By default, a cell's connections are unexplored. If any path can be found, it becomes at least "partial access both", otherwise "no access"
Examples: 
- If the cell cannot be accessed from e.g. the north, all values including the north side are "no access".
- If it can be accessed from the north, but leads to no other sides, then the north side is "full access" and all other sides "no access".
- If all blocks on the north cell's side lead to all blocks on the south side, then there is "full access" from north to south
- If all blocks on the north cell's side lead to some blocks on the south side, then there is "partial access out" from north to south
- If some blocks on the north cell's side lead to all blocks on the south side, then there is "partial access in" from north to south
- If some blocks on the north cell's side lead to some blocks on the south side, then there is "partial access in-out" from north to south
### Ease of Travel Map
In addition to the connectivity map, the ease of travel map contains the n\*k-th-percentile for the cost of travel, with f\[0] being the minimum and f\[-1] being the maximum.
The function for calculating this value takes a cell (coordinates and depth)