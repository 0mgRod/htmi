import sys
import os
from PIL import Image
from tkinter import Tk, filedialog
from tqdm import tqdm
import gzip


def convert_image_to_html(image_path, output_path, scale_factor, compress):
    # Open the image
    image = Image.open(image_path)

    # Get image dimensions
    width, height = image.size

    # Adjust the dimensions based on the scale factor
    if scale_factor != 1:
        width = int(width / scale_factor)
        height = int(height / scale_factor)
        image = image.resize((width, height))

    # Start building the HTML content
    html_content = '<!DOCTYPE html>\n'
    html_content += '<html>\n'
    html_content += '<head>\n'
    html_content += '<style>\n'
    html_content += 'table { border-collapse: collapse; }\n'
    html_content += 'td { padding: 0; border: none; width: 1px; height: 1px; }\n'
    html_content += '</style>\n'
    html_content += '</head>\n'
    html_content += '<body>\n'
    html_content += '<table>\n'

    # Iterate over each pixel in the image
    progress = tqdm(total=width * height, desc='Converting Image', unit='pixel')
    for y in range(height):
        html_content += '<tr>\n'
        for x in range(width):
            # Get the RGB values of the pixel
            pixel = image.getpixel((x, y))
            r, g, b = pixel[:3]

            # Convert RGB to hexadecimal color
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)

            # Add the pixel as a table cell with the corresponding color
            html_content += '<td class="pixel" style="background-color: {}; width: 1px; height: 1px;"></td>\n'.format(
                hex_color)

            progress.update(1)  # Update progress bar

    progress.close()

    # Complete the HTML content
    html_content += '</table>\n'
    html_content += '</body>\n'
    html_content += '</html>'

    # Write the HTML content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(html_content)

    # Compress the output file with gzip if requested
    if compress:
        compressed_path = output_path + '.gz'
        with open(output_path, 'rb') as input_file, gzip.open(compressed_path, 'wb') as output_file:
            output_file.writelines(input_file)
        os.remove(output_path)  # Remove the uncompressed file
        return compressed_path
    else:
        return output_path


if __name__ == '__main__':
    # Get the absolute paths of the files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_file = filedialog.askopenfilename(title="Select image file",
                                            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg")])
    if not os.path.isabs(image_file):
        image_file = os.path.join(current_dir, image_file)

    html_file = os.path.join(current_dir, 'output.html')

    # Ask for the scale factor
    scale_factor_str = input("Enter the scale factor (type 1 for same size, 2 for 2x smaller etc): ")
    if scale_factor_str.strip():
        scale_factor = float(scale_factor_str)
    else:
        scale_factor = 1

    # Ask if gzip compression should be applied
    compress_str = input("Compress with gzip? (y/n): ")
    compress = compress_str.lower() == 'y' if compress_str.strip() else False

    # Convert image to HTML
    output_file = convert_image_to_html(image_file, html_file, scale_factor, compress)

    print(f"HTML file generated: {output_file}")
