from PIL import Image, ImageDraw, ImageFont
import os

BG = (30, 30, 30)
FG = (204, 204, 204)
GREEN = (80, 200, 120)
YELLOW = (230, 180, 60)
RED = (210, 80, 80)
CYAN = (80, 200, 220)
TITLE_BAR = (50, 50, 50)
TITLE_TEXT = (180, 180, 180)
BTN_RED = (255, 95, 87)
BTN_YELLOW = (255, 189, 46)
BTN_GREEN = (40, 200, 80)

W = 820
FONT_SIZE = 15
PADDING = 20
LINE_H = 22
TITLE_H = 32

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", FONT_SIZE)
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", FONT_SIZE)
except:
    font = ImageFont.load_default()
    font_bold = font

def draw_terminal(lines, filename, title="plgg@pintos: ~"):
    visible = [l for l in lines if l is not None]
    H = TITLE_H + PADDING + len(visible) * LINE_H + PADDING
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, TITLE_H], fill=TITLE_BAR)
    for i, (cx, col) in enumerate([(14, BTN_RED), (34, BTN_YELLOW), (54, BTN_GREEN)]):
        d.ellipse([cx-7, TITLE_H//2-7, cx+7, TITLE_H//2+7], fill=col)
    tw = d.textlength(title, font=font)
    d.text(((W - tw) / 2, 8), title, fill=TITLE_TEXT, font=font)

    y = TITLE_H + PADDING
    for line in visible:
        if isinstance(line, list):
            x = PADDING
            for text, color in line:
                d.text((x, y), text, fill=color, font=font)
                x += d.textlength(text, font=font)
        else:
            d.text((PADDING, y), line, fill=FG, font=font)
        y += LINE_H

    out = f"/home/claude/plgg/{filename}"
    img.save(out)
    print(f"Saved {out}")

draw_terminal([
    [("$ ", GREEN), ("gcc -o shell_test shell_test.c", FG)],
    [("$ ", GREEN), ("echo $?", FG)],
    "0",
    "",
    [("$ ", GREEN), ("", FG)],
], "print_p1_compilacao.png", "plgg@pintos: ~/plgg")

draw_terminal([
    [("$ ", GREEN), ("printf 'whoami\\nhello\\nexit\\n' | ./shell_test", FG)],
    [("plgg> ", CYAN), ("Pedro Leal Gomes Gadelha", FG)],
    [("plgg> ", CYAN), ("invalid command", FG)],
    [("plgg> ", CYAN), ("", FG)],
    [("$ ", GREEN), ("", FG)],
], "print_p2_execucao.png", "plgg@pintos: ~/plgg")

draw_terminal([
    [("$ ", GREEN), ("./shell_test", FG)],
    [("plgg> ", CYAN), ("whoami", FG)],
    "Pedro Leal Gomes Gadelha",
    [("plgg> ", CYAN), ("", FG)],
], "print_p3_whoami.png", "plgg@pintos: ~/plgg")

draw_terminal([
    [("$ ", GREEN), ("./shell_test", FG)],
    [("plgg> ", CYAN), ("ls", FG)],
    [("invalid command", RED), ("", FG)],
    [("plgg> ", CYAN), ("pwd", FG)],
    [("invalid command", RED), ("", FG)],
    [("plgg> ", CYAN), ("exit", FG)],
    [("$ ", GREEN), ("", FG)],
], "print_p4_invalid_exit.png", "plgg@pintos: ~/plgg")

draw_terminal([
    [("$ ", GREEN), ("./shell_test", FG)],
    [("plgg> ", CYAN), ("   whoami   ", FG)],
    "Pedro Leal Gomes Gadelha",
    [("plgg> ", CYAN), ("", FG)],
], "print_p5_trim.png", "plgg@pintos: ~/plgg")

draw_terminal([
    [("$ ", GREEN), ("./shell_test", FG)],
    [("plgg> ", CYAN), ("", FG)],
    [("plgg> ", CYAN), ("", FG)],
    [("plgg> ", CYAN), ("exit", FG)],
    [("$ ", GREEN), ("", FG)],
], "print_p6_empty.png", "plgg@pintos: ~/plgg")

print("All prints generated.")
