from spellchecker import SpellChecker
from rapidfuzz import fuzz
import streamlit as st

spell = SpellChecker()

QA_DATA = { 
   "Door Issues": "Open door, then re-close gently.\n\n"
                "If it doesn't work, call maintenance.",

"Vacuum Issues": "Check the vacuum level by adjusting the vacuum knob located behind the machine.\n\n"
                  "If the vacuum knob doesn't work, call maintenance.",

"Blurry Barcodes": "Increase the vacuum level by turning the vacuum knob clockwise.",

"Banding": "Step 1: Wet wipe all printheads.\n\n"
           "Step 2: Short purge all printheads.\n\n"
           "Step 3: Dry wipe all printheads.\n\n"
           "Step 4: Print nozzle test.\n\n"
           "If banding is still present after wiping, call your supervisor.",

"Computer Frozen": "Restart the DURST program.",

"Drying Issues": "Call maintenance.",

"Initialization Issues": "Step 1: Go to the Printer tab.\n\n"
                          "Step 2: Click Initialize Sledge.\n\n"
                          "Step 3: Click Initialize Printer.\n\n"
                          "If it's still not initializing, restart the machine.",

"Missing Nozzles": "Step 1: Wet wipe printheads.\n\n"
                   "Step 2: Long purge.\n\n"
                   "Step 3: Dry wipe.\n\n"
                   "Repeat if the missing nozzles are starting to recover.",

"Lois Sensor Issue": "Call maintenance.",

"Purge Tub Error": "Open the purge tub, then re-close it gently.",

"Registration Issues": "Check the vacuum level.",

"UV Issues": "On the Printer tab, turn the UV lamp off, then turn it back on.\n\n"
  "If the UV lamp is still not working, restart the machine.",

"Communication Issues": "Restart the machine.",

"Head Crash": "On the Printer tab, click Initialize Printer.",

"Ink Leak": "Call maintenance.",

"Jam": "On the Printer tab, click Initialize Printer.",

"Sledge Control Error": "On the Printer tab, click Initialize Sledge.",

"Feeding Unit Error": "Check that the feeding switch is on.\n\n"
    "The switch is located at the bottom-left of the front end of the machine.",

"Feeder Wheels Not Coming Down": "Check that the feeding switch is on.\n\n"
    "The switch is located at the bottom-left of the front end of the machine.",

"Not Recognizing Purge Tub Is Open for Purge": "Open the purge tub, then re-close it gently.",

"UV Lamp Error After Sledge Crash": "On the Printer tab, turn the UV lamp off, then turn it back on.\n\n"
  "If it doesn't work, restart the machine.\n\n"
  "If it still isn't working after restarting the machine, call maintenance.",

"Power Trip Off": "Restart the machine.",

"Ink Spray": "Short purge all printheads, then dry wipe.",

"Error In Checking Printhead Ink Tanks": "Lift up the ink waste lever, then close it down gently.\n\n"
    "If the error isn't cleared, call maintenance.",


   
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
            