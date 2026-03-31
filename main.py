def preprocess(lines):
    """
    Converts lines of text into a list of lists,
    where each inner list contains uppercase words from a line,
    ignoring apostrophes and splitting on non-alphanumeric characters.
    """
    result = []
    for line in lines:
        line = line.upper().replace("'", "")  # Remove apostrophes
        words = [word for word in line.split() if word.isalpha()]
        result.append(words)
    return result
 
def extract_abbreviations(words):
    """
    Identifies potential abbreviations from a list of words
    based on the assignment's scoring rules.
    """
    def find_pos(position):
        """
        Helper function to find the word and position of a character
        given its overall position in the concatenated words.
        """
        for i, word in enumerate(words):
            if len(word) > position:
                break
            position -= len(word)
        if position == 0:  # First letter of a word
            score = 0
        elif position == len(word) - 1:  # Last letter of a word
            score = 20 if word[position] == 'E' else 5
        else:
            position_value = max(0, position - 1)  # 0 for 1st, 1 for 2nd, etc.
            score = position_value + common_score.get(word[position], 0)
        return i, position, score
 
    result = {}
    common_score = {'A': 25, 'B': 8, 'C': 8, 'D': 9, 'E': 35, 'F': 7,
                    'G': 9, 'H': 7, 'I': 25, 'J': 3, 'K': 6, 'L': 15,
                    'M': 8, 'N': 15, 'O': 20, 'P': 8, 'Q': 1, 'R': 15,
                    'S': 15, 'T': 15, 'U': 20, 'V': 7, 'W': 7, 'X': 3, 'Y': 7, 'Z': 1}
    total_length = sum(len(word) for word in words)
 
    for i in range(1, total_length):
        index1, pos1, score1 = find_pos(i)
        abbrev = words[0][0] + words[index1][pos1]
        for j in range(i + 1, total_length):
            index2, pos2, score2 = find_pos(j)
            abbrev += words[index2][pos2]
            score = score1 + score2
            result[abbrev] = min(result.get(abbrev, float('inf')), score)  # Keep lowest score
 
    return result
 
def remove_duplicates(abbrevs):
    """
    Removes duplicate abbreviations across multiple lines.
    """
    indices = {}
    for abbrev_dict in abbrevs:
        for abbrev in abbrev_dict:
            indices.setdefault(abbrev, []).append(abbrev_dict[abbrev])
 
    unique_abbrevs = [abbrev for abbrev, scores in indices.items() if len(scores) == 1]
 
    filtered = []
    for abbrev_dict in abbrevs:
        filtered.append({abbrev: score for abbrev, score in abbrev_dict.items() if abbrev in unique_abbrevs})
    return filtered
 
def find_lowest_scores(abbrev_dict):
    """
    Returns abbreviations with the lowest score from a dictionary.
    """
    if not abbrev_dict:
        return []
    min_score = min(abbrev_dict.values())
    return [abbrev for abbrev, score in abbrev_dict.items() if score == min_score]
 
def main():
    """
    Processes the 'trees.txt' file to extract abbreviations according to the assignment rules.
    """
    with open('trees.txt', 'r') as file:
        lines = file.readlines()
 
    processed_lines = preprocess(lines)
    abbreviations = [extract_abbreviations(words) for words in processed_lines]
    filtered_abbrevs = remove_duplicates(abbreviations)
 
    out_path = 'Alsammak_trees_abbrevs.txt'  # Output file name
    with open(out_path, 'w') as file:
        for line, abbrev_dict in zip(lines, filtered_abbrevs):
            result = find_lowest_scores(abbrev_dict)
            file.write(line.strip() + '\n')  # Write the original line
            file.write(' '.join(result) + '\n')  # Write the abbreviations
 
if __name__ == '__main__':
    main()