# Executive Summary

**Chapter 19: Manipulating Images** introduces the **Pillow** module, a third-party Python library used to edit digital image files. Digital images are common in modern life, but editing thousands of them by hand using software like Photoshop is slow and expensive. This chapter teaches how to write programs that can automatically **crop, resize, rotate, and draw** on images. By the end of this chapter, students will be able to perform batch processing, such as adding a watermark logo to hundreds of photos in just a few seconds.

---

# Deep-Dive Content: Manipulating Images

## 1. Computer Image Fundamentals

To manipulate images, one must first understand how computers represent colors and locations.

### 1.1 Colors and RGBA Values

- **RGBA Definition**: Computers represent colors using four numbers: **Red, Green, Blue, and Alpha** (transparency).
- **Value Range**: Each component is an integer from **0** (none) to **255** (maximum).
- **Alpha Channel**: This value determines how much of the background you can "see through" a pixel. A value of 0 is fully transparent, while 255 is fully opaque.
- **Pillow Implementation**: In Pillow, these are represented as a **tuple** of four integers, such as `(255, 0, 0, 255)` for solid red.
- **Helpful Tool**: The `ImageColor.getcolor()` function allows you to use standard color names (like 'red' or 'chocolate') to get RGBA tuples.

### 1.2 Coordinates and Box Tuples

- **The Coordinate System**: Python uses x and y coordinates. The **origin (0,0)** is the top-left corner of the image.
- **Axis Movement**: The x-coordinate increases from left to right, while the **y-coordinate increases going down**.
- **Box Tuples**: Pillow functions often require a "box tuple" of four integers: **(Left, Top, Right, Bottom)**.
    - _Note_: The box includes the left and top pixels but goes up to (and does not include) the right and bottom pixels.

## 2. Working with the Pillow Module

Pillow is a powerful library that treats images as objects in Python code.

### 2.1 Opening and Saving Images

- **Loading**: Use `Image.open('filename.png')` to create an Image object.
- **Attributes**: Image objects have a `size` (width and height tuple), `filename`, and `format` (e.g., 'PNG' or 'JPEG').
- **Saving**: Use the `save()` method. Pillow automatically identifies the format based on the file extension you provide.

### 2.2 Manipulating Images

- **Cropping**: The `crop()` method takes a box tuple and returns a **new** Image object containing only the selected area.
- **Copying**: The `copy()` method returns a separate Image object so you can modify a copy without losing the original.
- **Pasting**: The `paste()` method puts one image on top of another at specific coordinates.
- **Resizing**: The `resize()` method takes a tuple of two integers (width, height) and returns a new resized image.
- **Rotating and Flipping**: The `rotate()` method rotates the image counterclockwise by a degree value. The `transpose()` method can flip an image horizontally or vertically.

### 2.3 Individual Pixel Control

- **Get/Put**: You can use `getpixel((x, y))` to see a pixel's color or `putpixel((x, y), (R, G, B, A))` to change it.
- **Example Code (Coloring half an image)**:
    
    ```
    from PIL import Image
    im = Image.new('RGBA', (100, 100))
    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210)) # Top half light gray
    ```
    

## 3. Drawing and Text

Pillow can create shapes and write text directly onto images using the `ImageDraw` and `ImageFont` modules.

### 3.1 The ImageDraw Module

- First, create an `ImageDraw` object by passing an image to `ImageDraw.Draw(im)`.
- **Shapes**: You can draw points, lines, rectangles, ellipses, and polygons.
- **Arguments**: These methods use the `fill` (inside color) and `outline` (border color) parameters.

### 3.2 Drawing Text

- The `text()` method requires a coordinate, a string, and an optional **font**.
- **Loading Fonts**: `ImageFont.truetype('arial.ttf', 32)` loads a specific font file and sets its size in points.
- **Sizing**: The `textsize()` method calculates the width and height of a string in a specific font before you draw it, helping you center it.

---

# ⚠️ Important Warnings & Notes

- **Installation Name**: When installing via pip, use `pillow`, but in your code, use `from PIL import Image`.
- **In-Place Modification**: The **`paste()`** method modifies the Image object **directly** (in place). It does not return a new object.
- **Memory Management**: Python's garbage collector will delete image data once variables are no longer used to free up computer memory.
- **Transparency Bug**: When using `paste()`, if the image has transparent pixels, you **must** pass the image itself as the third argument (a "mask") so the transparency copies correctly.
- **Coordinate Trap**: Remember that y-coordinates start at 0 at the top and increase as you go **down**.

---

# 📘 Vocabulary Table

|Word/Term|Simple English Definition|Arabic Translation|
|:--|:--|:--|
|**Opaque**|Not see-through; solid color.|معتم|
|**Pixel**|The smallest dot of color on a screen.|بكسل / عنصر صورة|
|**RGBA**|Red, Green, Blue, Alpha (transparency).|نظام الألوان الرباعي|
|**Crop**|To cut off the outside parts of an image.|قص / اجتزاء|
|**Transpose**|To flip or change the position of something.|قلب / تبديل الموضع|
|**Watermark**|A logo or text placed over an image for protection.|علامة مائية|
|**Coordinates**|Numbers that show a specific point on a map or screen.|إحداثيات|

---

# Key Takeaways

1. **Automation Advantage**: Programming allows for batch editing (like resizing 1,000 photos) which is free and faster than manual tools.
2. **Top-Left Origin**: All screen and image math in Python starts at (0,0) in the upper-left corner.
3. **Use `copy()` Often**: Because some methods modify the original object, always create a copy if you need to keep the original image unchanged.
4. **Drawing is Multi-Step**: To draw, you must first have an Image, then create a Draw object, then call shape methods.
5. **Font Location**: Python automatically searches for `.ttf` font files in your operating system's standard font folders.