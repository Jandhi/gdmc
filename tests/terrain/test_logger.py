# Allows code to be run in root directory
import sys

sys.path[0] = sys.path[0].removesuffix("\\tests\\terrain")

# Actual file
from gdpc import Editor, Block
from grimoire.terrain.tree_cutter import log_trees

editor = Editor(buffering=True, caching=True)

area = editor.getBuildArea()
editor.transform = (area.begin.x, 0, area.begin.z)

print("Loading world slice...")
build_rect = area.toRect()
world_slice = editor.loadWorldSlice(build_rect)
print("World slice loaded!")

log_trees(editor, build_rect, world_slice)
