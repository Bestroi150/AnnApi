# AnnApi - Latin Text Annotation Tool

A Flask-based web application for annotating Latin text with linguistic features using spaCy's Latin language model.

## Features

- **Text Tokenization**: Automatically segments Latin text into tokens using spaCy
- **Linguistic Annotation**: Automatically generates annotations including:
  - Part-of-Speech (POS) tags
  - Lemmatization
  - Morphological features (case, gender, number, aspect, tense, mood, person, voice, verbForm)
- **Interactive Editing**: Modify generated annotations directly in the web interface
- **JSON Export**: Save annotations as structured JSON files with timestamps

## Requirements

- Python 3.7+
- Flask 2.3.3
- spaCy 3.5.0
- Additional dependencies listed in `requirements.txt`

## Installation

1. Clone or download the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Latin language model:
   ```bash
   python -m spacy download la_core_web_lg
   ```

## Project Structure

```
AnnApi/
├── api/
│   └── main.py              # Flask application and core NLP functions
├── templates/
│   └── annotate.html        # Web interface template
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Usage

1. Start the Flask application:
   ```bash
   python api/main.py
   ```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter Latin text in the text area and click "Annotate"

4. Review and edit the generated annotations as needed

5. Click "Save Modifications as JSON" to export the annotated data

## How It Works

### Tokenization
The application uses spaCy's Latin model to tokenize input text into individual tokens.

### Annotation
Each token receives automatic annotations:
- **All tokens**: POS tag, lemma
- **Nouns, adjectives, determiners, pronouns, conjunctions, particles**: case, gender, number
- **Verbs and auxiliaries**: aspect, tense, verbForm, voice, mood, person

### Editing & Export
Annotations are displayed in an editable form where users can modify any field before saving. Export saves all modified annotations as JSON with a timestamp-based filename.

## Dependencies

- **Flask**: Web framework for creating the web interface
- **spaCy**: Natural Language Processing library with pre-trained Latin model
- **Materialize CSS**: Frontend framework for responsive UI

## Output Format

Annotations are saved as JSON with the following structure:

```json
[
  {
    "token": "word",
    "pos": "NOUN",
    "lemma": "lemma",
    "case": "Nom",
    "gender": "Fem",
    "number": "Sing",
    ...
  }
]
```

## License

Please see the [LICENSE](https://github.com/Bestroi150/AnnApi/blob/main/LICENSE) of the application.

