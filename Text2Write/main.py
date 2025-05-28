from PIL import Image, ImageDraw, ImageFont
import textwrap

# Step 1: Multi-line input with END as stop
print("Enter your paragraph (type 'END' to finish):")
lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

text = "\n".join(lines)

# Step 2: Create the image
width, height = 600,800
img = Image.new("RGB", (width, height), color="white")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("IndieFlower-Regular.ttf", 20)

# Step 3: Draw notebook lines
line_spacig = 30
start_y = 30
for y in range(start_y,height,line_spacig):
    draw.line([(40,y),(width - 40 ,y)], fill=(200,200,200), width=1)

# Step 4: Draw red margin line
draw.line([(70,40), (70, height - 40)], fill=(255,0,0), width=2)

# Step 5: wrap and draw text
wrapped_text = textwrap.wrap(text, width=40)
x, y = 70, 50
line_spacing = 30

for line in wrapped_text:
    draw.text((x, y), line, font=font, fill=(0, 0, 0))
    y += line_spacing

# Step 6: Save image
img.save("text.png")
print("✅ Handwritten image created: text.png")
