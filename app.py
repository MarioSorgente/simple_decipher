import streamlit as st
import time

# Helper function for re-running the app safely
def safe_rerun():
    try:
        st.experimental_rerun()
    except AttributeError:
        pass  # In case experimental_rerun is not available

# List of cards, each card is either a welcome, question, or final card.
cards = [
    {
        "type": "welcome",
        "title": "Welcome Oceane",
        "text": "Solve the equation to get the password."
    },
    {
        "type": "question",
        "title": "Operation 1",
        "question": "T = 5×4",
        "answer": 20
    },
    {
        "type": "question",
        "title": "Operation 2",
        "question": "I = 3^2",
        "answer": 9
    },
    {
        "type": "question",
        "title": "Operation 3",
        "question": "P = 8+8",
        "answer": 16
    },
    {
        "type": "question",
        "title": "Operation 4",
        "question": "E = 10÷2",
        "answer": 5
    },
    {
        "type": "question",
        "title": "Operation 5",
        "question": "N = 7+7",
        "answer": 14
    },
    {
        "type": "question",
        "title": "Operation 6",
        "question": "S = 20−1",
        "answer": 19
    },
    {
        "type": "question",
        "title": "Operation 7",
        "question": "O = 5×3",
        "answer": 15
    },
    {
        "type": "question",
        "title": "Operation 8",
        "question": "S = 18+1",
        "answer": 19
    },
    {
        "type": "question",
        "title": "Operation 9",
        "question": "E = 50÷10",
        "answer": 5
    },
    {
        "type": "question",
        "title": "Operation 10",
        "question": "M = 12+1",
        "answer": 13
    },
    {
        "type": "question",
        "title": "Operation 11",
        "question": "P = 8*2",
        "answer": 16
    },
    {
        "type": "question",
        "title": "Operation 12",
        "question": "R = 20−2",
        "answer": 18
    },
    {
        "type": "question",
        "title": "Operation 13",
        "question": "E = 7-2",
        "answer": 5
    },
    {
        "type": "final",
        "title": "Deciphered Message",
        "text": """20.9  
16.5.14.19.15  
19.5.13.16.18.5  

This is a message you have to decipher. You can use up to 2 hints:
- **Hint 1:** mingle letter and numbers  
- **Hint 2:** consider a substitution  
- **Hint 3:** consider the numerical position of the letters in the english alphabet

Now, enter the number of hints you used:"""
    }
]

# Initialize session state for card index.
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# Function to render a card with modern, colorful design
def render_card(title, body):
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ffffff, #e6f0fa);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 650px;
            margin: 40px auto;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            text-align: center;">
            <h2 style="color: #1d3557; margin-bottom: 20px;">{title}</h2>
            <p style="font-size: 20px; color: #457b9d; line-height: 1.5;">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main app flow: show one card at a time.
def main():
    current = st.session_state.card_index

    # If all cards are done, show a completion message.
    if current >= len(cards):
        st.success("You've completed the puzzle!")
        return

    card = cards[current]

    if card["type"] == "welcome":
        render_card(card["title"], card["text"])
        if st.button("Next", key="welcome_next"):
            st.session_state.card_index += 1
            safe_rerun()

    elif card["type"] == "question":
        render_card(card["title"], card["question"])
        user_answer = st.number_input("Your answer:", key=f"input_{current}", step=1)
        if st.button("Submit Answer", key=f"submit_{current}"):
            if user_answer == card["answer"]:
                # Immediately go to next card if answer is correct.
                st.session_state.card_index += 1
                safe_rerun()
            else:
                st.error("Incorrect answer. Please try again.")

    elif card["type"] == "final":
        render_card(card["title"], card["text"])
        hints_used = st.number_input("How many hints did you use?", min_value=0, max_value=3, step=1, key="hints")
        if st.button("Submit Hint Usage", key="hints_submit"):
            if hints_used == 0:
                st.info("Since you used zero hints, you get a coffee, a tiramisu, and a hug")
            elif hints_used == 1:
                st.info("Since you used 1 hint, you get a tiramisu and a hug")
            elif hints_used == 2:
                st.info("Since you used 2 hints, you get a coffee and a hug")
            elif hints_used == 3:
                st.info("Since you used 2 hints, you get a hug. Other prizes were a coffee and a tiramisu")
            st.session_state.card_index += 1
            safe_rerun()

if __name__ == "__main__":
    main()
