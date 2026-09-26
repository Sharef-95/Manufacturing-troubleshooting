from spellchecker import SpellChecker
from rapidfuzz import fuzz
import streamlit as st

spell = SpellChecker()


QA_DATA = { 
  "Drying Issues": "Call maintenance.",

"Lois Sensor Issue": "Call maintenance.",

"Blurry Barcodes": "Check the vacuum level.\n\n"
"Vacuum level must be set to 10 for all types of sheets.\n\n"
"Vacuum level for magnets must be set to 5.",

"Encoder Issue": "Call maintenance.",

"Banding": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"Step 4: Print a nozzle test.\n\n"
"If banding is still present after wiping, call your supervisor/PC.",

"Computer Frozen": "Restart the DURST app.",

"Door Issues": "Open the door and re-close it gently.",

"Initialization Issues": "Step 1: Go to the Printer tab.\n\n"
"Step 2: Click Initialize Sledge.\n\n"
"Step 3: Click Initialize Printer.\n\n"
"If it still does not initialize, restart the machine.",

"Communication Issues": "Restart the machine.",

"Head Crash": "Go to the Printer tab and click Initialize Printer.",

"Ink Leak": "Call maintenance.",

"Jam": "Go to the Printer tab and click Initialize Printer.",

"Loading Issues": "",

"Registration Issues": "Check the vacuum level.\n\n"
"Vacuum level must be set to 10 for all types of sheets.\n\n"
"Vacuum level for magnets must be set to 5.",

"UV Issues": "Go to the Printer tab, turn the UV lamp off, and turn it back on.\n\n"
"If it does not work, restart the machine.",

"Vacuum Issues": "Call maintenance.",

"UV Lamp Failure": "Go to the Printer tab, turn the UV lamp off, and turn it back on.\n\n"
"If it does not work, restart the machine.",

"Banding in the Firstoff": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"Step 4: Print a nozzle test.\n\n"
"If banding is still present after wiping, call your supervisor/PC.",

"Missing Nozzles": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"If nozzles are still missing, call your supervisor.",

"Printhead Ink Tank Error": "Lift up the ink waste lever and close it down gently.\n\n"
"If the error is not cleared, call maintenance.",

"Continuous Feeder Issues": "Check that the feeding switch is on. The switch is located at the bottom-left of the front end of the machine.",

"UV Lamps": "Go to the Printer tab, turn the UV lamp off, and turn it back on.\n\n"
"If the UV lamp is still not working, restart the machine.",

"Ink Spots": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"If ink spots are still present after wiping, call your supervisor/PC.",

"Water Marks Ink Seeming Lawn": "Call maintenance.",

"Rub Marks": "Call maintenance.",

"Air Fitting Leaking": "Call maintenance.",

"Ink Smearing": "",

"UV Lamp Failure One and 2": "Go to the Printer tab, turn the UV lamp off, and turn it back on.\n\n"
"If the UV lamp is still not working, restart the machine.",

"Ink Not Heating": "Restart the machine.",

"M/C4 Component Error": "Call maintenance.",

"Pink Lines Around Product": "Call maintenance.",

"Lines Through Grey Images": "Call maintenance.",

"Piece Of Magnet Stuck Inside": "Call maintenance.",

"Printing Program Has No Options For Printing": "Call IT.",

"Loose Screw": "Call maintenance.",

"Air Hose": "Call maintenance.",

"Purge Tub Error": "Open the purge tub and re-close it gently.",

"Paper Jammed In Press": "Increase the vacuum.",

"Power Outage": "Call maintenance.",

"Curing Issues": "Call maintenance.",

"Making Loud Noise": "Call maintenance.",

"Sledge Will Not Initialize": "Go to the Printer tab and click Initialize Sledge.\n\n"
"If the sledge does not initialize, restart the machine.",

}

def correct_spelling(text):
    words = text.split()
    corrected_words = []

    for word in words:
        corrected = spell.correction(word)
        corrected_words.append(corrected if corrected else word)

    return " ".join(corrected_words)

def get_answer(question: str) -> str:
    question = correct_spelling(question)

    q = question.strip().lower()

    for stored_q, stored_a in QA_DATA.items():
        if stored_q.strip().lower() == q:
            return stored_a
    best_score = 0
    best_answer = None

    # optional: partial match when no exact match is found
    for stored_q, stored_a in QA_DATA.items():
        score = fuzz.token_set_ratio(q,stored_q.strip().lower())
        if score > best_score:
            best_score = score
            best_answer = stored_a

    if best_score >= 45:
        return best_answer

    return "Sorry, I don't have an answer for that question yet."

def Rigid2():
    Search = st.text_input("Rigid 2",
key="Rigid2")

    if Search:
     answer = get_answer(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)
            