# PyAztec
A Python library for reading and generating Aztec codes.

# Usage
## Prerequisites

OpenCV

## Code Examples

```
code example
```

# Roadmap
## Currently In-Progress

* Write documentation about Aztec Code for possible contributors (only decoding for now)
* Decode some Aztec codes by hand as test-cases and for documentation purposes
* Structure the library according to best practices (documentation/tests/folder structure/necessary files)
* Finish steps **2 to 4** of the decoding process (probably the most important use-case)

## Things for the Future

* Write a Reed-Solomon Code module for error handling
* Start the draft for the encoding process

## Decoding Process Draft
The decoding process is split into four steps, the beginning of every step should be part of the public interface of the library. The four steps are:

1. Scan an input image for the bulls-eye pattern and determine whether it is a compact or full Aztec code. Then decode the mode message to get the number of layers and number of datawords. From the number of layers extrapolate the boundaries of the Aztec code. Finally transform the image to square (e.g. by perspective transform, rotation, cropping).
  * Takes **input image**
  * Gives **transformed image, size of bulls-eye pattern/type of Aztec code (compact or full), number of layers, number of datawords**
2. Convert a cropped/quadratic image of the Aztec code to a 2-dimensional array of bits.
  * Takes **transformed image, size of bulls-eye pattern/type of Aztec code (compact or full), number of layers, numbers of datawords (optional)**
  * Gives **2-dimensional array of bits**
3. Order the bits of the Aztec code into a linearly ordered bitstring that can be read by the finite state machine of **step 4**. During this process any stuffed bits need to be removed.
  * Takes **2-dimensional array of bits**
  * Gives **bitstring for data/padding/Reed-Solomon codewords, bitstring for mode-message**
4. Parse the mode-message. Finally decode the bitstring of data, padding, and error-correction codewords (Reed-Solomon) by using a finite state machine.
  * Takes **bitstring for data/padding/reed-solomon codewords, bitstring for mode-message**
  * Gives **decoded string**

## Encoding Process Draft

# About the Aztec Code
[General Information](/about_aztec/general)
[Decoding](/about_aztec/decoding)
[Encoding](/about_aztec/encoding)