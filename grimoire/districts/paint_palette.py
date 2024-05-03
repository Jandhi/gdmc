from ..core.assets.asset import Asset


class PaintPalette(Asset):
    palette: dict
    smooth: bool  # true if the palette dict contains 3 dicts for blocks/slabs/stairs, false if its only a weighted dict for 'blocks'
