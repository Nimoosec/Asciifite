# asciifite 🎨

**asciifite** is a high-performance Python library for converting images and videos into colorful ASCII art and generating creative text banners for CLI applications. 

By leveraging **NumPy vectorized operations**, this library ensures that frame-by-frame conversion is significantly faster than standard Python loops.

---

## 🚀 Features
* **Video-to-ASCII**: Convert standard video files (.mp4, .avi, etc.) into colorful ASCII-style videos.
* **Image-to-ASCII**: Transform any digital image into a detailed, textured ASCII rendering.
* **Creative Banners**: Generate stylized, framed text banners using multiple "brush" styles (solid, thin, dotted).
* **Aspect Correction**: Automatically adjusts character density to maintain the original visual proportions.

---

## 📦 Installation

Ensure you have Python installed, then navigate to the project root folder and install via pip:

    pip install asciifite

### 🛠 Dependencies
The library relies on the following industry-standard packages:
* **opencv-python**: For media decoding and rendering.
* **numpy**: For high-speed image matrix processing.

---

## 📖 Usage Guide & Examples

### 1. Generating Creative Banners
Use the BannerGenerator class to create stylized headers.

    from asciifite import BannerGenerator
    bg = BannerGenerator()
    banner = bg.generate("ABC", style="solid", frame=True)
    print(banner)

### 2. Converting Videos to ASCII
The process_video function handles reading frames, conversion, and writing the final video.

    from asciifite import process_video
    process_video(
        input_path="input.mp4", 
        output_path="output.mp4", 
        width=120, 
        cell_size=8
    )

### 3. Converting Images
Turn any photo into an ASCII masterpiece with process_image.

    from asciifite import process_image
    process_image(
        input_path="photo.jpg", 
        output_path="ascii.jpg", 
        width=150, 
        cell_size=10
    )

---

## ⚙️ Configuration Options
* **width**: Number of ASCII characters across the output.
* **cell_size**: The pixel dimensions of each character block.
* **charset**: Choose between 'standard', 'complex', or 'blocks'.

---

## 📂 Project Structure
    asciifite_project/
    ├── asciifite/            
    │   ├── __init__.py     
    │   ├── core.py         
    │   └── io.py           
    ├── setup.py            
    └── README.md
