def hex_to_rgb(st):
    return f"{int(st[1:3], 16)},{int(st[3:5], 16)},{int(st[5:7], 16)}"


def generate(palette):
    return f"""\
[ColorEffects:Disabled]
Color={hex_to_rgb(palette["dawn"]["surface"])}
ColorAmount=0.47500000000000003
ColorEffect=2
ContrastAmount=0
ContrastEffect=0
IntensityAmount=-0.7000000000000001
IntensityEffect=0

[ColorEffects:Inactive]
ChangeSelectionColor=true
Color={hex_to_rgb(palette["dawn"]["overlay"])}
ColorAmount=0.5
ColorEffect=3
ContrastAmount=0
ContrastEffect=0
Enable=false
IntensityAmount=0
IntensityEffect=0

[Colors:Button]
BackgroundAlternate={hex_to_rgb(palette["dawn"]["highlight_med"])}
BackgroundNormal={hex_to_rgb(palette["dawn"]["overlay"])}
DecorationFocus={hex_to_rgb(palette["dawn"]["text"])}
DecorationHover={hex_to_rgb(palette["dawn"]["highlight_med"])}
ForegroundActive={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundInactive={hex_to_rgb(palette["dawn"]["muted"])}
ForegroundLink={hex_to_rgb(palette["dawn"]["rose"])}
ForegroundNegative={hex_to_rgb(palette["moon"]["rose"])}
ForegroundNeutral={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundNormal={hex_to_rgb(palette["dawn"]["pine"])}
ForegroundPositive={hex_to_rgb(palette["dawn"]["tree"])}
ForegroundVisited={hex_to_rgb(palette["dawn"]["tree"])}

[Colors:Complementary]
BackgroundAlternate={hex_to_rgb(palette["moon"]["overlay"])}
BackgroundNormal={hex_to_rgb(palette["moon"]["base"])}
DecorationFocus={hex_to_rgb(palette["moon"]["iris"])}
DecorationHover={hex_to_rgb(palette["moon"]["highlight_low"])}
ForegroundActive={hex_to_rgb(palette["moon"]["gold"])}
ForegroundInactive={hex_to_rgb(palette["moon"]["muted"])}
ForegroundLink={hex_to_rgb(palette["moon"]["rose"])}
ForegroundNegative={hex_to_rgb(palette["dawn"]["rose"])}
ForegroundNeutral={hex_to_rgb(palette["moon"]["tree"])}
ForegroundNormal={hex_to_rgb(palette["moon"]["text"])}
ForegroundPositive={hex_to_rgb(palette["moon"]["tree"])}
ForegroundVisited={hex_to_rgb(palette["moon"]["tree"])}

[Colors:Selection]
BackgroundAlternate={hex_to_rgb(palette["dawn"]["muted"])}
BackgroundNormal={hex_to_rgb(palette["dawn"]["iris"])}
DecorationFocus={hex_to_rgb(palette["dawn"]["text"])}
DecorationHover={hex_to_rgb(palette["dawn"]["pine"])}
ForegroundActive={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundInactive={hex_to_rgb(palette["dawn"]["foam"])}
ForegroundLink={hex_to_rgb(palette["dawn"]["rose"])}
ForegroundNegative={hex_to_rgb(palette["moon"]["rose"])}
ForegroundNeutral={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundNormal={hex_to_rgb(palette["dawn"]["base"])}
ForegroundPositive={hex_to_rgb(palette["dawn"]["tree"])}
ForegroundVisited={hex_to_rgb(palette["dawn"]["tree"])}

[Colors:Tooltip]
BackgroundAlternate={hex_to_rgb(palette["moon"]["overlay"])}
BackgroundNormal={hex_to_rgb(palette["dawn"]["overlay"])}
DecorationFocus={hex_to_rgb(palette["dawn"]["text"])}
DecorationHover={hex_to_rgb(palette["dawn"]["highlight_med"])}
ForegroundActive={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundInactive={hex_to_rgb(palette["dawn"]["muted"])}
ForegroundLink={hex_to_rgb(palette["dawn"]["rose"])}
ForegroundNegative={hex_to_rgb(palette["moon"]["rose"])}
ForegroundNeutral={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundNormal={hex_to_rgb(palette["dawn"]["text"])}
ForegroundPositive={hex_to_rgb(palette["dawn"]["tree"])}
ForegroundVisited={hex_to_rgb(palette["dawn"]["tree"])}

[Colors:View]
BackgroundAlternate={hex_to_rgb(palette["dawn"]["base"])}
BackgroundNormal={hex_to_rgb(palette["dawn"]["surface"])}
DecorationFocus={hex_to_rgb(palette["dawn"]["text"])}
DecorationHover={hex_to_rgb(palette["dawn"]["highlight_high"])}
ForegroundActive={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundInactive={hex_to_rgb(palette["dawn"]["muted"])}
ForegroundLink={hex_to_rgb(palette["dawn"]["rose"])}
ForegroundNegative={hex_to_rgb(palette["moon"]["rose"])}
ForegroundNeutral={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundNormal={hex_to_rgb(palette["dawn"]["pine"])}
ForegroundPositive={hex_to_rgb(palette["dawn"]["tree"])}
ForegroundVisited={hex_to_rgb(palette["dawn"]["tree"])}

[Colors:Window]
BackgroundAlternate={hex_to_rgb(palette["dawn"]["overlay"])}
BackgroundNormal={hex_to_rgb(palette["dawn"]["base"])}
DecorationFocus={hex_to_rgb(palette["dawn"]["text"])}
DecorationHover={hex_to_rgb(palette["dawn"]["highlight_med"])}
ForegroundActive={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundInactive={hex_to_rgb(palette["dawn"]["muted"])}
ForegroundLink={hex_to_rgb(palette["dawn"]["rose"])}
ForegroundNegative={hex_to_rgb(palette["moon"]["rose"])}
ForegroundNeutral={hex_to_rgb(palette["dawn"]["gold"])}
ForegroundNormal={hex_to_rgb(palette["dawn"]["pine"])}
ForegroundPositive={hex_to_rgb(palette["dawn"]["tree"])}
ForegroundVisited={hex_to_rgb(palette["dawn"]["tree"])}

[General]
ColorScheme={palette["__name__"]}
Name={palette["__name__"]}
TintFactor=0.14
TitlebarIsAccentColored=true
shadeSortColumn=true

[KDE]
contrast=1

[WM]
activeBackground={hex_to_rgb(palette["dawn"]["text"])}
activeBlend={hex_to_rgb(palette["dawn"]["pine"])}
activeForeground={hex_to_rgb(palette["dawn"]["surface"])}
inactiveBackground={hex_to_rgb(palette["dawn"]["overlay"])}
inactiveBlend={hex_to_rgb(palette["dawn"]["text"])}
inactiveForeground={hex_to_rgb(palette["dawn"]["text"])}
"""
