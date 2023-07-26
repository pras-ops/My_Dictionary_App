# Python Dictionary Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
The Python Dictionary Project is a command-line based dictionary application built using Python. It allows users to search for words and get their meanings from a JSON-based dictionary file.

## Features
- Search for the meanings of words
- Command-line interface for interaction
- JSON-based dictionary data
- Easy-to-use and user-friendly

## Getting Started
### Prerequisites
- Python 3.x
- Git (optional, for cloning the repository)

### Installation
Clone the repository (if you haven't already):
   ```bash
   git clone https://github.com/pras-ops/My_Dictionary_App.git
   cd dictionary_project
   ```
### Usage
To use the dictionary application, run the `main.py` script in the terminal:

   ```bash
      python src/main.py
   ```
Once the application is running, you can enter a word to get its meaning. The application will display the definition if the word is found in the dictionary, otherwise, it will show an appropriate message.

### Data
The dictionary data is stored in a JSON file named `data/dictionary.json`. You can modify this file to add or remove words and their meanings.

### Testing
To run the unit tests for the dictionary module, use the following command:
   ```bash
      pytest tests/test_dictionary.py
   ```