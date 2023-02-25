import spacy
load_model = spacy.load("en_core_web_sm")
doc = load_model("Hi my name is mak")
print(doc)