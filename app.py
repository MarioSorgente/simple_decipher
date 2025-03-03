import streamlit as st
import time

# Callback function to advance to the next card.
def advance_card():
    st.session_state.card_index += 1

# List of cards with alternating color designs.
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

# Initialize session state for card index and correctness flag.
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# We store per-card correctness using a key "correct_{card_index}"
def mark_correct(card_index):
    st.session_state[f"correct_{card_index}"] = True

def is_correct(card_index):
    return st.session_state.get(f"correct_{card_index}", False)

# Function to render a card with alternate colors and modern design.
def render_card(title, body, card_index):
    if card_index % 2 == 0:
        bg_color = "linear-gradient(135deg, #ffffff, #e6f0fa)"
        title_color = "#1d3557"
        text_color = "#457b9d"
    else:
        bg_color = "linear-gradient(135deg, #fefefe, #f2f2ff)"
        title_color = "#264653"
        text_color = "#2a9d8f"

    st.markdown(
        f"""
        <div style="
            background: {bg_color};
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 650px;
            margin: 40px auto;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            text-align: center;
            transition: all 0.3s ease-in-out;">
            <h2 style="color: {title_color}; margin-bottom: 20px;">{title}</h2>
            <p style="font-size: 20px; color: {text_color}; line-height: 1.5;">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def main():
    current = st.session_state.card_index

    if current >= len(cards):
        st.success("You've completed the puzzle!")
        return

    card = cards[current]

    # Welcome Card
    if card["type"] == "welcome":
        render_card(card["title"], card["text"], current)
        if st.button("Start", key="start", on_click=advance_card):
            time.sleep(0.3)

    # Question Cards
    elif card["type"] == "question":
        render_card(card["title"], card["question"], current)
        user_input = st.text_input("Your answer:", key=f"input_{current}", placeholder="Type your answer here")
        if st.button("Submit", key=f"submit_{current}"):
            try:
                user_answer = int(user_input)
            except ValueError:
                user_answer = None
            if user_answer is not None and user_answer == card["answer"]:
                mark_correct(current)
            else:
                st.error("Incorrect answer. Please try again.")
        # Only show Next button if the answer is correct.
        if is_correct(current):
            st.button("Next", key=f"next_{current}", on_click=advance_card)

    # Final Card
    elif card["type"] == "final":
        render_card(card["title"], card["text"], current)
        user_input = st.text_input("How many hints did you use?", key="hints_input", placeholder="Enter a number (0-3)")
        if st.button("Submit", key="final_submit"):
            try:
                hints_used_int = int(user_input)
            except ValueError:
                hints_used_int = None
            if hints_used_int is not None:
                if hints_used_int == 0:
                    st.info("Since you used zero hints, you get a coffee, a tiramisu, and a hug")
                elif hints_used_int == 1:
                    st.info("Since you used 1 hint, you get a tiramisu and a hug")
                elif hints_used_int == 2:
                    st.info("Since you used 2 hints, you get a coffee and a hug")
                elif hints_used_int >= 3:
                    st.info("Since you used 2 hints, you get a hug. Other prizes were a coffee and a tiramisu")
                mark_correct(current)
            else:
                st.error("Please enter a valid number between 0 and 3.")
        if is_correct(current):
            st.button("Next", key="final_next", on_click=advance_card)

if __name__ == "__main__":
    main()
