# Cryptanalysis Tools

A collection of Python functions for analysing text, frequency distributions,
and classical substitution ciphers.

This project started as a personal collection of utilities written while
learning Python and studying classical cryptography. The emphasis is on
understanding the algorithms involved rather than relying on external
libraries.

The code is intended to be readable, educational, and easy to modify.

---

## Features

### Text Processing

- Remove punctuation and non-alphabetic characters
- Convert text to uppercase
- Optionally preserve spaces
- Accept multi-line text input

### Vocabulary Analysis

- Extract unique words from a body of text
- Prepare text for further statistical analysis

### Frequency Analysis

- Calculate letter frequencies for A-Z
- Optionally include space frequencies
- Compare observed frequencies against standard English frequencies

### Tetragram Analysis

- Generate tetragram frequency tables
- Export tetragram counts to text files
- Useful for experimentation with classical cipher-breaking techniques

### Statistical Tools

- Chi-squared calculations
- Text scoring using English letter frequencies
- Vector inner products
- Components for future cryptanalysis tools

---

## Why This Exists

Many examples of cryptographic analysis online focus on using large libraries
or prebuilt tools. This project takes the opposite approach.

The aim is to implement common techniques directly in Python in order to
understand how they work internally.

This repository serves both as a learning project and as a toolkit that can be
reused in future cipher experiments.

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

---

## References

This project was developed using information from a variety of educational
sources, including:

- *Classical Cryptography* by Thomas Kaeding (Madness)
- Wikipedia articles relating to:
  - Frequency analysis
  - Chi-squared statistics
  - Classical cryptography
  - N-grams and tetragrams

Where external data files are used (for example tetragram frequency data),
appropriate attribution should be preserved.

---

## Goals

Planned additions include:

- Caesar cipher analysis
- Vigenère cipher analysis
- Index of Coincidence calculations
- Cosine similarity scoring
- Hill-climbing attacks
- N-gram scoring improvements
- Language comparison tools

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
