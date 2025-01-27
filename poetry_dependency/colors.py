from enum import Enum

class Color(str, Enum):
    
    # Blacks and Whites
    BLACK = "#000000"
    WHITE = "#FFFFFF"

    # Blues
    NAVY = "#000080"
    DARK_BLUE = "#00008B"
    BLUE = "#0000FF"
    LIGHT_BLUE = "#ADD8E6"

    # Greens
    DARK_GREEN = "#006400"
    TEAL = "#008080"
    DARK_CYAN = "#008B8B"
    GREEN = "#00FF00"
    LIME = "#00FF00"
    LIGHT_GREEN = "#90EE90"

    # Cyans
    CYAN = "#00FFFF"
    LIGHT_CYAN = "#E0FFFF"

    # Grays
    DARK_SLATE_GRAY = "#2F4F4F"
    DIM_GRAY = "#696969"
    SLATE_GRAY = "#708090"
    LIGHT_SLATE_GRAY = "#778899"
    DARK_GRAY = "#A9A9A9"
    GRAY = "#808080"
    SILVER = "#C0C0C0"
    DARK_SILVER = "#AFAFAF"
    LIGHT_GRAY = "#D3D3D3"
    LIGHT_SILVER = "#F5F5F5"

    # Reds
    DARK_RED = "#8B0000"
    RED = "#FF0000"
    LIGHT_RED = "#FF7F7F"

    # Oranges
    DARK_ORANGE = "#FF8C00"
    ORANGE = "#FFA500"
    LIGHT_ORANGE = "#FFDAB9"

    # Yellows
    DARK_YELLOW = "#9B870C"
    YELLOW = "#FFFF00"
    LIGHT_YELLOW = "#FFFFE0"

    # Magentas
    DARK_MAGENTA = "#8B008B"
    PURPLE = "#800080"
    LIGHT_MAGENTA = "#FF77FF"
    MAGENTA = "#FF00FF"

    # Pinks
    DARK_PINK = "#FF1493"
    PINK = "#FFC0CB"
    LIGHT_PINK = "#FFB6C1"

    # Browns
    DARK_BROWN = "#5C4033"
    BROWN = "#A52A2A"
    LIGHT_BROWN = "#DEB887"

    # Purples
    DARK_PURPLE = "#4B0082"
    LIGHT_PURPLE = "#E6E6FA"

    # Golds
    DARK_GOLD = "#B8860B"
    GOLD = "#FFD700"
    LIGHT_GOLD = "#FFF8DC"