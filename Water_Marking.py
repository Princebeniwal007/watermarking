from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_path, output_path, text, opacity=128,color=(255,255,255)):
    try:
        
        base_image = Image.open(input_path).convert("RGBA")
        
        
        watermark = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)
        
        
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            try:
                font = ImageFont.truetype("arialbd.ttf", 40)
            except:
                font = ImageFont.load_default().font_variant(size=40)
        
        
        text_width = draw.textlength(text, font=font)
        text_height = 40  
        x = (base_image.width - text_width) // 2
        y = (base_image.height - text_height) // 2
        
        rgba_color = (*color, opacity)  # 
        draw.text((x, y), text, font=font, fill=rgba_color)
        
        
        watermarked = Image.alpha_composite(base_image, watermark)
        
        
        if output_path.lower().endswith('.png'):
            watermarked.save(output_path)
        else:
            watermarked.convert("RGB").save(output_path)
            
        print(f"Success! Watermarked image saved to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


if __name__ == "__main__":
    input_img = input("Enter the image path: ")
    output_img = "watermarked.jpg"
    watermark_text = input("Enter the Watermark text: ")
    
    colors = {
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "black": (0, 0, 0)
    }
    str=input("Enter the color(white,red,green,blue,black,yellow): ")
    
    if not os.path.exists(input_img):
        print(f"Error: Input image '{input_img}' not found!")
    else:
        add_watermark(input_img, output_img, watermark_text,opacity=128,color=colors[str])