def hex_to_rgb(st):
    return f"{int(st[1:3], 16)},{int(st[3:5], 16)},{int(st[5:7], 16)}"

def generate(palette):
    return f"""\
[Foreground]
Color={hex_to_rgb(palette["moon"]["highlight_high"])}

[ForegroundFaint]
Color={hex_to_rgb(palette["dawn"]["text"])}

[ForegroundIntense]
Color={hex_to_rgb(palette["moon"]["overlay"])}

[Background]
Color={hex_to_rgb(palette["dawn"]["base"])}

[BackgroundFaint]
Color={hex_to_rgb(palette["dawn"]["overlay"])}

[BackgroundIntense]
Color={hex_to_rgb(palette["dawn"]["surface"])}


# Like background
[Color0]
Color={hex_to_rgb(palette["dawn"]["base"])}

[Color0Intense]
Color={hex_to_rgb(palette["dawn"]["highlight_high"])}

[Color0Faint]
Color={hex_to_rgb(palette["dawn"]["highlight_med"])}


# Red
[Color1]
Color={hex_to_rgb(palette["dawn"]["love"])}

[Color1Intense]
Color={hex_to_rgb(palette["moon"]["love"])}

[Color1Faint]
Color={hex_to_rgb(palette["main"]["love"])}


# Green
[Color2]
Color={hex_to_rgb(palette["dawn"]["tree"])}

[Color2Intense]
Color={hex_to_rgb(palette["moon"]["tree"])}

[Color2Faint]
Color={hex_to_rgb(palette["main"]["tree"])}


# Yellow
[Color3]
Color={hex_to_rgb(palette["dawn"]["gold"])}

[Color3Intense]
Color={hex_to_rgb(palette["moon"]["iris"])}

[Color3Faint]
Color={hex_to_rgb(palette["main"]["iris"])}


# Blue
[Color4]
Color={hex_to_rgb(palette["dawn"]["iris"])}

[Color4Intense]
Color={hex_to_rgb(palette["moon"]["gold"])}

[Color4Faint]
Color={hex_to_rgb(palette["main"]["gold"])}


# Magenta
[Color5]
Color={hex_to_rgb(palette["dawn"]["rose"])}

[Color5Intense]
Color={hex_to_rgb(palette["moon"]["rose"])}

[Color5Faint]
Color={hex_to_rgb(palette["main"]["rose"])}


# Cyan
[Color6]
Color={hex_to_rgb(palette["dawn"]["pine"])}

[Color6Intense]
Color={hex_to_rgb(palette["moon"]["pine"])}

[Color6Faint]
Color={hex_to_rgb(palette["main"]["pine"])}


# Opposite
[Color7]
Color={hex_to_rgb(palette["main"]["highlight_med"])}

[Color7Intense]
Color={hex_to_rgb(palette["main"]["highlight_high"])}

[Color7Faint]
Color={hex_to_rgb(palette["main"]["highlight_low"])}


[General]
Anchor=0.5,0.5
Blur=true
ColorRandomization=false
Description=Rosé Sakura Dawn
FillStyle=Tile
Opacity=0.85
Wallpaper=
WallpaperFlipType=NoFlip
WallpaperOpacity=1

"""
