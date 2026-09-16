# Cryptanalysis Tools

A collection of Python functions for analysing text, frequency distributions,
and classical substitution ciphers.

This project started as a personal collection of utilities written while
learning Python and studying classical cryptography. The emphasis is on
understanding the algorithms involved rather than relying on external
libraries.

The code is intended to be readable, educational, and easy to modify.

---

## Brown Corpus

Some frequency data included in this project was generated using the
Brown Corpus.

The Brown Corpus contains copyrighted material and is subject to
restrictions on reproduction and redistribution.

To respect those restrictions, I have not included a copy of the
Brown Corpus in this repository.

Users wishing to obtain the corpus should consult the Brown Corpus
documentation and obtain a copy from an authorised source.

Source:
https://listings.lib.msu.edu/public-corpora/cd421/manuals/brown/INDEX.HTM
(accessed 16 September 2026)
---

### Text Processing

 Remove punctuation and non-alphabetic characters
 Convert text to uppercase
 Optionally preserve spaces
 Accept multi-line text input

### Vocabulary Analysis

Extract unique words from a body of text
 Prepare text for further statistical analysis

### Frequency Analysis

 Calculate letter frequencies for A-Z
Optionally include space frequencies
Compare observed frequencies against standard English frequencies

### Tetragram Analysis

 Generate tetragram frequency tables
 Export tetragram counts to text files
 Useful for experimentation with classical cipher-breaking techniques

### Statistical Tools

 Chi-squared calculations
 Text scoring using English letter frequencies
 Vector inner products
 Components for future cryptanalysis tools

---

## Why I made this

Many examples of cryptographic analysis online focus on using large libraries
or prebuilt tools. This project takes the opposite approach.

The aim is to implement common techniques directly in Python in order to
understand how they work internally.

This repository serves both as a learning project and as a toolkit that can be
reused in future cipher experiments.

Also, who are we kidding? It's fun.

---

## Current Functions

| Function | Purpose |
|----------|---------|
| `get_text()` | Accept multi-line text input |
| `clean()` | Normalize text for analysis |
| `unique()` | Find unique words |
| `letter_freqs()` | Calculate letter frequencies |
| `tetragram_freqs()` | Generate tetragram frequency files |
| `X_squared()` | Calculate a chi-squared statistic |
| `X_squared_text()` | Compare text to expected English frequencies |
| `inner_product()` | Calculate vector dot products |
| `validate()` | Ensures input matches expected type |
| `find_cosine_angle()` | Determines cosine similarity |
| `IOC()` | Calculate index of coincidence |
| `shift_by()` | Shifts alphabet |
| `caesar()` | Basic implementation of caesar cipher |
| `parse()` | Attempts to add spaces to text, badly
| `split_blocks()` | Splits text into blocks of every nth letter |
| `gen()` | Generates an alphabet key from a keyword |

---

## References

This project was developed using information from a variety of educational
sources, including:

- *Classical Cryptography* by Thomas Kaeding (Madness)
- Various Wikipedia articles
- The National Cipher Challenge
- The Brown corpus (for linguistic data)

Special thanks to my high school teacher, Lisa Gittlemon, who encouraged me to first learn to code instead of kicking me out of her classroom when I got bored.

Where external data files are used (for example tetragram frequency data),
appropriate attribution should be preserved.

---


## Disclaimer

This project is intended for educational purposes and historical cryptographic
study. It is not intended for modern cryptographic security applications. It is
purely for fun and I take no responsibility if you use this for cheating or 
to gain access to confidential material, however implausible this may seem.

---

## Author

Created by Leah (Leya) Gross.
(Gross rhymes with boss and not with close)

Feel free to use, modify, and learn from this code. If redistributing modified
versions, please preserve existing attribution notes and references where
appropriate.
