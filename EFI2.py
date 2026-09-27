from spellchecker import SpellChecker
from rapidfuzz import fuzz, process
import streamlit as st

spell = SpellChecker()

QA_DATA = { 
     "Banding":"Step 1: Perfrom a super purge \n\n"
          "Step 2: On the printer screen. Click maintenance.\n\n"
          "Step 3: Manually wet-wipe all printheads with the solution liquid provided for the machine.\n\n"
          "Step 4: Print nozzles check.\n\n"
          "If you still have issues, call your supervisor/pc.",
    "Ink Bleed":"Decrease the temperature by 5.",
    "Jog Forward/reverse Not Functioning":"Check unwinder, and rewinder buttons are on.\n\n"
    "Make sure that the direction of unwinder, and rewinder are correct.\n\n"
    "If you still having issues, restart the machine. ",
    "Unable To Start Printing":"Turn off all printheads by clicking on them indivisually untill it says 'Available for printing'\n\n"
    "If still having issues. Restart the machine.",
    "Pump Not Responding":"Turn off all printheads by clicking on them indivisually untill it says 'Available for printing'",
    "Drive Heater Fault":"Call maintenance.",
    "Missing Nozzles":"Step 1: Perfrom a super purge \n\n"
          "Step 2: On the printer screen. Click maintenance.\n\n"
          "Step 3: Manually wet-wipe all printheads with the solution liquid provided for the machine.\n\n"
          "Step 4: Print nozzles check.\n\n"
          "If you still have issues, call your supervisor/pc.",
    "Ink Smearing On First Off":"Decrease the temperature by 5.",
    "Error - Ink Inside Vacuum Line":"Call maintenance.",
    "Machine Not Ready":"Turn off all printheads by clicking on them indivisually untill it says 'Available for printing'",
    "Heat Plate Not Shutting Off Automatically":"Call maintenance.",
    "Rip In Blanket":"Call IT",
    "Burned Through Material":"Call your supervisor/PC",
    "Ink Smear":"Decrease the temperature by 5.",
    "Temperature Settings":"Refer to the temperature record provided on your machine.",
    "Loose Unplug":"Call maintenance.",
    "3 Spindle Latches Too Tight":"Call maintenance.",
    "Emergency E Stop Rope Will Not Reset":"Verify that both windows are fully closed and properly aligned with the sensors.\n\n"
    "If still having issues, call maintenance.",
    "oil spots / glycol drop":"Verify that the oil tray is not full.\n\n"
    "If it is, clean it or call maintenance to clean it."
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

def EFI2():
    Search = st.text_input("EFI 2",
key="EFI2")

    if Search:
     answer = smart_search(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)