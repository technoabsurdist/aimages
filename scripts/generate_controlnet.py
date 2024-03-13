from PIL import Image, ImageDraw, ImageFont

# Function to generate the image
def generate_image(name):
    # Create a blank black image
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='black')
    
    # Create a drawing object
    draw = ImageDraw.Draw(img)
    
    # Use a built-in font
    font_size = 500
    font = ImageFont.load_default(70)
    
    # Calculate the text size
    text_length = draw.textlength(name, font, font_size=font_size)
    
    # Calculate the position for centering the text
    x = (width - text_length) / 2
    y = (height - text_length) / 2
    
    # Draw the text on the image
    draw.text((x, y), name, font=font, fill='white')
    
    # Save the image
    img.save(f'../control_nets/{"_".join(name.split(" "))}.png')
    print(f'Image saved as {name}.png')

# Get the name from the user
name = input("Enter a name: ")

# Generate the image
generate_image(name)