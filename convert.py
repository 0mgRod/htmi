import sys
import os
from PIL import Image
from tkinter import Tk, filedialog


def convert_image_to_html(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Get image dimensions
    width, height = image.size

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

        html_content += '</tr>\n'

    # Complete the HTML content
    html_content += '</table>\n'
    html_content += '</body>\n'
    html_content += '</html>'

    # Write the HTML content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(html_content)


if __name__ == '__main__':
    # Get the absolute paths of the files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_file = filedialog.askopenfilename(title="Select image file", filetypes=[("PNG Image", "*.png"),("JPEG Image", "*.jpg")])
    if not os.path.isabs(image_file):
        image_file = os.path.join(current_dir, image_file)

    html_file = os.path.join(current_dir, 'output.html')

    # Convert image to HTML
    convert_image_to_html(image_file, html_file)

    print(f"HTML file generated: {html_file}")
