**Feature branch: `None`**

Since the inhabited area will likely contain specialised regions, these will need to be defined.
They may make use of various objects, see #9 and #14

## Geographic
- [ ] Ocean
- [ ] River
- [ ] Lake: larger than a chunk
- [ ] Pond: smaller than a chunk
- [ ] Lava lake

## Residence
- [ ] ***(essential)*** Gathering place
- [ ] ***(essential)*** Campsite
- [ ] ***(essential)*** Housing
- [ ] Labour camp: near natural resource
- [ ] Refugee camp: far from illager structures

## Transport
- [ ] Docks: by the ocean in a large settlement

## Food, drink and health
- [ ] ***(essential)*** Farmland: flat, fertile soil; large, irregularly shaped surfaces

## Defence
- [ ] Military encampment
- [ ] Training grounds: in settlement or military encampment

## Industry
- [ ] ***(essential)*** Workshops
- [ ] Logging site: in forest
- [ ] Quarry / surface mine: near cliff exposed stone
- [ ] Shipyard: adjoining docks by the ocean

## Culture
- [ ] Marketplace: on busy intersections
- [ ] Ruins: in isolated locations
- [ ] ***(essential)*** Burial grounds: flat terrain on outskirts of settlement
- [ ] Hermitage: in almost inaccessible location

# Implementation suggestion
```py
class Area():
  parent = None  # optionally contains Area instance
  surface = []  # list of (x, y, z) tuples
  access_points = [] # list of (x, y, z) points for pathfinding
  
  
  populate():
    # place stuff, maybe terraform

  fitness(x, y, z):
    """"Determine the suitability of a given block to be in the area.""

```