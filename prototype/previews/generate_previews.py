"""Generate viewable SVG design boards for the Stump'd homepage concept."""

from html import escape
from pathlib import Path

NAVY = "#10141E"
GOLD = "#C17A22"
CREAM = "#E1D0B3"
RED = "#941E38"
WHITE = "#F4F4F4"
BLACK = "#000000"


def text(x, y, value, size, colour=CREAM, weight=400, family="Arial", anchor="start"):
    return (
        f'<text x="{x}" y="{y}" fill="{colour}" font-family="{family}" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'
    )


def multiline(x, y, lines, size, colour=CREAM, weight=400, leading=1.2, family="Arial"):
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else size * leading}">{escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )
    return f'<text x="{x}" y="{y}" fill="{colour}" font-family="{family}" font-size="{size}" font-weight="{weight}">{spans}</text>'


def rect(x, y, width, height, fill, stroke="none", radius=0, stroke_width=1):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'


def desktop():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="4050" viewBox="0 0 1440 4050">', rect(0, 0, 1440, 4050, NAVY)]
    out += [rect(0, 0, 1440, 92, BLACK), rect(48, 18, 124, 56, NAVY, GOLD, 2), text(110, 44, "STUMP’D", 17, WHITE, 800, anchor="middle"), text(110, 62, "OFFICIAL LOGO", 8, GOLD, 700, anchor="middle")]
    for x, label in zip((530, 650, 770, 885), ("WHAT WE DO", "WHO IT’S FOR", "PATHWAY", "ABOUT")):
        out.append(text(x, 54, label, 12, CREAM, 700))
    out += [text(1005, 54, "MEMBER LOG IN", 11, CREAM, 700), rect(1175, 23, 205, 47, GOLD, radius=2), text(1277, 53, "BOOK A CALL  →", 13, NAVY, 800, anchor="middle")]

    out += [text(72, 158, "MENTAL STRENGTH THROUGH CRICKET", 13, GOLD, 800), multiline(72, 255, ["Think Well.", "Play Better."], 90, WHITE, family="Georgia"), multiline(76, 500, ["Cricket is the training ground. Confidence, focus", "and resilience are the skills they take with them."], 24, CREAM, leading=1.45), rect(76, 615, 255, 56, GOLD), text(204, 650, "SEE HOW IT WORKS  ↓", 13, NAVY, 800, anchor="middle"), text(365, 650, "BOOK A PLANNING CALL", 13, GOLD, 800)]
    out += [rect(790, 130, 575, 620, "#211C18", GOLD), rect(810, 150, 535, 580, "#161C28"), multiline(835, 655, ["EXISTING STUMP’D", "PHOTOGRAPHY"], 18, GOLD, 800, 1.25)]

    out += [rect(0, 820, 1440, 500, CREAM), text(72, 895, "THE MOMENTS THAT MATTER", 13, RED, 800), multiline(72, 990, ["The game moves fast.", "The mind can learn to reset."], 58, RED, family="Georgia"), multiline(780, 1000, ["Mistake. Pressure. Frustration.", "A decision that did not go your way.", "", "Recognise it. Reset. Choose what’s next."], 22, NAVY, 500, 1.45)]

    out += [text(72, 1405, "A SIMPLE IDEA THAT TRAVELS", 13, WHITE, 800), text(72, 1515, "Next Ball.", 74, GOLD, family="Georgia"), multiline(74, 1585, ["You cannot change what just happened.", "You can influence what you do next."], 24, CREAM, 500, 1.5), rect(800, 1390, 2, 340, RED), multiline(855, 1480, ["Step back.", "Take a breath.", "NEXT BALL."], 49, WHITE, 700, 1.3, "Georgia")]

    out += [rect(0, 1800, 1440, 430, BLACK), text(72, 1875, "ONE SHARED LANGUAGE", 13, GOLD, 800), text(72, 1975, "The Stump’d 5.", 62, GOLD, family="Georgia")]
    for i, label in enumerate(("Think.", "Reset.", "Focus.", "Communicate.", "Lead.")):
        x = 72 + i * 260
        out += [text(x, 2070, f"0{i+1}", 11, GOLD, 800), text(x, 2140, label, 25, WHITE, family="Georgia")]

    out += [rect(0, 2230, 1440, 890, WHITE), text(72, 2310, "FIND YOUR STARTING POINT", 13, RED, 800), multiline(72, 2415, ["Built for the whole", "cricket community."], 60, RED, family="Georgia")]
    cards = ((72, 2600, "01", "Schools.", "Programmes for confidence, focus and life beyond cricket."), (730, 2600, "02", "Clubs.", "A shared language for pressure, communication and performance."), (72, 2845, "03", "Players.", "Individual tools for the moments that challenge how you play."), (730, 2845, "04", "Parents.", "Understand the language and support the player behind the performance."))
    for x, y, no, heading, body in cards:
        out += [rect(x, y, 638, 215, WHITE, RED), text(x+28, y+36, no, 11, RED, 800), text(x+28, y+91, heading, 34, RED, family="Georgia"), text(x+28, y+132, body, 15, NAVY, 500), text(x+28, y+181, "EXPLORE  →", 12, RED, 800)]

    out += [text(72, 3210, "A PATHWAY THAT GROWS WITH THEM", 13, GOLD, 800), text(72, 3300, "Spark to Core.", 61, GOLD, family="Georgia")]
    for i, (age, heading, detail) in enumerate((("YEARS 5–6 · AGES 9–11", "Spark", "Confidence · Emotions · Teamwork"), ("AGES 11–13", "Foundation", "Confidence · Emotions · Resilience"), ("AGES 14–17", "Core", "Pressure · Performance · Responsibility"))):
        y = 3385 + i * 120
        out += [rect(72, y, 1296, 1, "#6D4A26"), text(74, y+50, age, 12, CREAM, 700), text(485, y+57, heading, 38, GOLD, family="Georgia"), text(940, y+50, detail, 14, CREAM, 500)]
    out += [rect(0, 3820, 1440, 230, RED), text(720, 3885, "WHAT HAPPENS NEXT", 12, WHITE, 800, anchor="middle"), text(720, 3960, "Ready to start the conversation?", 43, WHITE, family="Georgia", anchor="middle"), rect(585, 3985, 270, 48, GOLD), text(720, 4016, "BOOK A PLANNING CALL  →", 12, NAVY, 800, anchor="middle"), "</svg>"]
    return "".join(out)


def mobile():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="390" height="4200" viewBox="0 0 390 4200">', rect(0, 0, 390, 4200, NAVY), rect(0, 0, 390, 70, BLACK), rect(18, 12, 90, 46, NAVY, GOLD), text(63, 39, "STUMP’D", 12, WHITE, 800, anchor="middle"), rect(296, 16, 76, 38, NAVY, GOLD), text(334, 40, "MENU", 11, CREAM, 800, anchor="middle")]
    out += [text(20, 118, "MENTAL STRENGTH THROUGH CRICKET", 10, GOLD, 800), multiline(20, 190, ["Think Well.", "Play Better."], 49, WHITE, family="Georgia"), multiline(20, 330, ["Cricket is the training ground.", "Confidence, focus and resilience", "are the skills they take with them."], 17, CREAM, 500, 1.45), rect(20, 455, 220, 50, GOLD), text(130, 486, "SEE HOW IT WORKS  ↓", 11, NAVY, 800, anchor="middle"), rect(20, 545, 350, 330, "#161C28", GOLD), multiline(38, 820, ["EXISTING STUMP’D", "PHOTOGRAPHY"], 14, GOLD, 800, 1.25)]
    out += [rect(0, 920, 390, 510, CREAM), text(20, 974, "THE MOMENTS THAT MATTER", 10, RED, 800), multiline(20, 1040, ["The game", "moves fast."], 43, RED, family="Georgia"), multiline(20, 1175, ["The mind can learn", "to reset."], 29, NAVY, 700, 1.2, "Georgia"), multiline(20, 1280, ["Mistake. Pressure. Frustration.", "Recognise it. Reset.", "Choose what’s next."], 17, NAVY, 500, 1.5)]
    out += [text(20, 1490, "A SIMPLE IDEA THAT TRAVELS", 10, WHITE, 800), text(20, 1570, "Next Ball.", 51, GOLD, family="Georgia"), multiline(20, 1635, ["You cannot change what just", "happened. You can influence", "what you do next."], 18, CREAM, 500, 1.4), rect(20, 1780, 350, 2, RED), multiline(20, 1845, ["Step back.", "Take a breath.", "NEXT BALL."], 35, WHITE, 700, 1.3, "Georgia")]
    out += [rect(0, 2050, 390, 590, BLACK), text(20, 2105, "ONE SHARED LANGUAGE", 10, GOLD, 800), text(20, 2170, "The Stump’d 5.", 39, GOLD, family="Georgia")]
    for i, label in enumerate(("Think.", "Reset.", "Focus.", "Communicate.", "Lead.")):
        y = 2250 + i * 70
        out += [text(22, y, f"0{i+1}", 10, GOLD, 800), text(78, y, label, 24, WHITE, family="Georgia"), rect(20, y+22, 350, 1, "#372B1F")]
    out += [rect(0, 2640, 390, 1110, WHITE), text(20, 2695, "FIND YOUR STARTING POINT", 10, RED, 800), multiline(20, 2760, ["Built for the whole", "cricket community."], 38, RED, family="Georgia")]
    for i, (heading, body) in enumerate((("Schools.", "Practical programmes for school and life."), ("Clubs.", "A shared language for pressure and performance."), ("Players.", "Individual tools for challenging moments."), ("Parents.", "Support the player behind the performance."))):
        y = 2900 + i * 190
        out += [rect(20, y, 350, 165, WHITE, RED), text(40, y+55, heading, 30, RED, family="Georgia"), text(40, y+93, body, 13, NAVY, 500), text(40, y+138, "EXPLORE  →", 10, RED, 800)]
    out += [text(20, 3810, "A PATHWAY THAT GROWS", 10, GOLD, 800), text(20, 3870, "Spark to Core.", 38, GOLD, family="Georgia")]
    for i, (heading, age) in enumerate((("Spark", "9–11"), ("Foundation", "11–13"), ("Core", "14–17"))):
        y = 3940 + i * 66
        out += [rect(20, y, 350, 1, "#6D4A26"), text(22, y+42, heading, 24, GOLD, family="Georgia"), text(350, y+40, age, 12, CREAM, 700, anchor="end")]
    out += ["</svg>"]
    return "".join(out)


HERE = Path(__file__).parent
(HERE / "homepage-desktop.svg").write_text(desktop())
(HERE / "homepage-mobile.svg").write_text(mobile())
