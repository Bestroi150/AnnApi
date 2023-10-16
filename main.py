import spacy
from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

nlp = spacy.load('la_core_web_lg')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def annotate():
    if request.method == 'POST':
        text = request.form.get('text', '')
        segmented_text = tokenize_with_spacy(text)
        annotated_text = annotate_text(segmented_text)
        
        if 'save' in request.form:
            # Generate a unique file name using a timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f'annotations_{timestamp}.json'
            save_annotations_as_json(annotated_text, filename)
        
        return render_template('annotate.html', text=text, segmented_text=segmented_text, annotated_text=annotated_text)
    
    return render_template('annotate.html')

def save_modifications_as_json(request_data, filename):
    modifications = []

    # Extract data from the form fields
    for i in range(len(request_data.getlist('token'))):
        token_data = {
            "token": request_data.getlist('token')[i],
            "pos": request_data.getlist('pos')[i],
            "lemma": request_data.getlist('lemma')[i]
        }
        
        if token_data["pos"] in ['NOUN', 'PROPN', 'PRON', 'CCONJ', 'PART', 'ADJ', 'DET']:
            token_data.update({
                "case": request_data.getlist('case')[i],
                "gender": request_data.getlist('gender')[i],
                "number": request_data.getlist('number')[i]
            })
        elif token_data["pos"] in ['VERB', 'AUX']:
            token_data.update({
                "aspect": request_data.getlist('aspect')[i],
                "tense": request_data.getlist('tense')[i],
                "verbForm": request_data.getlist('verbForm')[i],
                "voice": request_data.getlist('voice')[i],
                "mood": request_data.getlist('mood')[i],
                "person": request_data.getlist('person')[i]
            })

        modifications.append(token_data)

    # Save the modifications as JSON
    with open(filename, 'w') as json_file:
        json.dump(modifications, json_file)


def tokenize_with_spacy(text):
    doc = nlp(text)
    return [token.text for token in doc]

def annotate_text(segmented_text):
    annotated_tokens = []
    for token in segmented_text:
        doc = nlp(token)
        annotated_token = {
            'token': token,
            'pos': str(doc[0].pos_),
            'lemma': str(doc[0].lemma_),
            'aspect': ', '.join(doc[0].morph.get("Aspect", default=[""])),
            'tense': ', '.join(doc[0].morph.get("Tense", default=[""])),
            'verbForm': ', '.join(doc[0].morph.get("VerbForm", default=[""])),
            'voice': ', '.join(doc[0].morph.get("Voice", default=[""])),
            'mood': ', '.join(doc[0].morph.get("Mood", default=[""])),
            'number': ', '.join(doc[0].morph.get("Number", default=[""])),
            'person': ', '.join(doc[0].morph.get("Person", default=[""])),
            'case': ', '.join(doc[0].morph.get("Case", default=[""])),
            'gender': ', '.join(doc[0].morph.get("Gender", default=[""]))
        }

        annotated_tokens.append(annotated_token)
    return annotated_tokens

def save_annotations_as_json(annotated_text, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(annotated_text, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(debug=True)


