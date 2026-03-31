🌳 Tree Name Abbreviation Generator (Python)
🎓 Project Overview

This project was developed as part of my coursework at the University of Dundee. It focuses on building a Python program that generates optimal three-letter abbreviations for tree names based on a custom scoring system.

The program processes a list of tree names, generates all possible abbreviations, scores them, and selects the best (lowest-scoring) unique abbreviations.

🚀 **Key Features**
  Processes raw text data containing tree names
  Generates multiple abbreviation combinations per name
  Applies a scoring algorithm based on:
  Letter position
  Letter frequency/commonality
  Ensures abbreviations are unique across all entries
  Outputs the best abbreviation(s) per tree
  🛠️ Technologies Used
  Python
  File Handling (Input/Output)
  Core Data Structures (Lists, Dictionaries)
  
  ⚙️ How It Works
  1. Data Preprocessing
  Converts text to uppercase
  Removes special characters (e.g. apostrophes)
  Splits lines into clean words

    👉 Implemented in:
    preprocess(lines)
  2. Abbreviation Generation
  Combines letters from words to form abbreviations
  Calculates a score for each abbreviation based on position and letter importance

  👉 Core logic:
  extract_abbreviations(words)
  3. Duplicate Removal
  Ensures each abbreviation appears only once across all tree names
  remove_duplicates(abbrevs)

  4. Best Abbreviation Selection
  Selects abbreviation(s) with the lowest score
  find_lowest_scores(abbrev_dict)
  
  5. Output Generation
  Writes results to an output file:
  Alsammak_trees_abbrevs.txt




📂** Project Files**
  Input dataset:
  trees.txt
  Contains tree names such as:
    Alder
    Crab Apple
    Common Ash
    
**Output file:
  
  Alsammak_trees_abbrevs.txt
  Main script: main.py
  Report: Python Assignment.docx

▶️ **How to Run**
  Make sure Python is installed
  Place input file (trees.txt) in the same directory
  Run:
  python main.py
  Check the output file:
  Alsammak_trees_abbrevs.txt
  💡 What I Learned
  Designing structured Python programs using functions
  Working with real-world text data
  Implementing custom scoring algorithms
  Ensuring data uniqueness and correctness
  Writing clean and modular code
  🔮 Possible Improvements
  Allow user-defined abbreviation length
  Add command-line arguments for input/output files
  Improve performance for large datasets
  Add error handling and validation
  Use regular expressions for more robust preprocessing

👤 **Author**
  Sarraj Alsammak
  University of Dundee

This project demonstrates my ability to solve algorithmic problems, work with text data, and build structured Python applications — key skills for software engineering and data-related roles.
