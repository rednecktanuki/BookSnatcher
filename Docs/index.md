# BookSnatcher: Automated Book Downloader

**Description:**  
BookSnatcher is a tool that automates capturing pages from online books in your browser and compiles them into a PDF. It works great for Google Books and other browser-based readers.

---

## Table of Contents
1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
   - [1. Prepare Your Files](#1-prepare-your-files)
   - [2. Install Python](#2-install-python)
   - [3. Install OBS Studio](#3-install-obs-studio)
   - [4. Install Python Libraries](#4-install-python-libraries)
   - [5. Run BookSnatcher](#5-run-booksnatcher)
   - [6. Tips](#6-tips)

---

## Requirements

- Notepad  
- Python 3 for Windows  
- OBS Studio  
- Dual monitors (recommended but optional)  

---

## Setup Instructions

### 1. Prepare Your Files
1. Drag and drop `booksnatcher.py` onto your Desktop.  
2. Create an empty folder on your Desktop called: "snatchedbooks"
*(without quotation marks)*  

---

### 2. Install Python
1. Download Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. During installation, **check “Add Python to PATH”**.  
3. Verify installation:  
   1. Press `Win + R`, type `cmd`, and press Enter.  
   2. In CMD, type: py --version
You Should see the version of python.


### 3. Install OBS Studio


1. Download OBS Studio: https://obsproject.com/
2. Install OBS. 
4. If using dual monitors: Keep the book on one monitor in full-screen. & Use the second monitor for OBS controls.

### 4. Install Python Libraries
1. Open CMD
2. cd Desktop\BookSnatcher
3. pip install -r requirements.txt

### 5. Run BookSnatcher
1. close and reopen CMD
2. cd Desktop
3. py booksnatcher.py
4. Follow on-screen instructions
5.Open OBS, set it to copy window and right click > fullscreen projection > (choose your monitor)
6.Move your mouse to select the top-left corner of the area to capture and
Move your mouse to select the bottom-right corner of the monitor mirroring on OBS (think of it as clicking and dragging a screenshot but you just point) (to avoid black screens from protection)
7. the mouse MUST be on the screen of the real book so it can scroll down. have the online book set to: vertical scroll: OFF > Zoom: Fit to screen > Page layout: One page layout (for google book reader this is the sweet spot but it it needs to be a similar layout with non vertical and one page layout)
8. Let the script scroll automatically and take screenshots after setting guide for screenshots.
. When finished, press Ctrl + C to stop.
. All screenshots will be compiled into a PDF in the snatchedbooks folder.

### 6. Tips
1. maximize the book on your larger better screen for best resolution.
2. Adjust the scroll amount in the script if pages overlap or content is cut off.
3. you MUST set the cursors to screenshot the window in the OBS screen.







