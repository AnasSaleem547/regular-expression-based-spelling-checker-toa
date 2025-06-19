# **Regex Based Enhanced Spell Checker Application**

This Python application provides a comprehensive spell checking solution with a graphical user interface built using Tkinter. It includes features like real-time spell checking, dictionary management, batch processing, synonym lookup, and word autocompletion.

---

## **Features**

- **Spell Checking:** Analyze text for misspelled words  
- **Dictionary Management:** Add new words to the dictionary  
- **Batch Processing:** Check spelling in CSV files  
- **Synonym Lookup:** Find synonyms for words  
- **Autocomplete:** Get word suggestions based on prefixes  
- **Real-time Feedback:** See word processing in real-time  

---

## **Requirements**

- Python 3.x  
- Tkinter (usually included with Python installations)  
- CSV module (Python standard library)  

---

## **Installation**

Clone the repository or download the Python file:

git clone https://github.com/AnasSaleem547/regular-expression-based-spelling-checker-toa.git
Ensure you have a dictionary file named dictionary.txt in the same directory as the script. The application expects this file to be present.

# Enhanced Spell Checker Application

This Python application provides a comprehensive spell checking solution with a graphical user interface built using Tkinter. It includes features like real-time spell checking, dictionary management, batch processing, synonym lookup, and word autocompletion.

## **Interface Overview**

- Input Text Area: Enter text to be spell checked
- Output Text Area: Displays results and processing information

Control Buttons:

- Check Spelling: Analyze the input text
- Add Word: Add a new word to the dictionary
- Batch Check: Process a CSV file for misspellings
- Find Synonyms: Look up synonyms for a word
- Autocomplete: Get word suggestions based on a prefix

---

## Key Functions

- Spell Checking: Enter text and click "Check Spelling" to identify misspelled words
- Adding Words: Use "Add Word" to expand the dictionary
- Batch Processing: Process CSV files with "Batch Check"
- Synonym Lookup: Find alternative words with "Find Synonyms"
- Autocomplete: Get word suggestions with "Autocomplete"

---

## Customization

To customize the application:

- Update Dictionary: Modify the dictionary.txt file to add/remove words
- Add Synonyms: Expand the synonyms dictionary in the SpellCheckerApp class
- Modify Styling: Adjust colors and fonts in the button style dictionary:

  btn_style = {
    'bg': '#0052cc',
    'fg': 'white',
    'padx': 10,
    'pady': 5,
    'font': ('Helvetica', 12, 'bold')
  }

---

## Limitations

- The synonym dictionary is predefined and static
- Dictionary file (dictionary.txt) must be present in the same directory
- Batch processing only works with CSV files

---

# Contributors
Thanks to the following people for their contributions:

- **[@bilal-ahmed-khan7412](https://github.com/bilal-ahmed-khan7412)**

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

## License

This project is licensed under the MIT License.


