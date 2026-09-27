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
        "E-stop Pressed":"On the printer screen. Check which E-stop is pressed, and release it.",
        "Registration on Blankets":"Increase the tension for the back spindle by 0.1.\n\n"
            "If you still having registraion issues, keep increasing tension untill it's fixed.",
        "Machine Not Running":"Step 1: Close printing app, and one app.\n\n"
          "Step 2: On The machine screen. Turn off winder, unwinder, exhaust, and heat plate.\n\n"
          "Step 3: Turn off all printheads by pressing on each one indivisually.\n\n"
          "Step 4: On the printer screen. Change the media to different media.\n\n"
          "Step 5: Turn all printheads back on.\n\n"
          "Step 6: Turn winder, unwinder, exhaust, and heat plate back on.\n\n"
          "Step 7: Start a nozzle test.\n\n"
          "Step 8: Return to required media.\n\n"
          "If machine is still not responding: call maintenance.",
        "Line on Print":"Call maintenance.",
        "Ink Leaking":"Call maintenance.",
        "Paper Fault Error":"On the machine screen. Click Home.\n\n"
          "If the machine is not responding, open operator side window.\n\n"
          "Manually move printheads.\n\n"
          "Close window, and try again.\n\n"
          "if you still have issue. Call maintenance.",
        "Missing Nozzles":"Step 1: Perfrom a super purge \n\n"
          "Step 2: On the printer screen. Click maintenance.\n\n"
          "Step 3: Manually wet-wipe all printheads with the solution liquid provided for the machine.\n\n"
          "Step 4: Print nozzles check.\n\n"
          "If you still have issues, call your supervisor/pc.",
        "E-stop Pressed":"On the printer screen. Check which E-stop is pressed, and release it.",

        "Exhaust Hose Leaking":"Call maintenance.",
        "Colour Fade - Right Side":"Increase right side temp. by 5.",
        "Wrinkling on Substrates":"Decrease unwinder tension by 0.1.\n\n"
          "Increase winder tension by 0.1",
        "Ink Spots":"Replace felt pad.",
        "Encoder Error":"Call maintenance.",
        "Yellow Ink Leaking":"Call maintenance.",
        
        "Ink Tank Leaking":"Call maintenance.",
        "Unable to Purge":"",
        "Back Locking Mechanism Loose":"Call maintenance.",
        "Colour Fade - Left Side":"Increase left side temp. by 5.",
        "Cannot Recover Black Nozzles":"Step 1: Perfrom a super purge \n\n"
        "Step 2: On the printer screen. Click maintenance.\n\n"
        "Step 3: Manually wet-wipe all printheads with the solution liquid provided for the machine.\n\n"
        "Step 4: Print nozzles check.\n\n"
        "If you still have issues, call your supervisor/pc.",
        "Banding in First Off":"Step 1: Perfrom a super purge \n\n"
        "Step 2: On the printer screen. Click maintenance.\n\n"
        "Step 3: Manually wet-wipe all printheads with the solution liquid provided for the machine.\n\n"
        "Step 4: Print nozzles check.\n\n"
        "If you still have issues, call your supervisor/pc.",
        "Missing Magenta Nozzles":"Step 1: Perfrom a super purge \n\n"
        "Step 2: On the printer screen. Click maintenance.\n\n"
        "Step 3: Manually wet-wipe all printheads with the solution liquid provided for the machine.\n\n"
        "Step 4: Print nozzles check.\n\n"
        "If you still have issues, call your supervisor/pc.",
        
        "Balance Bar Adjustment":"Call maintenance.",
        "Cyan Ink Drip":"Call maintenance.",
        "Ink Bleeding Into White":"",
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

def EFI1():
    Search = st.text_input("EFI1",
key="EFI1")

    if Search:
     answer = smart_search(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)