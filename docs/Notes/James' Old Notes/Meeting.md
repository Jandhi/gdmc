beautiful houses, designed interior, maybe more house styles would be nice
There was a building that we could not enter. 
Pro: Adapts to topology, good walls, nice buildings and furniture, realistic farmland (though too steep in parts); Contra: Rubbish navigability (though smoothed paving is good), janky furnishing (most entrances blocked, no windows), excessive bulldozing of natural features
The generator has ***a very precise aesthetics, which it reproduces in all of its settlements***. While it adapts very well to the terrain, it does not adapt that well to the current biome. That being said, it produces really pleasant villages. 
The decoration inside the house is very beautiful, and the city walls look very natural

Comment indexing:

| **Good**             |        |
| -------------------- | ------ |
| Villages             | I      |
| **Houses**           | **II** |
| Furniture            | I      |
| Farmland             | I      |
| Walls                | II     |
| Adaption to topology | II     |
| Smoothed paths       | I      |

| **Bad**              |        |
| -------------------- | ------ |
| Few styles           | I      |
| **Navigability**     | **II** |
| Steep farmland       | I      |
| Interior             | I      |
| Lack of windows      | I      |
| Natural preservation | I      |
| Adaption to biome    | I      |

Ranking:
- Adaptability: 3rd (-0.34/+0.21)
	- 0.25-point improvement for 2nd
	- 2.5-point improvement for 1st
- Functionality: 4th (-0.11/+0.07)
	- 0.25-point improvement for 2nd
	- 1.5-point improvement for 1st
- Narrative: 6th (-0.66/+0.14)
	- 0.25-point improvement for 3rd
	- 0.5-point improvement for 2nd
	- 1.25-point improvement for 1st
- Aesthetics: 3rd (-0.02/+0.13)
	- 0.25-point improvement for 2nd
	- 1.25-point improvement for 1st
- Overall: 2nd (-0.0575/+1.5175)

Quick wins:
- Adaptability
	- [ ] +0.25 Biome adaption
- Functionality
	- [ ] +0.25 Street lighting
	- [ ] +0.1 Keeping doors free
	- [ ] +0.1 Field irrigation
- Narrative
	- [ ] +1 Decorative structures (scarecrows, wells, monuments, carts etc.)
- Aesthetics
	- [ ] +0.5 Refine prefabs (currently very flat walls etc.)
		- [ ] Make use of GDPC randomised texture fill? (adaptive prefabs)
	- [ ] +0.5 More variation (currently lots of 1x1x1)

Larger tasks:
- Adaptability
	- [ ] +1 Use of special features in the landscape
	- [ ] +1 Cave exploitation (underground structure bonus)
	- [ ] +1 Adaptive prefabs
	- [ ] +1 Adaptive palettes
	- [ ] +0.5 Improved settlement/building placement
- Functionality
	- [ ] +1 Specialised rooms/buildings
	- [ ] +0.5 Streets and plazas
	- [ ] +0.5 roping off/avoiding steep drops
- Narrative
	- [ ] +0.5 Individual decoration
	- [ ] +0.5 Chronicle challenge (+ chronicle bonus)
- Aesthetics
	- [ ] +1 Rework building generation
	- [ ] +1 Parks, gardens and plazas

## Issues
Generic:
- Next to no windows
- Terraforming too aggressive

1. Large map
	1. Hard to find at a distance
	2. Jank with wall
2. Swamp and mangrove
	1. Wall can't deal with water
3. Coast
	1. No use of coastline
4. Mountain
	1. Far too aggressive with chopping off mountaintops
5. Island
	1. Completely decimated the forest, even though it wasn't used otherwise

How to deal with biomes?
- Min. roof angle and shady spaces (e.g. verandas) based on precipitation
- Materials and windows based on temperature and environment

1. What do we want to achieve (and who'd like to do what)?
	- [ ] Zach and Jan: Buildings
		- [ ] ?: External walls, doors and windows
		- [ ] Zach: Better interiors
			- [ ] Intentional layout
			- [ ] Reliable stairwells
			- [ ] Ensure walkability
		- [ ] Jan: Material system
		- [ ] Jan: More variation
			- [ ] Use prefabs
			- [ ] For main biome types: Default, arid, wetland
			- [ ] Stretch: Different geometries
	- [ ] Victor: Roads
		- [ ] Using vertices for roads
		- [ ] Roads beyond city
			- [ ] A* with drunken walk during search
		- [ ] Special roads for different districts
		- [ ] Street furniture (signage, lamps etc.)
	- [ ] Tim: Districts
		- [ ] More parameters
			- [ ] Surface block
			- [ ] Roughness
			- [ ] Biome (affects voronoi)
			- [ ] Water
			- [ ] Tree density
			- [ ] Border district
		- [ ] Improved Voronoi
			- [ ] Grid-based semi-random seeds
			- [ ] Distinguish unexplored vertices
		- [ ] Types
			- [ ] Urban
				- [ ] Generic
				- [ ] (Park)
				- [ ] (Slum)
				- [ ] (Market)
			- [ ] Rural
				- [ ] Wheat fields
				- [ ] (Logging)
				- [ ] (Fishing)
			- [ ] Off-limits
				- [ ] Generic
				- [ ] (Mountains)
		- [ ] (Trees)
			- [ ] Taper to border
			- [ ] Replace inland vanilla trees (less dense)
	- [ ] James: Decoration, meta and documentation
		- [ ] Help along wherever help is needed
		- [ ] District decorations
		- [ ] Street furniture
		- [ ] Gardening & trees
		- [ ] Water features (docks, boats)
2. What is out-of-scope?
	- [ ] Structure detection
	- [ ] Specialised districts & buildings
	- [ ] Economy simulation (production chains)
	- [ ] Work on agents
3. What and roughly when are our milestones?
	- See #goals
4. What are the next steps?
	- [ ] Everyone breaks down their job into smaller tasks (ideally, each task should take around 2 hours), and assigns them a priority
	- [ ] Where systems are to be created/modified, draft one or more approaches
		- [ ] Should be discussed in-group before next meeting
	- [ ]

## My tasks

- [ ] District decoration
	- [ ] Identify free spaces in district (flood fill search)
	- [ ] Determine road and house enclosure (on which sides are there houses/streets)
		- [ ] Island (surrounded by streets)
		- [ ] Peninsula (1 access to street, more street than property)
		- [ ] Cove (1 access to street, more property than street)
		- [ ] Channel (2+ accesses to street)
		- [ ] Court (surrounded by property)
	- [ ] Determine road exposure (percentage of circumferance)
		- [ ] 0: No road access
		- [ ] 1: Surrounded by road
	- [ ] Determine house enclosure
	- [ ] Select type based on size and RE
		- [ ] Filler (very small/odd)
		- [ ] Market stall (if space prominent and large enough)
		- [ ] Square
			- [ ] Benches
			- [ ] Fountain
			- [ ] Well
			- [ ] Fire pit
			- [ ] Performing stage
		- [ ] Private garden
			- [ ] Flower
			- [ ] Vegetable
			- [ ] Pen
			- [ ] Doghouse
			- [ ] Overgrown
		- [ ] Park
			- [ ] Playground
			- [ ] Picnic
			- [ ] Trees
		- [ ] Community
			- [ ] Garden
			- [ ] Oven
			- [ ] Book exchange
			- [ ] Donation box
			- [ ] Bulletin board
		- [ ] Grave
		- [ ] Stables / parking area
		- [ ] Crates and piles
		- [ ] Cultural
			- [ ] Monument / memorial (very prominent)
			- [ ] Shrine (less prominent)
			- [ ] Art
		- [ ] Agricultural
			- [ ] Scarecrows
			- [ ] Haystacks
- [ ] Street lighting
	- [ ] Coverage system
		- [ ] Maps:
			- [ ] Lighting
			- [ ] Drinking water
			- [ ] Irrigation
			- [ ] Waste
			- [ ] Goods
		- [ ] Placing furniture with coverage properties results in appropriate map update
	- [ ] Formats
		- [ ] Lamppost
			- [ ] Single
			- [ ] Double
		- [ ] Suspended/string lights
		- [ ] Wall lights (need to determine suitable walls)
		- [ ] Bollards
		- [ ] (Ground lights)
		- [ ] (Emedded lights)
- [ ] Signage
	- [ ] Navigation
		- [ ] Fingerposts
		- [ ] Arrows
		- [ ] Trail blazes
		- [ ] (Street names)
		- [ ] (Maps)
	- [ ] Informational
		- [ ] Facilities
		- [ ] Plaques
		- [ ] Rules / News
	- [ ] Cultural
		- [ ] Adverts and offers
- [ ] Street furniture
	- [ ] Benches
	- [ ] Bollards
	- [ ] Wells
	- [ ] Stalls
	- [ ] Signposts
	- [ ] Notice boards
	- [ ] Gallows, stocks etc.
	- [ ] Wayside crosses, shrines etc.
	- [ ] Rubbish bins
	- [ ] Banners and posters
	- [ ] Understood! In that case, here are some static, non-functional assets that could make a video game environment feel more alive:

>1. **Street Signs and Signage:** Decorative street signs, banners, and posters adorning buildings, walls, and lampposts, adding visual interest and character to the environment.
>2. **Statues and Sculptures:** Decorative statues, sculptures, and monuments placed in public squares, parks, and plazas, serving as landmarks and points of interest.
>3. **Fountains and Water Features:** Ornate fountains, ponds, and water features with sculpted figures and decorative motifs, enhancing the beauty and ambiance of public spaces.
>4. **Planters and Flowerpots:** Decorative planters, flowerpots, and hanging baskets filled with colorful flowers and greenery, adding vibrancy and life to streets and buildings.
>5. **Street Furniture:** Benches, tables, and chairs placed along sidewalks, in parks, and outside buildings, providing seating and resting spots for virtual inhabitants.
>6. **Street Lamps and Lanterns:** Decorative street lamps, lanterns, and torches illuminating pathways and streets, creating a warm and inviting atmosphere during nighttime.
>7. **Window Boxes and Shutters:** Window boxes filled with flowers and herbs, as well as decorative shutters and window frames, adding charm and detail to building facades.
>8. **Decorative Paving and Cobblestones:** Intricate patterns and designs created with cobblestones, bricks, and tiles, embellishing streets, squares, and courtyards.
>9. **Outdoor Art Installations:** Artistic installations and sculptures placed in outdoor spaces, such as abstract structures, kinetic art, or interactive exhibits.
>10. **Architectural Details:** Decorative architectural elements such as ornate facades, intricate carvings, and decorative moldings adorning buildings and structures.

