# Steganography Detection using Python

A lightweight Python tool that detects whether an image is
**steganographically altered** or **safe**.

This code analyzes images and attempts to detect hidden data embedded
using common steganography techniques such as:

-   **LSB (Least Significant Bit) Steganography**
-   **J-UNIWARD**
-   **JMiPOD**
-   **UERD**

The script inspects image data and statistical patterns to identify
potential hidden payloads.

------------------------------------------------------------------------

# Overview

Steganography is a technique used to hide secret information inside
digital media such as images.

While it has legitimate uses, it is also commonly used in:

-   Malware communication
-   Data exfiltration
-   Covert messaging

This python file provides a **basic steganography detection code** that
can flag suspicious images by analyzing:

-   Bit-level patterns in RGB images
-   DCT coefficient variance in JPEG images
-   Extracted hidden text patterns

------------------------------------------------------------------------

# Features

-   Detects **LSB-based steganography in PNG images**
-   Detects **JPEG steganography artifacts**
-   Supports detection of algorithms such as:
    -   J-UNIWARD
    -   JMiPOD
    -   UERD
-   Includes **LSB encoding implementation** for testing
-   Simple **single-function image safety classification**

Output:

    Safe!

or

    Suspicious! Possible steganography detected
    
------------------------------------------------------------------------

# How the Detection Works

## 1. LSB Detection (PNG Images)

For non-JPEG images:

1.  The image is flattened into a pixel array.
2.  Least Significant Bits (LSBs) are extracted.
3.  Bits are converted into bytes.
4.  Bytes are interpreted as ASCII characters.
5.  If meaningful text patterns are detected, the image is flagged as
    **suspicious**.

Detection heuristic:

    [A-Za-z]{4,}

Meaning **4 or more consecutive alphabet characters**.

------------------------------------------------------------------------

## 2. JPEG Steganography Detection

For JPEG images the script performs:

1.  Convert image to grayscale
2.  Divide image into **8×8 blocks**
3.  Compute **DCT (Discrete Cosine Transform)**
4.  Analyze **mid-frequency coefficients**
5.  Calculate statistical variance

If variance exceeds a threshold:

    variance > 20

The image may contain steganographic artifacts from algorithms such as:

-   J-UNIWARD
-   JMiPOD
-   UERD

------------------------------------------------------------------------

## Create a Steganographic Image (LSB)

You can also generate an LSB stego image for testing.

``` python
encode("Hello World!", "image.png")
```

This will create:

    steg_img.png

------------------------------------------------------------------------

# Example

Input:

    Safe1-secret.png

Output:

    Suspicious! Might contain hidden embeddings

------------------------------------------------------------------------

# Limitations

This project is **not a full forensic steganalysis system**.

Limitations include:

-   Detection is heuristic-based
-   May produce **false positives**
-   May miss **highly sophisticated steganography**
-   Only basic statistical checks are implemented
-   Designed primarily for **educational and research purposes**

Professional steganalysis tools use:

-   Machine Learning
-   Rich Models
-   Deep Neural Networks


------------------------------------------------------------------------

# Author

Developed by **Shivam Mohite**
