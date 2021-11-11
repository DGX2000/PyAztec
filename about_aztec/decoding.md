# Decoding
*Note: We assume every image to be free of errors, so that the topic of error-correction can be left to the encoding section.*

Steps of the Decoding Process:
1. Decode the mode message to get the number of layers and the number of data codewords.
2. Calculate the total amount of bits of the codewords and padding, depending on the amount of layers bits might need to be skipped at the beginning:
    * Compact: **(88 + 16\*L)\*L** with L=number of layers
    * Full: **(112 + 16\*L)\*L** with L=number of layers
3. Read all the bits for the previously obtained number of data codewords. The pattern for reading this bitstring is peculiar and best left to the examples below. Furthermore any stuffed bits - complementary bits that the encoder inserts if all but the last bit of a codeword are of the same value - need to be skipped. Even further a full Aztec symbol has a reference grid (every 16th row and column, centered on the bulls-eye) which bits also need to be skipped.
![Reference Grid on a Symbol of Maximum Size (151x151)](reference_grid_maximum.png)
4. Once all the bits of the encoded data are collected, the translation process into the original data can finally start.

- table for standard aztec encoding
- special notes

### Example 1: Straightforward Decoding

- image for decoding mode message
- image for decoding codewords

### Example 2: Decoding Digits

- image for decoding mode message
- image for decoding codewords

### Example 3: Decoding 8-Bit Characters

- image for decoding mode message
- image for decoding codewords
