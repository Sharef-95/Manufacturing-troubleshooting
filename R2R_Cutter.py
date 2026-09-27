from spellchecker import SpellChecker
from rapidfuzz import fuzz, process
import streamlit as st

spell = SpellChecker()

QA_DATA = { 
     "Tool Change Required",
        "Program Issue",
        "Laser Issue",
        "Belt Issue",
        "Blade Adjustment",
        "Blade Change",
        "New Blade or Adjust",
        "Vacuum Generator Error",
        "Not Cutting Through Banner",
        "Grab Bar Needs Adjustment",
        "Blade Broken or Missing",
        "Cutting Issue",
        "Safety Device Error",
        "Emergency Stop",
        "Excessive Wrinkles Causing Scrap",
        "Jam",
        "Blade Adjustment Required",
        "Not Advancing Banners",
        "Controller Error",
        "Belt Ripped",
        "Grab Bar Not Moving Material Forward",
        "Advance Bar Not Grabbing Banners",
        "Making Noise",
        "E-stop Cannot Clear",
        "Screw Fell Off Grab Bar",
        "Belt Not Advancing",
        "Split in Belt",
        "Light Curtain Issue",
        "Material Jammed Under Belt",
        "Belt Lifting",
        "Thumping Sound When Belt Advances",
        "Scrap Jammed",
        "Dancer Bar Not Rotating",
        "Cut Orientation Issue",
        "Blade Change Causing Tearing"
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

def R2R_Cutter():
    Search = st.text_input("R2R Cutter",
key="R2R_Cutter")

    if Search:
     answer = smart_search(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)