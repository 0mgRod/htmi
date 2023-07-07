# Image to HTML Converter and Viewer

This project consists of two Python scripts that allow you to convert an image file (PNG or JPEG) to an HTML file, where each pixel of the image is represented as a table cell with corresponding colors. It also provides a PyQt5-based viewer to display the generated HTML file.

## Prerequisites

- Python 3.x
- Required Python packages: `Pillow`, `PyQt5`, `tkinter`

You can install the required packages using pip:

```bash
pip install pillow PyQt5
```

## Usage
### Step 1: Convert Image to HTML
1. Run the `convert.py` script using the following command:
```bash
python convert.py
```
2. Enter the path of the image file you want to convert when prompted.
3. The script will generate an HTML file named output.html in the same directory as the script, representing the image in HTML format.

### Step 2: View HTML as Image
1. Run the `viewimg.py` script using the following command:

```bash
python viewimg.py
```

2. Use the file dialog to select the output.html file generated in Step 1.

3. A PyQt5 window titled "HTML Viewer" will open, displaying the image rendered from the HTML file.

## Customization
- Image and HTML file names: You can modify the variables in the image_to_html.py script to specify the desired file names for the input image and output HTML file.

- Styling: The generated HTML file uses inline styling to set the background color of each table cell. You can modify the CSS styles in the image_to_html.py script to customize the appearance of the rendered image.

## Limitations
- Supported image formats: The scripts support PNG and JPEG image formats. Ensure that the image file you provide is in either of these formats.

- Large image files: The generated HTML file can become large in size for high-resolution or large-sized images, which may impact the rendering performance in the PyQt5 window.

## License
This project is licensed under the [MIT LICENSE](LICENSE).
