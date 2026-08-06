import os
from PIL import Image, ImageDraw

def clean_watermarks_by_overlay(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Loop through all files in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    
                    # This script is designed for the original 1280x720 images.
                    # If the images have already been cropped, this script will notify the user.
                    if width == 1280 and height == 720:
                        # Create a copy to edit
                        cleaned_img = img.copy()
                        draw = ImageDraw.Draw(cleaned_img)
                        
                        # Sample the background color from a nearby area in the bottom margin (e.g. at x=1050, y=685)
                        # to ensure the overlay blends in perfectly with the grid/blueprint background
                        bg_color = img.getpixel((1050, 685))
                        
                        # Draw a solid rectangle over the NotebookLM watermark in the bottom right corner.
                        # Watermark is within x=1120 to x=1270, y=660 to y=707.
                        # We cover x=1100 to x=1275, y=655 to y=712.
                        draw.rectangle([1100, 655, 1275, 712], fill=bg_color)
                        
                        cleaned_img.save(filepath, quality=95)
                        print(f"Successfully removed watermark from: {filename} (Overlay applied, kept 1280x720 size)")
                    elif width == 1280 and height == 650:
                        print(f"Skipping {filename}: Already cropped to 1280x650. Please restore the original 1280x720 file first.")
                    else:
                        print(f"Skipping {filename}: non-standard dimensions ({width}x{height})")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    target_dir = "Slide/nb_imges"
    print(f"Starting non-destructive watermark overlay clean-up in: {target_dir}")
    clean_watermarks_by_overlay(target_dir)
    print("Clean-up completed.")
