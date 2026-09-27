from spellchecker import SpellChecker
from rapidfuzz import fuzz, process
import streamlit as st

spell = SpellChecker()

QA_DATA = { 
     "Tool Change Required":"Call maintenance.",
        "Program Issue":"Restart cut program, and cut server.",
        "Belt Issue":"Call maintenance.",
        "Blade Adjustment":"Call maintenance.",
        "Blade Change":"Call maintenance.",
        "New Blade or Adjust":"Call maintenance.",
        "Vacuum Generator Error":"Clear the error and try again\n\n"
        "If the issue persits, call maintenance.",
        "Not Cutting Through Banner":"Ask for blade adjustment/change.",
        "Grab Bar Needs Adjustment":"Call maintenance.",
        "Blade Broken or Missing":"Call maintenance.",
        "Cutting Issue":"Before starting the Cut File.\n\n"
        "Ensure the material is flat and free of wrinkles.",
        "Safety Device Error":"Call maintenance.",
        "Emergency Stop / E-stop":"Locate all Emergency stop buttons.\n\n"
        "Ensure that they are released.\n\n"
        "If you still having issues, call maintenance.",
        "Excessive Wrinkles Causing Scrap":"On the cutters screen, increase the vacuum level to 10"
        
        "Not Advancing Banners",
        "Controller Error":"Clear the error.\n\n"
        "If it comes back, all maintenance",
        "Belt Ripped":"Call maintenance.",
        "Grab Bar Not Moving Material Forward":"Call maintenance.",
        "Advance Bar Not Grabbing Banners":"Call maintenance.",
        "Making Noise":"Call maintenance.",
        "E-stop Cannot Clear":"Call maintenance.",
        "Screw Fell Off Grab Bar":"Call your supervisor/PC.",
        "Belt Not Advancing":"Call maintenance.",
        "Split in Belt":"Call maintenance.",
        "Light Curtain Issue":"Verify that there is nothing blocking light curtain.\n\n"
        "If not, call maintenance.",
        "Material Jammed Under Belt":"Call maintenance.",
        "Belt Lifting":"Call maintenance.",
        "Thumping Sound When Belt Advances":"Call maintenance.",
        "Scrap Jammed":"Call maintenance.",
        "Dancer Bar Not Rotating":"Call maintenance.",
        
        "Blade Change Causing Tearing":"Call maintenance.",
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