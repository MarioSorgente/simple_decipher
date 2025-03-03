import streamlit as st
import time

# Callback function to advance to the next card.
def advance_card():
    st.session_state.card_index += 1

# List of cards with alternating designs.
cards = [
    {
        "type": "welcome",
        "title": "Welcome Oceane",
        "text": "Solve the maths to get the password."
    },
    {
        "type": "question",
        "title": "Operation 1",
        "question": "5×4",
        "answer": 20
    },
    {
        "type": "question",
        "title": "Operation 2",
        "question": "3^2",
        "answer": 9
    },
    {
        "type": "question",
        "title": "Operation 3",
        "question": "8+8",
        "answer": 16
    },
    {
        "type": "question",
        "title": "Operation 4",
        "question": "10÷2",
        "answer": 5
    },
    {
        "type": "question",
        "title": "Operation 5",
        "question": "7+7",
        "answer": 14
    },
    {
        "type": "question",
        "title": "Operation 6",
        "question": "20−1",
        "answer": 19
    },
    {
        "type": "question",
        "title": "Operation 7",
        "question": "5×3",
        "answer": 15
    },
    {
        "type": "question",
        "title": "Operation 8",
        "question": "18+1",
        "answer": 19
    },
    {
        "type": "question",
        "title": "Operation 9",
        "question": "50÷10",
        "answer": 5
    },
    {
        "type": "question",
        "title": "Operation 10",
        "question": "Mario's day date of birth",
        "answer": 13
    },
    {
        "type": "question",
        "title": "Operation 11",
        "question": "8*2",
        "answer": 16
    },
    {
        "type": "question",
        "title": "Operation 12",
        "question": "20−2",
        "answer": 18
    },
    {
        "type": "question",
        "title": "Operation 13",
        "question": "7-2",
        "answer": 5
    },
    {
        "type": "final",
        "title": "Deciphered Message",
        "text": """20.9  
16.5.14.19.15  
19.5.13.16.18.5  

This is a message you have to decipher.

You can get hints if you need help. Click a hint button below to see a confirmation before revealing the hint."""
    }
]

# Initialize session state for card index and correctness flag.
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# Initialize hint confirmation state if not already set.
for h in ["hint1", "hint2", "hint3"]:
    if h not in st.session_state:
        st.session_state[h] = False

# We store per-card correctness using a key "correct_{card_index}"
def mark_correct(card_index):
    st.session_state[f"correct_{card_index}"] = True

def is_correct(card_index):
    return st.session_state.get(f"correct_{card_index}", False)

# Function to render a card with a burgundy-inspired modern design.
def render_card(title, body, card_index):
    burgundy = "#800020"
    # Use light, complementary backgrounds with burgundy accents.
    if card_index % 2 == 0:
        bg_color = "linear-gradient(135deg, #f8e1e7, #fdeff1)"
    else:
        bg_color = "linear-gradient(135deg, #fff0f5, #ffe6eb)"
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
            <h2 style="color: {burgundy}; margin-bottom: 20px;">{title}</h2>
            <p style="font-size: 20px; color: #330011; line-height: 1.5;">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_hint_button(hint_num, hint_text):
    button_key = f"hint_button_{hint_num}"
    confirm_key = f"hint_confirm_{hint_num}"
    # If the hint is already confirmed, show the hint.
    if st.session_state.get(f"hint{hint_num}", False):
        st.info(f"Hint {hint_num}: {hint_text}")
    else:
        # Show the button to get the hint.
        if st.button(f"Hint {hint_num}", key=button_key):
            with st.expander("Are you sure you want to get the hint?"):
                if st.button("Yes, show hint", key=confirm_key):
                    st.session_state[f"hint{hint_num}"] = True

# Container for the card.
card_container = st.empty()

def main():
    total_cards = len(cards)
    current = st.session_state.card_index

    # Display progress bar at the top.
    progress = (current + 1) / total_cards
    st.progress(progress)

    if current >= total_cards:
        st.success("You've completed the puzzle!")
        return

    card = cards[current]

    with card_container.container():
        # Welcome Card
        if card["type"] == "welcome":
            render_card(card["title"], card["text"], current)
            if st.button("Start", key="start", on_click=advance_card):
                time.sleep(0.3)

        # Question Cards
        elif card["type"] == "question":
            render_card(card["title"], card["question"], current)
            st.write("Your answer:")
            user_input = st.text_input("", key=f"input_{current}", placeholder="Type your answer here")
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

        # Final Card with hints and deciphered message.
        elif card["type"] == "final":
            render_card(card["title"], card["text"], current)
            st.write("Need a hint? Click the buttons below:")
            col1, col2, col3 = st.columns(3)
            with col1:
                show_hint_button(1, "Mingle letters and numbers.")
            with col2:
                show_hint_button(2, "Consider a substitution.")
            with col3:
                show_hint_button(3, "Look at the numerical position of letters in the English alphabet.")
            st.button("Next", key="final_next", on_click=advance_card)

if __name__ == "__main__":
    main()
