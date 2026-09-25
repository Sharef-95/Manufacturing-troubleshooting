from spellchecker import SpellChecker
from rapidfuzz import fuzz
import streamlit as st

spell = SpellChecker()

QA_DATA = { 
    "Door Issues": "open door, re-close gently."
    "if it doesn't work call maintenance. ",
    "Vacuum Issues": "Check vacuum level by adjusting vacuum knob located behind the machine."
    "if vacuum knob doesn't work, call maintenance.",
    "Blurry Barcodes": "Increase vacuum level, by turning vacuum knob clockwise",
    "Banding": "step 1: wet wipe all printheads\n\n"
"step 2: short purge all printheads.\n\n"
"step 3: Dry wipe all printheads.\n\n"
    "step 4: print nozzle test.\n\n"
    "if banding is still present after wiping, call your supervisor",
    
    "Computer Frozen": "Restart DURST program.",
    "Drying Issues": "call maintenance.",
    "Initialization Issues": "step 1: go printer tab \n\n"
    "step 2:click initialize Sledge\n\n"
    "step 3 click initilize printer"
    "if it's still not initilizing, restart the machine.",
    "Missing Nozzles": "step 1: wet wipe printheads"
    "step 2:long purge "
    "step 3: dry wipe."
    "repeat if missing nozzles are starting toto recover. ",
    "Lois Sensor Issue": "call maintenance.",
    "Purge Tub Error": "open purge tub, re-close it gently.",
    "Registration Issues": "Check vacuum level.",
    "UV Issues": "on printer tab, turn UV lamp off, and turn back on.\n\n"
    "if UV lamp is still not working, restart the machine.",
    "Communication Issues": "restart the machine.",
    "Head Crash": "on printer tab. Click initilize printer.",
    "Ink Leak": "Call maintenance.",
    "Jam": "on printer tab. Click initilize printer",
    "Sledge Control Error": "on printer tab. Click initilize sledge.",
    "Feeding Unit Error": "Check feeding switch is on. The sitch is located at the bottom-left of the front end of the machine.",
    "Computer Frozen": "Restart DURST program.",
    "Feeder Wheels Not Coming Down": "Check feeding switch is on\n\n."
    " The switch is located at the bottom-left of the front end of the machine.",
    "Not Recognizing Purge Tub Is Open for Purge": "open purge tub, re-close it gently.",
    "UV Lamp Error After Sledge Crash": "on printer tab, turn UV lamp off, and turn it back on.\n\n"
"if it doesn't work restart the machine\n\n"
"if it still not worling after restarting the machine, call maintenance.",
    "Power Trip Off": "Restart the machine",
    "ink spray":"short purge all printheads, and dry wipe.",
    "Error In Checking Printhead Ink Tanks":"Left up ink waste lever, and close down gently.\n\n"
"if error isn't cleared, call maintenance."
   
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

def Rigid1():
    Search = st.text_input("Rigid 1",
key="Rigid1")

    if Search:
     answer = get_answer(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)
            