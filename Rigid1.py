from spellchecker import SpellChecker
from rapidfuzz import fuzz, process
import streamlit as st

spell = SpellChecker()



QA_DATA = { 

    
    "What causes color registration error?": "Substrate slip, low vacuum level, or mechanical misalignment.",


    "How do you fix colour registration?": "Increase the vacuum level until the substrate is held flat and registration error is within tolerance.",

    "What is the registration tolerance?": "0.70 mm is the acceptable misregistration limit.",

    "vacuum level": "5 for magnets, 10 for sheets",

    "What is the vacuum level for decals?": "between 3-5.",


    "What is the vacuum level for magnets?": "5.",

    "What is the vacuum level for foamboard?": "10.",

    "What is the vacuum level for lawnsign?": "10.",

    "What is the vacuum level for foamboards?": "10.",

    "What's the vacuum level for lawnsigns ?": "10.",

    "material slipping ": "Increase vacuum level",

    "Feeding issues ": "take the sheet out, and re-feed it. If the problem persists, call maintenance. ",

    "crooked sheet, skewed sheet": "Increase vacuum level, If the problem persists, call maintenance.",
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


def smart_search(question: str) -> str:
    question = correct_spelling(question)

    q = question.strip().lower()
    q = q.replace("problems","issues")
    q = q.replace("problem","issue")

    # Words that usually don't help identify the actual issue
    stop_words = {
        "what", "whats", "what's", "is", "the", "a", "an",
        "for", "to", "of", "do", "i", "have", "how",
        "can", "my", "me", "please", "tell", "about",
        "level", "setting","machine",
    }

    # Get important words from the user's question
    q_words = {
        word.strip(".,?!")
        for word in q.split()
        if word.strip(".,?!") not in stop_words
    }

    best_score = 0
    best_answer = None

    for stored_q, stored_a in QA_DATA.items():

        stored = stored_q.strip().lower()

        stored_words = {
            word.strip(".,?!")
            for word in stored.split()
            if word.strip(".,?!") not in stop_words
        }

        # Count important words that appear in both questions
        matching_words = q_words.intersection(stored_words)

        keyword_score = len(matching_words)

        # Fuzzy similarity
        fuzzy_score = fuzz.token_set_ratio(q, stored)

        # Combine keyword matching + fuzzy matching
        score = (keyword_score * 20) + fuzzy_score

        if score > best_score:
            best_score = score
            best_answer = stored_a

    if best_answer and best_score >= 45:
        return best_answer

    return "Sorry, I don't have an answer for that question yet."

def Rigid1():
    Search = st.text_input("Rigid 1",
key="Rigid1")

    if Search:
     answer = smart_search(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)
            