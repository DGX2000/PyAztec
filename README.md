# PyAztec
A Python library for reading and generating Aztec codes.

# Usage

## Prerequisites

## Code Examples

# Roadmap
## Currently In-Progress

* Write documentation about Aztec Code for possible contributors
* Decode some Aztec codes by hand as test-cases and for documentation purposes
* Structure the library according to best practices (documentation/tests/folder structure/necessary files)

## Decoding
The decoding process is split into four steps, the beginning of every step should be part of the public interface of the library. The four steps are:

1. Scan an input image for the bulls-eye pattern and determine whether it is a compact or full Aztec code. Then decode the mode message to get the number of layers and number of datawords. From the number of layers extrapolate the boundaries of the Aztec code. Finally transform the image to square (e.g. by perspective transform, rotation, cropping).
  * Takes **input image**
  * Gives **transformed image, size of bulls-eye pattern/type of Aztec code (compact or full), number of layers, number of datawords**
2. Convert a cropped/quadratic image of the Aztec code to a 2-dimensional array of bits.
  * Takes **transformed image, size of bulls-eye pattern/type of Aztec code (compact or full), number of layers, numbers of datawords (optional)**
  * Gives **2-dimensional array of bits**
3. e
  * sdfdsf
4. f
  * sdfsdf

## Encoding

# About the Aztec Code