# Decoding
*Note: We assume every image to be free of errors, so that the topic of error-correction can be left to the encoding section.*

Steps of the Decoding Process:
1. Decode the mode message to get the number of layers and the number of data codewords.
2. Calculate the total amount of bits of the codewords and padding, depending on the amount of layers bits might need to be skipped at the beginning:
    * Compact: **(88 + 16\*L)\*L** with L=number of layers
    * Full: **(112 + 16\*L)\*L** with L=number of layers
3. Read all the bits for the previously obtained number of data codewords. The pattern for reading this bitstring is peculiar and best left to the examples below. Furthermore any stuffed bits (complementary bits that the encoder inserts if all but the last bit of a codeword are of the same value) need to be skipped. Even further a full Aztec symbol has a reference grid (alternating bits in every 16th row and column, centered on the bulls-eye) which also needs to be skipped.  
![Reference Grid on a Symbol of Maximum Size (151x151)](reference_grid_maximum.png)
4. Once all the bits of the encoded data are collected, the translation process into the original data can finally start.

 Value | Upper | Lower | Mixed | Punct | Digit
---|---|---|---|---|---
 0 | P/S | P/S | P/S | FLG(n) | P/S
 1 | SP | SP | SP | CR | SP 
 2 | A | a | ^A | CR LF | 0 
 3 | B | b | ^B | .SP | 1 
 4 | C | c | ^C | ,SP | 2 
 5 | D | d | ^D | :SP | 3 
 6 | E | e | ^E | ! | 4 
 7 | F | f | ^F | " | 5
 8 | G | g | ^G | # | 6
 9 | H | h | ^H | $ | 7
 10 | I | i | ^I | % | 8
 11 | J | j | ^J | & | 9
 12 | K | k | ^K | ' | ,
 13 | L | l | ^L | ( | .
 14 | M | m | ^M | ) | U/L
 15 | N | n | ^[ | * | U/S
 16 | O | o | ^\ | + | 
 17 | P | p | ^] | , | 
 18 | Q | q | ^^ | - | 
 19 | R | r | ^_ | . | 
 20 | S | s | @ | / | 
 21 | T | t | \\ | : | 
 22 | U | u | ^ | ; | 
 23 | V | v | _ | < | 
 24 | W | w | ` | = | 
 25 | X | x | \| | > | 
 26 | Y | y | ~ | ? | 
 27 | Z | z | ^? | [ | 
 28 | L/L | U/S | L/L | ] | 
 29 | M/L | M/L | U/L | { | 
 30 | D/L | D/L | P/L | } | 
 31 | B/S | B/S | B/S | U/L | 

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
