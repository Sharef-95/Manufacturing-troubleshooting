from spellchecker import SpellChecker
from rapidfuzz import fuzz, process
import streamlit as st

spell = SpellChecker()

QA_DATA = { 
    "Power Supply Error":" Call maintenance.",
    "Not Cutting Through Material":"initilize cutting tool",
    "Aux Drive 0 Not Ready":"1. Locate Aux drive switch at the back of the machine.\n\n"
      "2. If the switch is set to AUTO, move it to the ON position.\n\n"
      "3. If the switch is already ON, return it to the AUTO position.\n\n"
      "If the issue persists, restart the machine and check again.",
    "Laser Issue":"Call maintenance.",
    "Cutting Issues":"",
    "Vacuum Hose Broken":"Call maintenance.",
    "Ext. Material Handling 1 Not Ready Error":"Call maintenance.",
    "Light Curtain Triggered":"Check under the machine for fabric material blocking the light curtain.\n\n"
      "If there nothing blocking it, call maintenance.",
    "Program Issue":"Restart the cutting program.",
    "Safety Module Error":"Restart the machine.",
    "Material Not Advancing":"Make sure that Aux Drive 0 is ready.",
    "Camera Not Turning On":"Disconnet the green usb that connected to your computer, and re-connect it.",
    "Holder Bar Not Coming Down":"Make sure that there is no error on your machine screen.",
    "Controller Index Error 00000004":"Clear the error.\n\n"
      "Call maintenance if it comes back.",
    "Not Cutting Through Well":"Call maintenance.",
    "Not Cutting All The Way Through":"Call maintenance.",
    "Blade Adjustment":"Call maintenance.",
    "Aux Driver Not Ready":"1. Locate Aux drive switch at the back of the machine.\n\n"
      "2. If the switch is set to AUTO, move it to the ON position.\n\n"
      "3. If the switch is already ON, return it to the AUTO position.\n\n"
      "If the issue persists, restart the machine and check again.",
    "Bar Not Advancing Material":"Verify that the black holding bar is locked.\n\n",
    "Frozen":"Exit the cutting app.\n\n"
    "If it's still frozen, press alt + F4 on your keyboard.",
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

def Eurolaser():
    Search = st.text_input("Eurolaser",
key="Eurolaser")

    if Search:
     answer = smart_search(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)