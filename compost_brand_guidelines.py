#!/usr/bin/env python3
"""
COMPOST - Brand Guidelines One-Page Sheet
Design Philosophy: Quiet Infrastructure
"""

from PIL import Image, ImageDraw, ImageFont
import math

# Canvas dimensions (portrait, A4-ish ratio at high res)
WIDTH = 2400
HEIGHT = 3200

# Brand colors
COLORS = {
    'bg': (22, 21, 19),
    'card': (32, 30, 27),
    'card_light': (42, 40, 36),
    'layer_3': (62, 58, 52),
    'layer_4': (82, 76, 68),
    'layer_5': (105, 98, 88),
    'sand': (148, 140, 128),
    'light': (188, 182, 172),
    'highlight': (235, 232, 226),
    'green': (82, 128, 82),
    'green_light': (108, 152, 102),
    'green_bright': (118, 168, 108),
    'error': (168, 88, 88),
}


def draw_color_swatch(draw, x, y, size, color, label, hex_code, label_font, tiny_font, text_color):
    """Draw a color swatch with label"""
    # Swatch
    draw.rectangle([x, y, x + size, y + size], fill=color)
    # Thin border for dark colors
    if sum(color) < 150:
        draw.rectangle([x, y, x + size, y + size], outline=COLORS['layer_4'], width=1)
    # Label
    draw.text((x, y + size + 12), label, font=label_font, fill=text_color)
    draw.text((x, y + size + 32), hex_code, font=tiny_font, fill=COLORS['layer_5'])


def draw_section_header(draw, x, y, text, font, color):
    """Draw a section header with subtle line"""
    draw.text((x, y), text, font=font, fill=color)
    text_bbox = draw.textbbox((x, y), text, font=font)
    line_y = y + (text_bbox[3] - text_bbox[1]) + 8
    draw.line([(x, line_y), (x + 180, line_y)], fill=COLORS['layer_4'], width=1)


def rgb_to_hex(rgb):
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def create_guidelines():
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 72)
        section_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 28)
        label_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 18)
        body_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 16)
        tiny_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 13)
        wordmark_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 48)
    except:
        title_font = ImageFont.load_default()
        section_font = title_font
        label_font = title_font
        body_font = title_font
        tiny_font = title_font
        wordmark_font = title_font

    margin = 100
    col_width = (WIDTH - margin * 3) // 2

    # === HEADER ===
    draw.text((margin, 80), "COMPOST", font=title_font, fill=COLORS['highlight'])
    draw.text((margin, 160), "Brand Guidelines v1.0", font=label_font, fill=COLORS['sand'])

    # Subtle header line
    draw.line([(margin, 210), (WIDTH - margin, 210)], fill=COLORS['layer_4'], width=1)

    # === SECTION 1: COLOR PALETTE ===
    section_y = 260
    draw_section_header(draw, margin, section_y, "COLOR PALETTE", section_font, COLORS['highlight'])

    # Primary colors
    draw.text((margin, section_y + 50), "Primary", font=label_font, fill=COLORS['sand'])

    swatch_size = 80
    swatch_y = section_y + 80
    primary_colors = [
        (COLORS['bg'], "Background", rgb_to_hex(COLORS['bg'])),
        (COLORS['highlight'], "Primary Text", rgb_to_hex(COLORS['highlight'])),
        (COLORS['sand'], "Secondary Text", rgb_to_hex(COLORS['sand'])),
        (COLORS['green'], "Accent", rgb_to_hex(COLORS['green'])),
    ]

    for i, (color, label, hex_code) in enumerate(primary_colors):
        x = margin + i * (swatch_size + 40)
        draw_color_swatch(draw, x, swatch_y, swatch_size, color, label, hex_code,
                         tiny_font, tiny_font, COLORS['light'])

    # Earth tones
    draw.text((margin, swatch_y + 140), "Earth Tones (Layering)", font=label_font, fill=COLORS['sand'])

    earth_y = swatch_y + 170
    earth_colors = [
        (COLORS['card'], "Layer 1", rgb_to_hex(COLORS['card'])),
        (COLORS['layer_3'], "Layer 2", rgb_to_hex(COLORS['layer_3'])),
        (COLORS['layer_4'], "Layer 3", rgb_to_hex(COLORS['layer_4'])),
        (COLORS['layer_5'], "Layer 4", rgb_to_hex(COLORS['layer_5'])),
        (COLORS['light'], "Layer 5", rgb_to_hex(COLORS['light'])),
    ]

    small_swatch = 60
    for i, (color, label, hex_code) in enumerate(earth_colors):
        x = margin + i * (small_swatch + 30)
        draw_color_swatch(draw, x, earth_y, small_swatch, color, label, hex_code,
                         tiny_font, tiny_font, COLORS['sand'])

    # Green accent variants
    draw.text((margin + col_width + margin, section_y + 50), "Accent Variants", font=label_font, fill=COLORS['sand'])

    green_y = section_y + 80
    green_colors = [
        (COLORS['green'], "Moss", rgb_to_hex(COLORS['green'])),
        (COLORS['green_light'], "Growth", rgb_to_hex(COLORS['green_light'])),
        (COLORS['green_bright'], "Highlight", rgb_to_hex(COLORS['green_bright'])),
    ]

    for i, (color, label, hex_code) in enumerate(green_colors):
        x = margin + col_width + margin + i * (swatch_size + 40)
        draw_color_swatch(draw, x, green_y, swatch_size, color, label, hex_code,
                         tiny_font, tiny_font, COLORS['light'])

    # Usage note
    draw.text((margin + col_width + margin, green_y + 140),
              "Green used sparingly—only for yield,", font=tiny_font, fill=COLORS['layer_5'])
    draw.text((margin + col_width + margin, green_y + 158),
              "growth, or positive indicators.", font=tiny_font, fill=COLORS['layer_5'])

    # === SECTION 2: TYPOGRAPHY ===
    section_y = 600
    draw_section_header(draw, margin, section_y, "TYPOGRAPHY", section_font, COLORS['highlight'])

    # Primary typeface
    draw.text((margin, section_y + 50), "Primary Typeface", font=label_font, fill=COLORS['sand'])
    draw.text((margin, section_y + 80), "Avenir", font=wordmark_font, fill=COLORS['highlight'])
    draw.text((margin, section_y + 140), "Light / Book weights preferred", font=tiny_font, fill=COLORS['layer_5'])
    draw.text((margin, section_y + 160), "Generous letter-spacing for headlines", font=tiny_font, fill=COLORS['layer_5'])

    # Type scale
    draw.text((margin + col_width + margin, section_y + 50), "Type Scale", font=label_font, fill=COLORS['sand'])

    type_samples = [
        ("Headline", 36, COLORS['highlight']),
        ("Subhead", 24, COLORS['sand']),
        ("Body", 16, COLORS['light']),
        ("Caption", 13, COLORS['layer_5']),
    ]

    sample_y = section_y + 85
    for label, size, color in type_samples:
        try:
            sample_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", size)
        except:
            sample_font = body_font
        draw.text((margin + col_width + margin, sample_y), label, font=sample_font, fill=color)
        draw.text((margin + col_width + margin + 200, sample_y + (size - 13)),
                  f"{size}px", font=tiny_font, fill=COLORS['layer_4'])
        sample_y += size + 16

    # === SECTION 3: TONE & VOICE ===
    section_y = 860
    draw_section_header(draw, margin, section_y, "TONE & VOICE", section_font, COLORS['highlight'])

    # Do's
    draw.text((margin, section_y + 50), "Do", font=label_font, fill=COLORS['green'])

    dos = [
        "Calm, confident, understated",
        "Technical but accessible",
        "Patient—compounding takes time",
        "Precise with numbers",
        "Infrastructure-coded language",
    ]

    do_y = section_y + 80
    for item in dos:
        draw.ellipse([margin, do_y + 6, margin + 6, do_y + 12], fill=COLORS['green'])
        draw.text((margin + 18, do_y), item, font=body_font, fill=COLORS['light'])
        do_y += 28

    # Don'ts
    draw.text((margin + col_width + margin, section_y + 50), "Don't", font=label_font, fill=COLORS['error'])

    donts = [
        "Hype, urgency, FOMO",
        "Degen culture references",
        "Exclamation marks",
        "Emojis (except sparingly)",
        "Promises of specific returns",
    ]

    dont_y = section_y + 80
    for item in donts:
        draw.line([(margin + col_width + margin, dont_y + 8),
                   (margin + col_width + margin + 8, dont_y + 8)], fill=COLORS['error'], width=2)
        draw.text((margin + col_width + margin + 18, dont_y), item, font=body_font, fill=COLORS['light'])
        dont_y += 28

    # === SECTION 4: VISUAL LANGUAGE ===
    section_y = 1150
    draw_section_header(draw, margin, section_y, "VISUAL LANGUAGE", section_font, COLORS['highlight'])

    # Principles
    principles = [
        ("Sedimentary Layers", "Horizontal bands suggesting accumulation over time"),
        ("Organic Growth", "Green accents rising through layers—value compounding"),
        ("Negative Space", "Generous margins; ideas need room to breathe"),
        ("Subtle Texture", "Fine grain; nothing too clean or digital"),
        ("Data as Design", "Numbers integrated visually, not decorated"),
    ]

    princ_y = section_y + 50
    for title, desc in principles:
        draw.text((margin, princ_y), title, font=label_font, fill=COLORS['sand'])
        draw.text((margin + 200, princ_y), desc, font=body_font, fill=COLORS['layer_5'])
        princ_y += 36

    # Visual example - mini layer diagram
    example_x = margin + col_width + margin
    example_y = section_y + 60
    layer_h = 24

    for i, color in enumerate([COLORS['layer_5'], COLORS['layer_4'], COLORS['layer_3'], COLORS['card']]):
        draw.rectangle([example_x, example_y + i * layer_h,
                       example_x + 280, example_y + (i + 1) * layer_h], fill=color)

    # Green stem in example
    stem_x = example_x + 140
    for y in range(example_y + 10, example_y + layer_h * 4 - 10, 6):
        draw.ellipse([stem_x - 2, y - 2, stem_x + 2, y + 2], fill=COLORS['green'])

    # Nodes
    for i, progress in enumerate([0.3, 0.6, 0.9]):
        node_y = example_y + layer_h * 4 - int(layer_h * 4 * progress) + 5
        node_size = 4 + progress * 6
        draw.ellipse([stem_x - node_size, node_y - node_size,
                     stem_x + node_size, node_y + node_size], fill=COLORS['green'])

    draw.text((example_x, example_y + layer_h * 4 + 15),
              "Value rising through layers", font=tiny_font, fill=COLORS['layer_5'])

    # === SECTION 5: SPACING & GRID ===
    section_y = 1420
    draw_section_header(draw, margin, section_y, "SPACING", section_font, COLORS['highlight'])

    draw.text((margin, section_y + 50), "Base unit: 8px", font=body_font, fill=COLORS['light'])
    draw.text((margin, section_y + 78), "Margins: Generous (80-120px at large sizes)", font=body_font, fill=COLORS['light'])
    draw.text((margin, section_y + 106), "Letter-spacing headlines: +2-4%", font=body_font, fill=COLORS['light'])
    draw.text((margin, section_y + 134), "Line-height body: 1.6", font=body_font, fill=COLORS['light'])

    # Spacing visual
    spacing_x = margin + col_width + margin
    spacing_y = section_y + 50

    # Show 8px grid
    for i in range(8):
        x = spacing_x + i * 24
        draw.rectangle([x, spacing_y, x + 20, spacing_y + 20],
                      fill=COLORS['card'] if i % 2 == 0 else COLORS['layer_3'])
    draw.text((spacing_x, spacing_y + 30), "8px base unit", font=tiny_font, fill=COLORS['layer_5'])

    # === SECTION 6: LOGO USAGE ===
    section_y = 1620
    draw_section_header(draw, margin, section_y, "WORDMARK", section_font, COLORS['highlight'])

    # Primary wordmark
    draw.rectangle([margin, section_y + 50, margin + 320, section_y + 130], fill=COLORS['card'])
    # Wordmark with spacing
    wordmark = "COMPOST"
    wm_x = margin + 40
    wm_y = section_y + 70
    for char in wordmark:
        draw.text((wm_x, wm_y), char, font=wordmark_font, fill=COLORS['highlight'])
        bbox = draw.textbbox((0, 0), char, font=wordmark_font)
        wm_x += (bbox[2] - bbox[0]) + 8

    draw.text((margin, section_y + 145), "Primary (dark bg)", font=tiny_font, fill=COLORS['layer_5'])

    # Reversed
    draw.rectangle([margin + 360, section_y + 50, margin + 680, section_y + 130], fill=COLORS['highlight'])
    wm_x = margin + 400
    for char in wordmark:
        draw.text((wm_x, wm_y), char, font=wordmark_font, fill=COLORS['bg'])
        bbox = draw.textbbox((0, 0), char, font=wordmark_font)
        wm_x += (bbox[2] - bbox[0]) + 8

    draw.text((margin + 360, section_y + 145), "Reversed (light bg)", font=tiny_font, fill=COLORS['layer_5'])

    # Clear space
    draw.text((margin + col_width + margin, section_y + 50), "Clear Space", font=label_font, fill=COLORS['sand'])
    draw.text((margin + col_width + margin, section_y + 80),
              "Minimum clear space = height of 'O'", font=body_font, fill=COLORS['light'])
    draw.text((margin + col_width + margin, section_y + 108),
              "in the wordmark on all sides", font=body_font, fill=COLORS['light'])

    # === FOOTER ===
    draw.line([(margin, HEIGHT - 120), (WIDTH - margin, HEIGHT - 120)], fill=COLORS['layer_4'], width=1)
    draw.text((margin, HEIGHT - 90), "COMPOST", font=label_font, fill=COLORS['sand'])
    draw.text((margin, HEIGHT - 65), "Brand Guidelines v1.0", font=tiny_font, fill=COLORS['layer_5'])
    draw.text((WIDTH - margin - 200, HEIGHT - 90), "Confidential", font=tiny_font, fill=COLORS['layer_4'])

    # Corner brackets
    bracket_len = 35
    bm = 50
    for cx, cy, dx, dy in [(bm, bm, 1, 1), (WIDTH-bm, bm, -1, 1),
                            (bm, HEIGHT-bm, 1, -1), (WIDTH-bm, HEIGHT-bm, -1, -1)]:
        draw.line([(cx, cy), (cx + bracket_len * dx, cy)], fill=COLORS['sand'], width=1)
        draw.line([(cx, cy), (cx, cy + bracket_len * dy)], fill=COLORS['sand'], width=1)

    return img


if __name__ == "__main__":
    guidelines = create_guidelines()
    guidelines.save("/Users/andy/Test Anti G projects/compost_brand_guidelines.png", "PNG", dpi=(150, 150))
    print("Brand guidelines saved: compost_brand_guidelines.png")
