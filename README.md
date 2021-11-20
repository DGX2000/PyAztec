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
## ToDo

- [X] documentation for the decoding process (./about_aztec)
- [X] decode some Aztec codes manually for test-cases and documentation
- [X] structure the package according to best practices (tests/init files)
- [X] write tests for **step 4** (manually decoded bitstrings)
- [X] implement **step 4** of decoding (without FLG(n)/Reed-Solomon/Mixed-Mode at the moment)
- [X] write tests for **step 2** (manually transcribed symbols)
- [X] implement **step 2** of decoding
- [X] write tests for **step 3** (manually read bitstrings)
- [X] implement **step 3** of decoding
- [ ] update readme (more description, instructions, decoding example)
- [ ] write documentation for the encoding process (Reed-Solomon and examples)
- [ ] add FLG(n)/Reed-Solomon/Mixed-Mode to **step 4** of decoding
- [ ] start draft for the encoding process
- [ ] implement encoding process
- [ ] update readme (encoding example)
- [ ] implement **step 1** of decoding
- [ ] update readme (final decoding example)

## Decoding Process Draft
The four steps are:

1. Scan an input image for the bulls-eye pattern and determine whether it is a compact or full Aztec code. Then decode the mode message to get the number of layers and number of datawords. From the number of layers extrapolate the boundaries of the Aztec code. Finally transform the image to square (e.g. by perspective transform, rotation, cropping).
  * Takes **input image**
  * Gives **transformed image, size of bulls-eye pattern/type of Aztec code (compact or full), number of layers, number of datawords**
2. Convert a cropped/quadratic image of the Aztec code to a 2-dimensional array of bits.
  * Takes **transformed image, size of bulls-eye pattern/type of Aztec code (compact or full), number of layers, numbers of datawords**
  * Gives **2-dimensional array of bits**
3. Order the bits of the Aztec code into a linearly ordered bitstring that can be read by the finite state machine of **step 4**. During this process any stuffed bits need to be removed.
  * Takes **2-dimensional array of bits**
  * Gives **bitstring for data/padding/Reed-Solomon codewords, bitstring for mode-message**
4. Parse the mode-message. Finally decode the bitstring of data, padding, and error-correction codewords (Reed-Solomon) by using a finite state machine.
  * Takes **bitstring for data/padding/reed-solomon codewords, bitstring for mode-message**
  * Gives **decoded string**

## Encoding Process Draft

# About the Aztec Code
[General](./about_aztec/general.md)  
|--[Decoding (with Examples)](./about_aztec/decoding.md)  
|--[Encoding (with Examples)](./about_aztec/encoding.md)  
