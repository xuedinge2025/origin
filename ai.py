import tkinter as tk
import random
import colorsys
import math

def random_pastel_hex():
    h = random.random()
    l = 0.85
    s = 0.45
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))

def heart_points(n):
    for i in range(n):
        t = math.pi * 2 * i / n
        x = 16 * (math.sin(t) ** 3)
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )
        yield (x, y)

MESSAGES = [
    "保持微笑状态", "天冷了，多穿衣服", "多喝水哦~", "保持好心情", "期待下一次见面", "愿所有烦恼都消失",
    "我想你了", "早点睡别熬夜", "好好爱自己", "顺顺利利", "今天过得开心嘛", "每天都要开心", "不许哭",
]

def main():
    root = tk.Tk()
    root.withdraw()

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    START_MESSAGE = ""
    START_BUTTON_TEXT = "好"
    def show_intro(message: str, button_text: str):
        intro = tk.Toplevel(root)
        intro.title("温馨提示")
        w, h = 360, 180
        x = (screen_w - w) // 2
        y = (screen_h - h) // 2
        intro.geometry(f"{w}x{h}+{x}+{y}")
        intro.resizable(False, False)
        intro.attributes("-topmost", True)
        lbl = tk.Label(intro, text=message, font=("Microsoft YaHei", 16, "bold"))
        lbl.pack(expand=True, fill="both")

        btn = tk.Button(
            intro,
            text=button_text,
            font=("Microsoft YaHei", 12, "bold"),
            command=intro.destroy,
            width=12,
            bg="#A7D3FF",
            fg="white",
            activebackground="#86C5FF",
            activeforeground="white",
        )
        btn.pack(pady=10)
        intro.protocol("WM_DELETE_WINDOW", intro.destroy)
        intro.focus_force()
        intro.grab_set()
        root.wait_window(intro)

    show_intro(START_MESSAGE, START_BUTTON_TEXT)

    win_w, win_h = 300, 120
    count = 38
    POP_INTERVAL_MS = 80
    MARGIN = 8
    EXPLODE_POP_INTERVAL_MS = 40  
    EXPLODE_COUNT = 110 

    scale_x = (screen_w - win_w - 60) / (16 * 2)
    scale_y = (screen_h - win_h - 120) / (17 + 13)
    scale = max(10, min(scale_x, scale_y))

    center_x = screen_w // 2
    center_y = screen_h // 2 - 120

    windows = []

    def create_tip(x, y, color, text):
        top = tk.Toplevel(root)
        top.title("温馨提示")
        top.geometry(f"{win_w}x{win_h}+{x}+{y}")
        top.configure(bg=color)
        top.resizable(False, False)
        top.attributes("-topmost", True)
        tk.Label(top, text=text, bg=color, fg="#333333", font=("Microsoft YaHei", 16, "bold")).pack(expand=True, fill="both")
        return top

    def jitter(n=14):
        return random.randint(-n, n)

    points = list(heart_points(count))
    min_idx = min(range(len(points)), key=lambda i: points[i][1])
    points = points[min_idx:] + points[:min_idx]
    for idx, (hx, hy) in enumerate(points):
        px = int(center_x + hx * scale - win_w / 2 + jitter(22))
        py = int(center_y - hy * scale - win_h / 2 + jitter(18))

        px = max(MARGIN, min(px, screen_w - win_w - MARGIN))
        py = max(MARGIN, min(py, screen_h - win_h - MARGIN))

        color = random_pastel_hex()
        text = random.choice(MESSAGES)

        top = create_tip(px, py, color, text)

        top.withdraw()
        root.after(idx * POP_INTERVAL_MS, top.deiconify)

        windows.append({"win": top, "x": px, "y": py})

    gather_x = center_x - win_w // 2
    gather_y = center_y - win_h // 2
    COVERAGE = 0.9
    MAX_TILES = 600

    def lerp(a, b, t):
        return a + (b - a) * t

    def animate_gather(step=0, steps=24):
        t = step / float(steps)
        for item in windows:
            w = item["win"]
            x0, y0 = item["x"], item["y"]
            x = int(lerp(x0, gather_x, t))
            y = int(lerp(y0, gather_y, t))
            w.geometry(f"{win_w}x{win_h}+{x}+{y}")
        if step < steps:
            root.after(30, animate_gather, step + 1, steps)
        else:
            root.after(200, start_explode)

    def start_explode():
        cols = max(1, screen_w // win_w)
        rows = max(1, screen_h // win_h)
        total_cells = cols * rows
        if EXPLODE_COUNT and EXPLODE_COUNT > 0:
            target_tiles = min(MAX_TILES, EXPLODE_COUNT)
        else:
            target_tiles = int(min(MAX_TILES, max(count, int(total_cells * COVERAGE))))

        CHAOS_SPREAD = 0.65

        def generate_positions(n):
            positions = []
            base_dx = win_w * CHAOS_SPREAD
            base_dy = win_h * CHAOS_SPREAD * 0.8
            attempts = 0
            max_attempts = n * 120
            while len(positions) < n and attempts < max_attempts:
                x = random.randint(MARGIN, screen_w - win_w - MARGIN)
                y = random.randint(MARGIN, screen_h - win_h - MARGIN)
                ok = True
                for (px, py) in positions:
                    cx1, cy1 = px + win_w / 2, py + win_h / 2
                    cx2, cy2 = x + win_w / 2, y + win_h / 2
                    dx = abs(cx1 - cx2)
                    dy = abs(cy1 - cy2)
                    thx = random.uniform(base_dx * 0.6, base_dx * 1.2)
                    thy = random.uniform(base_dy * 0.6, base_dy * 1.2)
                    if dx < thx and dy < thy:
                        ok = False
                        break
                if ok:
                    positions.append((x, y))
                attempts += 1
            while len(positions) < n:
                positions.append(
                    (
                        random.randint(MARGIN, screen_w - win_w - MARGIN),
                        random.randint(MARGIN, screen_h - win_h - MARGIN),
                    )
                )
            return positions

        scatter_positions = generate_positions(target_tiles)

        for item in windows:
            try:
                item["win"].destroy()
            except:
                pass
        windows.clear()

        for idx in range(target_tiles):
            tx, ty = scatter_positions[idx]
            color = random_pastel_hex()
            text = random.choice(MESSAGES)
            top = create_tip(tx, ty, color, text)
            top.withdraw()
            root.after(idx * EXPLODE_POP_INTERVAL_MS, top.deiconify)
            windows.append({"win": top, "x": tx, "y": ty})

    total_show_ms = count * POP_INTERVAL_MS + 600
    root.after(total_show_ms, animate_gather)

    def close_all(event=None):
        for item in windows:
            try:
                w = item["win"] if isinstance(item, dict) else item
                w.destroy()
            except:
                pass
        root.destroy()

    root.bind("<Escape>", close_all)

    root.mainloop()

if __name__ == "__main__":
    main()