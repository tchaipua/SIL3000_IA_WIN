from PIL import Image, ImageDraw

def draw_circle_x():
    size = 128
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Desenha Círculo
    margin = 8
    width = 8
    draw.ellipse(
        [margin, margin, size - margin, size - margin], 
        outline="black", 
        width=width
    )
    
    # Desenha o X interno
    x_margin = 36
    draw.line(
        [x_margin, x_margin, size - x_margin, size - x_margin], 
        fill="black", 
        width=8
    )
    draw.line(
        [x_margin, size - x_margin, size - x_margin, x_margin], 
        fill="black", 
        width=8
    )
    
    img.save("btn_fechar.png")
    print("Ícone btn_fechar.png restaurado para círculo original")

draw_circle_x()
