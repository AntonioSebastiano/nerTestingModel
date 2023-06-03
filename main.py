import spacy
from pathlib import Path
output_dir = Path(r'C:\Users\anton\Documents\RepositorySourceTree\DjangoAvatarBE - Airport\ner\model')  #inserire il path del modello


while(1):
    # Load the saved model and predictdo
    print("Loading from", output_dir)
    nlp_updated = spacy.load(output_dir)
    text = input()
    print(text)
    doc = nlp_updated(text)
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])

