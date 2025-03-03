import streamlit as st

def main():
    st.title("Solve the Equation to Get the Password")
    st.write("Solve each operation and input the correct result.")

    st.header("Group 1")
    t = st.number_input("T = 5×4", key="t", step=1)
    i = st.number_input("I = 3^2", key="i", step=1)

    st.header("Group 2")
    p1 = st.number_input("P = 8+8", key="p1", step=1)
    e1 = st.number_input("E = 10÷2", key="e1", step=1)
    n = st.number_input("N = 7+7", key="n", step=1)
    s1 = st.number_input("S = 20−1", key="s1", step=1)
    o = st.number_input("O = 5×3", key="o", step=1)

    st.header("Group 3")
    s2 = st.number_input("S = 18+1", key="s2", step=1)
    e2 = st.number_input("E = 50÷10", key="e2", step=1)
    m = st.number_input("M = 12+1", key="m", step=1)
    p2 = st.number_input("P = 8*2", key="p2", step=1)
    r = st.number_input("R = 20−2", key="r", step=1)
    e3 = st.number_input("E = 7-2", key="e3", step=1)

    if st.button("Submit Answers"):
        errors = []
        if t != 20:
            errors.append("T is incorrect")
        if i != 9:
            errors.append("I is incorrect")
        if p1 != 16:
            errors.append("P (Group 2) is incorrect")
        if e1 != 5:
            errors.append("E (Group 2) is incorrect")
        if n != 14:
            errors.append("N is incorrect")
        if s1 != 19:
            errors.append("S (Group 2) is incorrect")
        if o != 15:
            errors.append("O is incorrect")
        if s2 != 19:
            errors.append("S (Group 3) is incorrect")
        if e2 != 5:
            errors.append("E (Group 3) is incorrect")
        if m != 13:
            errors.append("M is incorrect")
        if p2 != 16:
            errors.append("P (Group 3) is incorrect")
        if r != 18:
            errors.append("R is incorrect")
        if e3 != 5:
            errors.append("E (Group 3, second) is incorrect")

        if errors:
            st.error("Some answers are incorrect: " + ", ".join(errors))
        else:
            st.success("All answers are correct!")
            st.subheader("Deciphered Message:")
            st.write("20.9")
            st.write("16.5.14.19.15")
            st.write("19.5.13.16.18.5")
            st.write("---")
            st.write("This is a message you have to decipher. You can use up to 2 hints:")
            st.write("• **Hint 1:** mingle letter and numbers")
            st.write("• **Hint 2:** consider a substitution")
            st.write("• **Hint 3:** consider the numerical position of the letters in the english alphabet")
            
            st.write("---")
            st.subheader("Prize Evaluation")
            hint_count = st.number_input("How many hints did you use?", min_value=0, max_value=3, step=1, key="hints")
            if st.button("Submit Hint Usage"):
                if hint_count == 0:
                    st.info("Since you used zero hints, you get a coffee, a tiramisu, and a hug")
                elif hint_count == 1:
                    st.info("Since you used 1 hint, you get a tiramisu and a hug")
                elif hint_count == 2:
                    st.info("Since you used 2 hints, you get a coffee and a hug")
                elif hint_count == 3:
                    st.info("Since you used 2 hints, you get a hug. Other prizes were a coffee and a tiramisu")

if __name__ == "__main__":
    main()
