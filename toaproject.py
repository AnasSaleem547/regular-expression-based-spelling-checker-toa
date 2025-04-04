import csv
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, scrolledtext
import os

def load_dictionary(file_path):
    dictionary = set()
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for word in row:
                    lower_case_word = word.strip().lower()
                    if lower_case_word:
                        dictionary.add(lower_case_word)
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {file_path} was not found.")
    except PermissionError:
        messagebox.showerror("Error", f"Permission denied when trying to read {file_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return dictionary

def tokenize(text):
    words = []
    current_word = []
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            current_word.append(lower_char)
        else:
            if current_word:
                word = ''.join(current_word)
                words.append(word)
                current_word = []
    if current_word:
        final_word = ''.join(current_word)
        words.append(final_word)
    return words

def spell_check(text, dictionary, callback):
    tokens = tokenize(text)
    misspelled_words = []
    for token in tokens:
        callback(token)
        if token not in dictionary:
            misspelled_words.append(token)
    return misspelled_words

def batch_spell_check(file_path, dictionary):
    misspelled_words = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line in reader:
                for word in line:
                    words_in_line = tokenize(word)
                    for word in words_in_line:
                        if word not in dictionary:
                            misspelled_words.append(word)
    except FileNotFoundError:
        messagebox.showinfo("File Not Found", "The specified file could not be found.")
    return misspelled_words

def add_to_dictionary(word, dictionary):
    lowercase_word = word.lower()
    dictionary.add(lowercase_word)

def find_synonyms(word, synonyms):
    if word:
        synonyms_list = synonyms.get(word, [])
        return synonyms_list
    return []

def autocomplete(prefix, dictionary):
    suggestions = []
    for word in dictionary:
        if word.startswith(prefix):
            suggestions.append(word)
    return suggestions

class SpellCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Enhanced Spell Checker Application")
        master.configure(background='#f0f0f0')

        base_dir = os.path.dirname(os.path.abspath(__file__))
        dictionary_path = os.path.join(base_dir, "words_pos.csv")
        self.dictionary = load_dictionary(dictionary_path)
        self.synonyms = {
            'bestfriend':['sir faisal','toa teacher','toa'],
            'accommodation': ['lodging', 'housing', 'residence'],
            'achieve': ['accomplish', 'attain', 'realize'],
            'across': ['over', 'through', 'crosswise'],
            'address': ['location', 'direction', 'speak to'],
            'advice': ['guidance', 'recommendation', 'counsel'],
            'advise': ['recommend', 'suggest', 'counsel'],
            'affect': ['influence', 'impact', 'alter'],
            'after': ['following', 'subsequent', 'later'],
            'again': ['once more', 'repeatedly', 'anew'],
            'against': ['opposite', 'contrary', 'versus'],
            'aggressive': ['forceful', 'assertive', 'aggressive'],
            'almost': ['nearly', 'virtually', 'about'],
            'among': ['between', 'in the midst of', 'surrounded by'],
            'apparent': ['obvious', 'evident', 'clear'],
            'appearance': ['look', 'presence', 'aspect'],
            'argument': ['debate', 'dispute', 'discussion'],
            'assessment': ['evaluation', 'appraisal', 'analysis'],
            'basically': ['fundamentally', 'essentially', 'primarily'],
            'beginning': ['start', 'commencement', 'onset'],
            'believe': ['think', 'feel', 'suppose'],
            'benefit': ['advantage', 'gain', 'profit'],
            'breathe': ['inhale', 'exhale', 'respire'],
            'brilliant': ['bright', 'intelligent', 'splendid'],
            'business': ['trade', 'commerce', 'occupation'],
            'calendar': ['schedule', 'datebook', 'planner'],
            'category': ['class', 'group', 'division'],
            'certain': ['sure', 'positive', 'convinced'],
            'challenge': ['difficulty', 'obstacle', 'contest'],
            'change': ['alter', 'modify', 'transform'],
            'character': ['personality', 'nature', 'disposition'],
            'choose': ['select', 'pick', 'opt'],
            'coming': ['approaching', 'next', 'forthcoming'],
            'committee': ['panel', 'board', 'group'],
            'completely': ['totally', 'entirely', 'fully'],
            'conscience': ['morals', 'scruples', 'ethics'],
            'conscious': ['aware', 'awake', 'alert'],
            'decision': ['choice', 'verdict', 'conclusion'],
            'definitely': ['certainly', 'clearly', 'absolutely'],
            'describe': ['depict', 'explain', 'define'],
            'desperate': ['hopeless', 'reckless', 'frantic'],
            'different': ['diverse', 'varied', 'distinct'],
            'difficult': ['hard', 'challenging', 'tough'],
            'disappear': ['vanish', 'fade', 'dissolve'],
            'disappoint': ['dismay', 'let down', 'fail'],
            'discipline': ['control', 'training', 'order'],
            'drunk': ['intoxicated', 'inebriated', 'tipsy'],
            'during': ['throughout', 'in the course of', 'amid'],
            'eager': ['keen', 'enthusiastic', 'avid'],
            'environment': ['surroundings', 'setting', 'ecosystem'],
            'equipped': ['furnished', 'provided', 'outfitted'],
            'especially': ['particularly', 'specially', 'notably'],
            'exaggerate': ['overstate', 'embellish', 'amplify'],
            'excellent': ['superb', 'outstanding', 'marvelous'],
            'except': ['besides', 'apart from', 'excluding'],
            'existence': ['being', 'existence', 'life'],
            'experience': ['encounter', 'knowledge', 'practice'],
            'experiment': ['test', 'trial', 'investigation'],
            'explanation': ['clarification', 'description', 'account'],
            'familiar': ['well-known', 'common', 'acquainted'],
            'finally': ['ultimately', 'eventually', 'at last'],
            'fluorescent': ['bright', 'glowing', 'vivid'],
            'foreign': ['overseas', 'external', 'alien'],
            'forty': ['four tens', '40'],
            'forward': ['ahead', 'onward', 'forth'],
            'friend': ['companion', 'ally', 'associate'],
            'further': ['additional', 'more', 'farther'],
            'gist': ['essence', 'main point', 'substance'],
            'government': ['administration', 'regime', 'authority'],
            'guard': ['protect', 'defend', 'shield'],
            'happened': ['occurred', 'took place', 'transpired'],
            'harass': ['bother', 'annoy', 'pester'],
            'hierarchy': ['ranking', 'pecking order', 'structure'],
            'humorous': ['funny', 'amusing', 'entertaining'],
            'identity': ['individuality', 'personality', 'character'],
            'immediately': ['instantly', 'directly', 'promptly'],
            'important': ['significant', 'crucial', 'vital'],
            'incidentally': ['by the way', 'aside', 'additionally'],
            'independent': ['self-sufficient', 'autonomous', 'free'],
            'interrupt': ['disrupt', 'break', 'halt'],
            'irresistible': ['enticing', 'tempting', 'compelling'],
            'knowledge': ['awareness', 'information', 'understanding'],
            'leisure': ['free time', 'downtime', 'relaxation'],
            'liaison': ['link', 'connection', 'contact'],
            'library': ['bookstore', 'archive', 'depository'],
            'license': ['permit', 'authorization', 'warrant'],
            'maintenance': ['upkeep', 'care', 'preservation'],
            'manageable': ['controllable', 'feasible', 'practicable'],
            'marriage': ['wedding', 'matrimony', 'union'],
            'medicine': ['medication', 'drug', 'remedy'],
            'millennium': ['thousand years', 'eon', 'age'],
            'necessary': ['essential', 'needed', 'required'],
            'neighbor': ['adjacent', 'nearby', 'next door'],
            'noticeable': ['obvious', 'evident', 'prominent'],
            'occasion': ['event', 'time', 'moment'],
            'occurred': ['happened', 'took place', 'transpired'],
            'official': ['formal', 'authorized', 'executive'],
            'opportunity': ['chance', 'occasion', 'opening'],
            'parallel': ['comparable', 'similar', 'analogous'],
            'parliament': ['congress', 'assembly', 'council'],
            'particular': ['specific', 'certain', 'peculiar'],
            'pastime': ['hobby', 'leisure activity', 'recreation'],
            'perceive': ['see', 'detect', 'recognize'],
            'performance': ['show', 'presentation', 'execution'],
            'permanent': ['lasting', 'enduring', 'eternal'],
            'perseverance': ['persistence', 'determination', 'tenacity'],
            'personnel': ['staff', 'employees', 'crew'],
            'possession': ['ownership', 'property', 'holding'],
            'possible': ['feasible', 'likely', 'probable'],
            'preferred': ['favored', 'chosen', 'selected'],
            'prejudice': ['bias', 'discrimination', 'bigotry'],
            'presence': ['attendance', 'existence', 'appearance'],
            'privilege': ['advantage', 'right', 'benefit'],
            'probably': ['likely', 'perhaps', 'possibly'],
            'procedure': ['process', 'operation', 'method'],
            'professor': ['teacher', 'instructor', 'educator'],
            'prominent': ['notable', 'distinguished', 'eminent'],
            'pronunciation': ['articulation', 'enunciation', 'accentuation'],
            'publicly': ['openly', 'publically'],
            'really': ['truly', 'actually', 'indeed'],
            'receipt': ['invoice', 'bill', 'voucher'],
            'receive': ['get', 'accept', 'obtain'],
            'recommend': ['suggest', 'advise', 'propose'],
            'reference': ['citation', 'mention', 'allusion'],
            'relevant': ['applicable', 'pertinent', 'germane'],
            'religious': ['spiritual', 'sacred', 'devout'],
            'remember': ['recall', 'recollect', 'memorize'],
            'resistance': ['opposition', 'defiance', 'rebellion'],
            'resource': ['supply', 'asset', 'means'],
            'restaurant': ['eatery', 'diner', 'cafe'],
            'rhyme': ['verse', 'poem', 'lyric'],
            'rhythm': ['beat', 'tempo', 'pace'],
            'ridiculous': ['absurd', 'ludicrous', 'preposterous'],
            'sacrifice': ['forfeit', 'give up', 'surrender'],
            'secretary': ['assistant', 'clerk', 'administrator'],
            'separate': ['divide', 'detach', 'isolate'],
            'sergeant': ['non-commissioned officer', 'NCO'],
            'significant': ['important', 'meaningful', 'major'],
            'similar': ['alike', 'comparable', 'analogous'],
            'sincerely': ['genuinely', 'honestly', 'earnestly'],
            'strength': ['power', 'force', 'might'],
            'successful': ['prosperous', 'victorious', 'fruitful'],
            'superintendent': ['supervisor', 'manager', 'director'],
            'supersede': ['replace', 'supplant', 'overtake'],
            'sure': ['certain', 'confident', 'positive'],
            'surprise': ['astonish', 'amaze', 'startle'],
            'technique': ['method', 'skill', 'tactic'],
            'temperature': ['heat', 'warmth', 'climate'],
            'therefore': ['thus', 'consequently', 'hence'],
            'threshold': ['doorstep', 'brink', 'limit'],
            'tomorrow': ['next day', 'following day'],
            'tongue': ['language', 'speech', 'lingua'],
            'truly': ['really', 'genuinely', 'sincerely'],
            'unconscious': ['insensible', 'comatose', 'unaware'],
            'understand': ['comprehend', 'grasp', 'perceive'],
            'unexpected': ['unforeseen', 'unanticipated', 'surprising'],
            'unfortunately': ['regrettably', 'sadly', 'alas'],
            'unique': ['distinctive', 'singular', 'exclusive'],
            'useful': ['helpful', 'practical', 'beneficial'],
            'usually': ['normally', 'generally', 'typically'],
            'vacuum': ['void', 'emptiness', 'vacuity'],
            'vehicle': ['car', 'transport', 'automobile'],
            'visible': ['seeable', 'observable', 'evident'],
            'weather': ['climate', 'conditions', 'atmosphere'],
            'weird': ['strange', 'unusual', 'bizarre']
        }

        btn_style = {'bg': '#0052cc', 'fg': 'white', 'padx': 10, 'pady': 5, 'font': ('Helvetica', 12, 'bold')}
        self.input_label = tk.Label(master, text="Input", font=('Helvetica', 14, 'bold'))
        self.input_label.pack(pady=(10, 0))
        self.text_input = scrolledtext.ScrolledText(master, height=10, width=50, font=('Helvetica', 12))
        self.text_input.pack(pady=(10, 0))

        self.check_btn = tk.Button(master, text="Check Spelling", command=self.check_spelling, **btn_style)
        self.check_btn.pack(pady=5)

        self.add_btn = tk.Button(master, text="Add Word", command=self.add_word, **btn_style)
        self.add_btn.pack(pady=5)

        self.batch_btn = tk.Button(master, text="Batch Check", command=self.batch_check, **btn_style)
        self.batch_btn.pack(pady=5)

        self.synonyms_btn = tk.Button(master, text="Find Synonyms", command=self.find_synonyms, **btn_style)
        self.synonyms_btn.pack(pady=5)

        self.autocomplete_btn = tk.Button(master, text="Autocomplete", command=self.autocomplete, **btn_style)
        self.autocomplete_btn.pack(pady=5)
        self.output_label = tk.Label(master, text="Output", font=('Helvetica', 14, 'bold'))
        self.output_label.pack(pady=(10, 0))
        self.output_area = scrolledtext.ScrolledText(master, height=10, width=50, state='disabled', font=('Helvetica', 12))
        self.output_area.pack(pady=(0, 10))

    def check_spelling(self):
        input_text = self.text_input.get('1.0', tk.END)
        self.output_area.config(state='normal')
        self.output_area.delete('1.0', tk.END)
        misspelled = spell_check(input_text, self.dictionary, self.process_word)
        final_message = "Misspelled words: " + ', '.join(misspelled) if misspelled else "No misspellings found!"
        self.display_output(f"\n{final_message}")

    def process_word(self, word):
        self.display_output(f"Checking word: {word}...", append=True)

    def add_word(self):
        word = simpledialog.askstring("Input", "Enter a word to add to the dictionary:")
        if word:
            add_to_dictionary(word, self.dictionary)
            self.display_output(f"Added '{word}' to dictionary.")

    def batch_check(self):
        filename = filedialog.askopenfilename()
        if filename:
            misspelled = batch_spell_check(filename, self.dictionary)
            message = "Misspelled words in file: " + ', '.join(misspelled) if misspelled else "No misspellings found in file!"
            self.display_output(message)

    def find_synonyms(self):
        word = simpledialog.askstring("Input", "Enter a word to find synonyms for:")
        if word:
            synonyms_list = find_synonyms(word, self.synonyms)
            if synonyms_list:
                message = "Synonyms for " + word + ": " + ', '.join(synonyms_list)
            else:
                message = "No synonyms found for " + word
            self.display_output(message)

    def autocomplete(self):
        prefix = simpledialog.askstring("Input", "Enter prefix for autocomplete:")
        if prefix:
            suggestions = autocomplete(prefix, self.dictionary)
            message = "Suggestions: " + ', '.join(suggestions) if suggestions else "No suggestions found."
            self.display_output(message)

    def display_output(self, message, append=False):
        if not append:
            self.output_area.config(state='normal')
            self.output_area.delete('1.0', tk.END)
        self.output_area.insert(tk.END, message + '\n')
        self.output_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
