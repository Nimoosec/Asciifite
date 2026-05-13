import cv2
import numpy as np
from .core import asciifite

def render_frame(char_map, color_data, cell_size=10):
    h, w = char_map.shape
    canvas = np.zeros((h * cell_size, w * cell_size, 3), dtype=np.uint8)
    
    for y in range(h):
        for x in range(w):
            char = char_map[y, x]
            color = [int(c) for c in color_data[y, x]]
            cv2.putText(canvas, char, 
                        (x * cell_size, y * cell_size + int(cell_size*0.8)),
                        cv2.FONT_HERSHEY_SIMPLEX, cell_size/32, color, 1)
    return canvas

def process_image(input_path, output_path, width=150, cell_size=10):
    engine = asciifite()
    img = cv2.imread(input_path)
    if img is None: return False
    
    chars, colors = engine.frame_to_ascii_data(img, width=width)
    result = render_frame(chars, colors, cell_size=cell_size)
    cv2.imwrite(output_path, result)
    return True

def process_video(input_path, output_path, width=100, cell_size=8):
    engine = asciifite()
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    
    ret, frame = cap.read()
    if not ret: return False
    
    chars, colors = engine.frame_to_ascii_data(frame, width=width)
    sample_render = render_frame(chars, colors, cell_size=cell_size)
    h_out, w_out = sample_render.shape[:2]
    
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w_out, h_out))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        chars, colors = engine.frame_to_ascii_data(frame, width=width)
        out.write(render_frame(chars, colors, cell_size=cell_size))
        
    cap.release()
    out.release()
    return True