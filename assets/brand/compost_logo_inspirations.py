#!/usr/bin/env python3
"""
COMPOST - Logo Inspirations Sheet
Design Philosophy: Quiet Infrastructure
"""

from PIL import Image, ImageDraw, ImageFont
import math

# Canvas dimensions
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
}


def draw_logo_card(draw, x, y, width, height, bg_color=None):
    """Draw a card background for logo display"""
    if bg_color is None:
        bg_color = COLORS['card']
    draw.rectangle([x, y, x + width, y + height], fill=bg_color)


def draw_logo_label(draw, x, y, title, description, title_font, desc_font):
    """Draw logo variant label"""
    draw.text((x, y), title, font=title_font, fill=COLORS['sand'])
    draw.text((x, y + 24), description, font=desc_font, fill=COLORS['layer_5'])


# === LOGO CONCEPTS ===

def draw_logo_stacked_layers(draw, cx, cy, size, colors):
    """
    Concept 1: Stacked horizontal layers
    Represents sedimentary accumulation, capital layering
    """
    layer_count = 5
    layer_height = size * 0.12
    gap = size * 0.04
    total_height = layer_count * layer_height + (layer_count - 1) * gap
    start_y = cy - total_height / 2

    layer_colors = [
        COLORS['layer_5'],
        COLORS['layer_4'],
        COLORS['layer_3'],
        COLORS['card_light'],
        COLORS['card'],
    ]

    for i in range(layer_count):
        layer_y = start_y + i * (layer_height + gap)
        # Each layer slightly different width for organic feel
        width_factor = 1.0 - i * 0.08
        layer_width = size * 0.8 * width_factor
        draw.rectangle([
            cx - layer_width / 2, layer_y,
            cx + layer_width / 2, layer_y + layer_height
        ], fill=layer_colors[i])

    # Green accent - growth emerging from top
    accent_height = size * 0.25
    accent_width = size * 0.06
    accent_y = start_y - accent_height - gap
    draw.rectangle([
        cx - accent_width / 2, accent_y,
        cx + accent_width / 2, start_y - gap
    ], fill=COLORS['green'])

    # Small node at top
    node_r = size * 0.05
    draw.ellipse([
        cx - node_r, accent_y - node_r,
        cx + node_r, accent_y + node_r
    ], fill=COLORS['green_bright'])


def draw_logo_circular_layers(draw, cx, cy, size, colors):
    """
    Concept 2: Concentric circles / rings
    Represents accumulation radiating outward, compounding
    """
    ring_count = 4
    max_r = size * 0.45
    ring_width = size * 0.08

    ring_colors = [
        COLORS['card'],
        COLORS['layer_3'],
        COLORS['layer_4'],
        COLORS['layer_5'],
    ]

    for i in range(ring_count - 1, -1, -1):
        r = max_r - i * (ring_width + size * 0.02)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ring_colors[i])

    # Center - green core
    core_r = size * 0.12
    draw.ellipse([cx - core_r, cy - core_r, cx + core_r, cy + core_r], fill=COLORS['green'])
    inner_r = core_r * 0.5
    draw.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r], fill=COLORS['green_bright'])


def draw_logo_stem_minimal(draw, cx, cy, size, colors):
    """
    Concept 3: Minimal stem with nodes
    Abstract representation of growth/compounding
    """
    stem_height = size * 0.7
    stem_width = size * 0.04
    start_y = cy + stem_height / 2

    # Stem
    draw.rectangle([
        cx - stem_width / 2, cy - stem_height / 2,
        cx + stem_width / 2, cy + stem_height / 2
    ], fill=COLORS['green'])

    # Nodes - increasing in size (compounding)
    node_positions = [0.25, 0.55, 0.85]
    for i, pos in enumerate(node_positions):
        node_y = start_y - stem_height * pos
        node_r = size * (0.06 + i * 0.03)
        draw.ellipse([
            cx - node_r, node_y - node_r,
            cx + node_r, node_y + node_r
        ], fill=COLORS['green'])
        # Inner
        inner_r = node_r * 0.5
        draw.ellipse([
            cx - inner_r, node_y - inner_r,
            cx + inner_r, node_y + inner_r
        ], fill=COLORS['green_bright'])


def draw_logo_letter_c(draw, cx, cy, size, colors):
    """
    Concept 4: Stylized letter C with layers
    Lettermark approach
    """
    # Outer C shape with layers
    outer_r = size * 0.4
    inner_r = size * 0.25
    gap_angle = math.radians(70)  # Gap in the C

    # Draw layered C
    layer_widths = [outer_r, outer_r * 0.85, outer_r * 0.7]
    layer_colors = [COLORS['layer_5'], COLORS['layer_4'], COLORS['layer_3']]

    for r, color in zip(layer_widths, layer_colors):
        # Draw arc segments
        points = []
        for angle in range(-140, 140, 5):
            rad = math.radians(angle)
            points.append((cx + math.cos(rad) * r, cy + math.sin(rad) * r))

        # Draw as thick line segments
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=color, width=int(size * 0.08))

    # Green accent at opening
    accent_y = cy - size * 0.15
    accent_r = size * 0.06
    draw.ellipse([
        cx + outer_r * 0.35 - accent_r, accent_y - accent_r,
        cx + outer_r * 0.35 + accent_r, accent_y + accent_r
    ], fill=COLORS['green_bright'])


def draw_logo_square_layers(draw, cx, cy, size, colors):
    """
    Concept 5: Square/rectangular layers stacked
    More geometric, architectural feel
    """
    layer_count = 4
    base_size = size * 0.65
    layer_height = size * 0.12
    gap = size * 0.03

    total_height = layer_count * layer_height + (layer_count - 1) * gap
    start_y = cy - total_height / 2 + size * 0.1

    layer_colors = [
        COLORS['layer_5'],
        COLORS['layer_4'],
        COLORS['layer_3'],
        COLORS['card_light'],
    ]

    for i in range(layer_count):
        layer_y = start_y + i * (layer_height + gap)
        # Progressive width
        width = base_size * (1.0 - i * 0.1)
        draw.rectangle([
            cx - width / 2, layer_y,
            cx + width / 2, layer_y + layer_height
        ], fill=layer_colors[i])

    # Green bar at top
    bar_width = base_size * 0.15
    bar_height = size * 0.25
    draw.rectangle([
        cx - bar_width / 2, start_y - bar_height - gap,
        cx + bar_width / 2, start_y - gap
    ], fill=COLORS['green'])


def draw_logo_abstract_growth(draw, cx, cy, size, colors):
    """
    Concept 6: Abstract upward growth
    Multiple stems converging
    """
    # Three stems rising and converging
    stem_positions = [-0.2, 0, 0.2]
    stem_heights = [0.5, 0.7, 0.55]

    base_y = cy + size * 0.3

    for i, (x_offset, h_factor) in enumerate(zip(stem_positions, stem_heights)):
        stem_x = cx + x_offset * size
        stem_height = size * h_factor
        stem_width = size * 0.05

        # Converge toward center at top
        top_x = cx + x_offset * size * 0.3
        top_y = base_y - stem_height

        # Draw as polygon for tapered effect
        points = [
            (stem_x - stem_width, base_y),
            (stem_x + stem_width, base_y),
            (top_x + stem_width * 0.5, top_y),
            (top_x - stem_width * 0.5, top_y),
        ]
        draw.polygon(points, fill=COLORS['green'] if i == 1 else COLORS['green'])

    # Central node at convergence point
    node_y = base_y - size * 0.7
    node_r = size * 0.08
    draw.ellipse([cx - node_r, node_y - node_r, cx + node_r, node_y + node_r], fill=COLORS['green_bright'])


def draw_logo_monogram_cp(draw, cx, cy, size, colors):
    """
    Concept 7: C + P monogram
    Interlocked letters
    """
    # Simple geometric C and P shapes
    stroke = int(size * 0.1)

    # C - left side
    c_r = size * 0.28
    c_cx = cx - size * 0.12

    # Draw C as arcs
    for angle in range(-130, 130, 8):
        rad = math.radians(angle)
        x = c_cx + math.cos(rad) * c_r
        y = cy + math.sin(rad) * c_r
        draw.ellipse([x - stroke/2, y - stroke/2, x + stroke/2, y + stroke/2], fill=COLORS['highlight'])

    # P - right side (simplified as vertical + half circle)
    p_x = cx + size * 0.08
    p_top = cy - size * 0.3
    p_mid = cy - size * 0.05
    p_bottom = cy + size * 0.3

    # Vertical stroke
    draw.rectangle([p_x - stroke/2, p_top, p_x + stroke/2, p_bottom], fill=COLORS['highlight'])

    # P bowl
    bowl_r = size * 0.15
    bowl_cx = p_x + stroke/2
    bowl_cy = (p_top + p_mid) / 2 + size * 0.05

    for angle in range(-90, 90, 8):
        rad = math.radians(angle)
        x = bowl_cx + math.cos(rad) * bowl_r
        y = bowl_cy + math.sin(rad) * bowl_r
        draw.ellipse([x - stroke/2, y - stroke/2, x + stroke/2, y + stroke/2], fill=COLORS['highlight'])


def draw_logo_seed_sprout(draw, cx, cy, size, colors):
    """
    Concept 8: Seed/sprout emerging
    Organic, growth metaphor
    """
    # Seed base (oval)
    seed_w = size * 0.35
    seed_h = size * 0.25
    seed_y = cy + size * 0.15

    draw.ellipse([
        cx - seed_w, seed_y - seed_h,
        cx + seed_w, seed_y + seed_h
    ], fill=COLORS['layer_4'])

    # Inner seed
    inner_w = seed_w * 0.7
    inner_h = seed_h * 0.7
    draw.ellipse([
        cx - inner_w, seed_y - inner_h,
        cx + inner_w, seed_y + inner_h
    ], fill=COLORS['layer_3'])

    # Sprout emerging
    sprout_height = size * 0.45
    sprout_width = size * 0.06
    sprout_top = seed_y - seed_h - sprout_height

    # Curved sprout (simplified as rectangle)
    draw.rectangle([
        cx - sprout_width / 2, sprout_top,
        cx + sprout_width / 2, seed_y - seed_h * 0.5
    ], fill=COLORS['green'])

    # Leaf/node at top
    leaf_r = size * 0.08
    draw.ellipse([
        cx - leaf_r, sprout_top - leaf_r * 0.5,
        cx + leaf_r, sprout_top + leaf_r * 1.5
    ], fill=COLORS['green_bright'])


def draw_logo_data_bars(draw, cx, cy, size, colors):
    """
    Concept 9: Rising data bars
    Finance/infrastructure feel
    """
    bar_count = 5
    bar_width = size * 0.1
    gap = size * 0.05
    total_width = bar_count * bar_width + (bar_count - 1) * gap

    heights = [0.3, 0.45, 0.7, 0.55, 0.4]  # Varying heights
    base_y = cy + size * 0.25

    start_x = cx - total_width / 2

    bar_colors = [
        COLORS['layer_5'],
        COLORS['layer_4'],
        COLORS['green'],  # Center bar in green
        COLORS['layer_4'],
        COLORS['layer_5'],
    ]

    for i in range(bar_count):
        bar_x = start_x + i * (bar_width + gap)
        bar_height = size * heights[i]
        bar_top = base_y - bar_height

        draw.rectangle([
            bar_x, bar_top,
            bar_x + bar_width, base_y
        ], fill=bar_colors[i])

    # Node on top of center bar
    center_x = start_x + 2 * (bar_width + gap) + bar_width / 2
    node_y = base_y - size * heights[2] - size * 0.05
    node_r = size * 0.05
    draw.ellipse([
        center_x - node_r, node_y - node_r,
        center_x + node_r, node_y + node_r
    ], fill=COLORS['green_bright'])


def create_logo_sheet():
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 72)
        section_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 28)
        label_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 18)
        desc_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 14)
        tiny_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", 13)
    except:
        title_font = ImageFont.load_default()
        section_font = title_font
        label_font = title_font
        desc_font = title_font
        tiny_font = title_font

    margin = 100
    card_width = 340
    card_height = 280
    gap = 50

    # === HEADER ===
    draw.text((margin, 80), "COMPOST", font=title_font, fill=COLORS['highlight'])
    draw.text((margin, 160), "Logo Explorations", font=label_font, fill=COLORS['sand'])
    draw.line([(margin, 210), (WIDTH - margin, 210)], fill=COLORS['layer_4'], width=1)

    # === LOGO GRID ===
    logos = [
        (draw_logo_stacked_layers, "Stacked Layers", "Sedimentary accumulation"),
        (draw_logo_circular_layers, "Concentric Rings", "Radiating growth"),
        (draw_logo_stem_minimal, "Growth Stem", "Compounding nodes"),
        (draw_logo_letter_c, "Letter C", "Layered letterform"),
        (draw_logo_square_layers, "Geometric Stack", "Architectural layers"),
        (draw_logo_abstract_growth, "Convergent Growth", "Multiple streams"),
        (draw_logo_monogram_cp, "CP Monogram", "Interlocked initials"),
        (draw_logo_seed_sprout, "Seed & Sprout", "Organic emergence"),
        (draw_logo_data_bars, "Data Bars", "Infrastructure/finance"),
    ]

    cols = 3
    start_y = 280

    for i, (logo_func, title, desc) in enumerate(logos):
        col = i % cols
        row = i // cols

        x = margin + col * (card_width + gap)
        y = start_y + row * (card_height + 80)

        # Card background
        draw_logo_card(draw, x, y, card_width, card_height)

        # Draw logo centered in card
        logo_cx = x + card_width / 2
        logo_cy = y + card_height / 2
        logo_func(draw, logo_cx, logo_cy, 160, COLORS)

        # Label
        draw_logo_label(draw, x, y + card_height + 12, title, desc, label_font, desc_font)

    # === RECOMMENDED SECTION ===
    rec_y = start_y + 3 * (card_height + 80) + 40
    draw.text((margin, rec_y), "RECOMMENDED DIRECTIONS", font=section_font, fill=COLORS['highlight'])
    draw.line([(margin, rec_y + 40), (margin + 280, rec_y + 40)], fill=COLORS['layer_4'], width=1)

    recommendations = [
        "1. Stacked Layers — Most aligned with 'capital allocation layer' positioning",
        "2. Growth Stem — Clean, memorable, conveys compounding",
        "3. Data Bars — Strong finance/infrastructure signal",
    ]

    rec_text_y = rec_y + 60
    for rec in recommendations:
        draw.ellipse([margin, rec_text_y + 5, margin + 6, rec_text_y + 11], fill=COLORS['green'])
        draw.text((margin + 18, rec_text_y), rec, font=label_font, fill=COLORS['light'])
        rec_text_y += 32

    # === NOTES ===
    notes_y = rec_text_y + 40
    draw.text((margin, notes_y), "Notes:", font=label_font, fill=COLORS['sand'])
    notes = [
        "All concepts use the established color palette",
        "Green accent appears sparingly—growth/yield signal",
        "Geometric forms preferred over organic flourishes",
        "Icon should work at 16px favicon size",
    ]

    notes_text_y = notes_y + 28
    for note in notes:
        draw.text((margin + 12, notes_text_y), "·  " + note, font=desc_font, fill=COLORS['layer_5'])
        notes_text_y += 24

    # === FOOTER ===
    draw.line([(margin, HEIGHT - 120), (WIDTH - margin, HEIGHT - 120)], fill=COLORS['layer_4'], width=1)
    draw.text((margin, HEIGHT - 90), "COMPOST", font=label_font, fill=COLORS['sand'])
    draw.text((margin, HEIGHT - 65), "Logo Explorations v1.0", font=tiny_font, fill=COLORS['layer_5'])

    # Corner brackets
    bracket_len = 35
    bm = 50
    for cx, cy, dx, dy in [(bm, bm, 1, 1), (WIDTH-bm, bm, -1, 1),
                            (bm, HEIGHT-bm, 1, -1), (WIDTH-bm, HEIGHT-bm, -1, -1)]:
        draw.line([(cx, cy), (cx + bracket_len * dx, cy)], fill=COLORS['sand'], width=1)
        draw.line([(cx, cy), (cx, cy + bracket_len * dy)], fill=COLORS['sand'], width=1)

    return img


if __name__ == "__main__":
    sheet = create_logo_sheet()
    sheet.save("/Users/andy/Test Anti G projects/compost_logo_inspirations.png", "PNG", dpi=(150, 150))
    print("Logo inspirations saved: compost_logo_inspirations.png")
