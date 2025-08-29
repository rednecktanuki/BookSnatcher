import mss
import mss.tools
import pyautogui
import time
import os
from PIL import Image  # added for PDF compilation

def main():
    # Startup message
    print("This script will help you capture scrolling screenshots of any book or document on your screen using MSS.")
    print("It will take a screenshot of the area you select, scroll down automatically, and repeat until you stop it manually (Ctrl+C).")
    print("Screenshots will be saved in a folder called 'snatchedbooks' on your Desktop.")
    print("\n(For your reading and snatching pleasure - SweetTeaKay)\n")

    input("Press ENTER to begin...")

    # Countdown for top-left corner
    print("\nMove your mouse to the TOP-LEFT corner of the area you want to capture. Countdown starting...")
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    x1, y1 = pyautogui.position()
    print(f"Top-left corner recorded at: ({x1}, {y1})")

    # Countdown for bottom-right corner
    print("\nNow move your mouse to the BOTTOM-RIGHT corner of the area you want to capture. Countdown starting...")
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    x2, y2 = pyautogui.position()
    print(f"Bottom-right corner recorded at: ({x2}, {y2})")

    # Calculate width and height
    width = x2 - x1
    height = y2 - y1

    # Set up save folder
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    save_folder = os.path.join(desktop, "snatchedbooks")
    os.makedirs(save_folder, exist_ok=True)

    print("\nStarting screenshot capture. Press Ctrl+C to stop.\n")

    count = 1
    with mss.mss() as sct:
        region = {"top": y1, "left": x1, "width": width, "height": height}
        try:
            while True:
                # Take screenshot of selected region
                filename = os.path.join(save_folder, f"screenshot_{count}.png")
                sct_img = sct.grab(region)
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)
                print(f"Saved {filename}")

                count += 1

                # Scroll down slightly
                pyautogui.scroll(-300) # adjust if scrolling too far or not enough
                time.sleep(3) # wait between screenshots

        except KeyboardInterrupt:
            print("\nStopped by user. All screenshots saved in 'snatchedbooks'.")

            # ------------------- PDF Compilation -------------------
            images = sorted([img for img in os.listdir(save_folder) if img.endswith(".png")])
            if not images:
                print("No images found to compile into PDF.")
            else:
                img_list = []
                for img_file in images:
                    img_path = os.path.join(save_folder, img_file)
                    img = Image.open(img_path).convert("RGB")
                    img_list.append(img)
                pdf_path = os.path.join(save_folder, "compiled_book.pdf")
                img_list[0].save(pdf_path, save_all=True, append_images=img_list[1:])
                print(f"PDF compiled successfully: {pdf_path}")

if __name__ == "__main__":
    main()
