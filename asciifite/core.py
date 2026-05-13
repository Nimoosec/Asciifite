import cv2
import numpy as np

class asciifite:
    def __init__(self, charset="standard"):
        char_presets = {
            "standard": "@%#*+=-:. ",
            "complex": r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. ",
            "blocks": "█▓▒░ "
        }
        self.charset = char_presets.get(charset, charset)
        self.chars = np.array(list(self.charset))

    def frame_to_ascii_data(self, frame, width=120):
        h, w = frame.shape[:2]
        aspect_ratio = h / w
        target_h = int(width * aspect_ratio * 0.5) # Font aspect correction[cite: 4]
        
        # Resize and grayscale for fast mapping[cite: 4]
        small = cv2.resize(frame, (width, target_h))
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        
        # Vectorized mapping of pixels to characters[cite: 4]
        num_chars = len(self.chars)
        idx = (gray.astype(float) / 255 * (num_chars - 1)).astype(int)
        return self.chars[idx], small

class BannerGenerator:
    def __init__(self):
        # 5-row ASCII font map for the full alphabet and symbols
        self.font_map = {
            'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
            'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
            'C': [" CCCC", "C    ", "C    ", "C    ", " CCCC"],
            'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
            'E': ["EEEEE", "E    ", "EEEE ", "E    ", "EEEEE"],
            'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
            'G': [" GGGG", "G    ", "G  GG", "G   G", " GGGG"],
            'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
            'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
            'J': [" JJJJ", "    J", "    J", "J   J", " JJJ "],
            'K': ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
            'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
            'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
            'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
            'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
            'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
            'Q': [" QOO ", "O   O", "O   O", "O  OO", " OOOQ"],
            'R': ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
            'S': [" SSSS", "S    ", " SSS ", "    S", "SSSS "],
            'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
            'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
            'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
            'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
            'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
            'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
            'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
            '0': [" 000 ", "0   0", "0   0", "0   0", " 000 "],
            '1': ["  1  ", " 11  ", "  1  ", "  1  ", " 111 "],
            ' ': ["     "] * 5,
            '!': ["  !  ", "  !  ", "  !  ", "     ", "  !  "],
            '?': [" ??? ", "    ?", "  ?? ", "     ", "  ?  "],
        }
        
    def generate(self, text, style='solid', frame=True):
        text = text.upper()
        brush = {"solid": "█", "thin": "┃", "dotted": "░"}.get(style, style)
        
        rows = ["", "", "", "", ""]
        for char in text:
            # Get data or default to a blank space if char not found
            char_data = self.font_map.get(char, self.font_map[' '])
            
            for i in range(5):
                # Replace any non-space character with the brush
                line = "".join([brush if c != ' ' else ' ' for c in char_data[i]])
                rows[i] += line + "  " # Added 2 spaces between letters

        if not frame:
            return "\n".join(rows)

        # Content width is the length of the first row (minus trailing spaces)
        content_width = len(rows[0].rstrip())
        border = "═" * (content_width + 4)
        
        output = [f"╔{border}╗"]
        for r in rows:
            # Pad each row to match the full width within the frame
            row_content = r.rstrip().ljust(content_width)
            output.append(f"║  {row_content}  ║")
        output.append(f"╚{border}╝")
        
        return "\n".join(output)