import streamlit as st

# Defining session state variables to track page, score, and username, linking them to session state
if "page" not in st.session_state:
    st.session_state.page = "home"

if "score" not in st.session_state:
    st.session_state.score = 0

if "name" not in st.session_state:
    st.session_state.name = ""

# Defining functions for each page of the quiz (There are 20 questions,1 home, and 1 results page, making 22)

# Defining the home page function, which will run the home page of the quiz, including a quiz description and start button


def home():
    st.markdown("<h1 style='text-align: center; color: black;'>Personal Project Trivia Quiz</h1>",
                unsafe_allow_html=True)
    st.write("### Welcome!")
    st.write(
        "**This website hosts a simple trivia quiz that I coded myself using Python**")
    st.session_state.name = st.text_input("Please enter your name")
    if st.button("Start Quiz"):
        if st.session_state.name == "":
            st.warning("Enter your name to proceed")
        else:
            st.session_state.page = "Question 1"
            st.rerun()

# Defining the function that will run the Question 1 page, including a proogress bar at the top, question text, buttons for answer options, and an incremental increase to the score variable for a correct answer


def Question_1():
    st.progress(0.05)
    st.markdown("<h2 style='text-align: center;'>Question 1</h2>",
                unsafe_allow_html=True)
    st.write(" #### What is the national flower of Japan?")
    if st.button("A. Lily", width=400):
        st.session_state.page = "Question 2"
        st.rerun()
    if st.button("B. Sunflower", width=400):
        st.session_state.page = "Question 2"
        st.rerun()
    if st.button("C. Cherry Blossom", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 2"
        st.rerun()
    if st.button("D. Peony", width=400):
        st.session_state.page = "Question 2"
        st.rerun()
    if st.button("E. Rose", width=400):
        st.session_state.page = "Question 2"
        st.rerun()

# Defining the function that will run the Question 2 page


def Question_2():
    st.progress(0.1)
    st.markdown("<h2 style='text-align: center;'>Question 2</h2>",
                unsafe_allow_html=True)
    st.write(" #### What is the best-selling book series of the 21st Century?")
    if st.button("A. Harry Potter", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 3"
        st.rerun()
    if st.button("B. Percy Jackson & the Olympians", width=400):
        st.session_state.page = "Question 3"
        st.rerun()
    if st.button("C. The Hunger Games", width=400):
        st.session_state.page = "Question 3"
        st.rerun()
    if st.button("D. Keeper of the Lost Cities", width=400):
        st.session_state.page = "Question 3"
        st.rerun()
    if st.button("E. Twilight", width=400):
        st.session_state.page = "Question 3"
        st.rerun()

# Defining the function that will run the Question 3 page


def Question_3():
    st.progress(0.15)
    st.markdown("<h2 style='text-align: center;'>Question 3</h2>",
                unsafe_allow_html=True)
    st.write(" #### Where are the Beatles from?")
    if st.button("A. London", width=400):
        st.session_state.page = "Question 4"
        st.rerun()
    if st.button("B. Liverpool", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 4"
        st.rerun()
    if st.button("C. Manchester", width=400):
        st.session_state.page = "Question 4"
        st.rerun()
    if st.button("D. Kent", width=400):
        st.session_state.page = "Question 4"
        st.rerun()
    if st.button("E. Brisbane", width=400):
        st.session_state.page = "Question 4"
        st.rerun()

# Defining the function that will run the Question 4 page


def Question_4():
    st.progress(0.20)
    st.markdown("<h2 style='text-align: center;'>Question 4</h2>",
                unsafe_allow_html=True)
    st.write(
        " #### Which of the following football teams are known as the “Red Devils”?")
    if st.button("A. Manchester City", width=400):
        st.session_state.page = "Question 5"
        st.rerun()
    if st.button("B. Liverpool", width=400):
        st.session_state.page = "Question 5"
        st.rerun()
    if st.button("C. Arsenal", width=400):
        st.session_state.page = "Question 5"
        st.rerun()
    if st.button("D. Everton", width=400):
        st.session_state.page = "Question 5"
        st.rerun()
    if st.button("E. Manchester United", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 5"
        st.rerun()

# Defining the function that will run the Question 5 page


def Question_5():
    st.progress(0.25)
    st.markdown("<h2 style='text-align: center;'>Question 5</h2>",
                unsafe_allow_html=True)
    st.write(" #### How many keys does a standard grand piano have?")
    if st.button("A. 72", width=400):
        st.session_state.page = "Question 6"
        st.rerun()
    if st.button("B. 90", width=400):
        st.session_state.page = "Question 6"
        st.rerun()
    if st.button("C. 64", width=400):
        st.session_state.page = "Question 6"
        st.rerun()
    if st.button("D. 88", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 6"
        st.rerun()
    if st.button("E. 94", width=400):
        st.session_state.page = "Question 6"
        st.rerun()

# Defining the function that will run the Question 6 page


def Question_6():
    st.progress(0.3)
    st.markdown("<h2 style='text-align: center;'>Question 6</h2>",
                unsafe_allow_html=True)
    st.write(" #### What was Pixar's first feature-length film?")
    if st.button("A. Cars", width=400):
        st.session_state.page = "Question 7"
        st.rerun()
    if st.button("B. Toy Story", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 7"
        st.rerun()
    if st.button("C. Wall-E", width=400):
        st.session_state.page = "Question 7"
        st.rerun()
    if st.button("D. Inside Out", width=400):
        st.session_state.page = "Question 7"
        st.rerun()
    if st.button("E. Up", width=400):
        st.session_state.page = "Question 7"
        st.rerun()

# Defining the function that will run the Question 7 page


def Question_7():
    st.progress(0.35)
    st.markdown("<h2 style='text-align: center;'>Question 7</h2>",
                unsafe_allow_html=True)
    st.write(" #### What is the capital of Canada?")
    if st.button("A. Auckland", width=400):
        st.session_state.page = "Question 8"
        st.rerun()
    if st.button("B. Quebec", width=400):
        st.session_state.page = "Question 8"
        st.rerun()
    if st.button("C. Toronto", width=400):
        st.session_state.page = "Question 8"
        st.rerun()
    if st.button("D. Montreal", width=400):
        st.session_state.page = "Question 8"
        st.rerun()
    if st.button("E. Ottawa", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 8"
        st.rerun()

# Defining the function that will run the Question 8 page


def Question_8():
    st.progress(0.4)
    st.markdown("<h2 style='text-align: center;'>Question 8</h2>",
                unsafe_allow_html=True)
    st.write(
        " #### What is the only planet in our solar system that rotates clockwise?")
    if st.button("A. Venus", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 9"
        st.rerun()
    if st.button("B. Mars", width=400):
        st.session_state.page = "Question 9"
        st.rerun()
    if st.button("C. Earth", width=400):
        st.session_state.page = "Question 9"
        st.rerun()
    if st.button("D. Jupiter", width=400):
        st.session_state.page = "Question 9"
        st.rerun()
    if st.button("E. Uranus", width=400):
        st.session_state.page = "Question 9"
        st.rerun()

# Defining the function that will run the Question 9 page


def Question_9():
    st.progress(0.45)
    st.markdown("<h2 style='text-align: center;'>Question 9</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which is the human body's largest organ?")
    if st.button("A. Lungs", width=400):
        st.session_state.page = "Question 10"
        st.rerun()
    if st.button("B. Brain", width=400):
        st.session_state.page = "Question 10"
        st.rerun()
    if st.button("C. Heart", width=400):
        st.session_state.page = "Question 10"
        st.rerun()
    if st.button("D. Skin", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 10"
        st.rerun()
    if st.button("E. Liver", width=400):
        st.session_state.page = "Question 10"
        st.rerun()

# Defining the function that will run the Question 10 page


def Question_10():
    st.progress(0.5)
    st.markdown("<h2 style='text-align: center;'>Question 10</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which of the following foods never perishes?")
    if st.button("A. Grapes", width=400):
        st.session_state.page = "Question 11"
        st.rerun()
    if st.button("B. Cheese", width=400):
        st.session_state.page = "Question 11"
        st.rerun()
    if st.button("C. Honey", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 11"
        st.rerun()
    if st.button("D. Pork", width=400):
        st.session_state.page = "Question 11"
        st.rerun()
    if st.button("E. Rice", width=400):
        st.session_state.page = "Question 11"
        st.rerun()

# Defining the function that will run the Question 11 page


def Question_11():
    st.progress(0.55)
    st.markdown("<h2 style='text-align: center;'>Question 11</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which animal was the first to be cloned?")
    if st.button("A. Sheep", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 12"
        st.rerun()
    if st.button("B. Mouse", width=400):
        st.session_state.page = "Question 12"
        st.rerun()
    if st.button("C. Hamster", width=400):
        st.session_state.page = "Question 12"
        st.rerun()
    if st.button("D. Duck", width=400):
        st.session_state.page = "Question 12"
        st.rerun()
    if st.button("E. Dog", width=400):
        st.session_state.page = "Question 12"
        st.rerun()

# Defining the function that will run the Question 12 page


def Question_12():
    st.progress(0.6)
    st.markdown("<h2 style='text-align: center;'>Question 12</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which guitarist notably performed on Michael Jackson's Beat It?")
    if st.button("A. Slash", width=400):
        st.session_state.page = "Question 13"
        st.rerun()
    if st.button("B. Jimi Hendrix", width=400):
        st.session_state.page = "Question 13"
        st.rerun()
    if st.button("C. George Harrison", width=400):
        st.session_state.page = "Question 13"
        st.rerun()
    if st.button("D. Eric Clapton", width=400):
        st.session_state.page = "Question 13"
        st.rerun()
    if st.button("E. Eddie van Halen", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 13"
        st.rerun()

# Defining the function that will run the Question 13 page


def Question_13():
    st.progress(0.65)
    st.markdown("<h2 style='text-align: center;'>Question 13</h2>",
                unsafe_allow_html=True)
    st.write(" #### How many points does the Star of David have?")
    if st.button("A. 5", width=400):
        st.session_state.page = "Question 14"
        st.rerun()
    if st.button("B. 6", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 14"
        st.rerun()
    if st.button("C. 7", width=400):
        st.session_state.page = "Question 14"
        st.rerun()
    if st.button("D. 8", width=400):
        st.session_state.page = "Question 14"
        st.rerun()
    if st.button("E. None", width=400):
        st.session_state.page = "Question 14"
        st.rerun()

# Defining the function that will run the Question 14 page


def Question_14():
    st.progress(0.70)
    st.markdown("<h2 style='text-align: center;'>Question 14</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which of the following zodiac signs is a water sign?")
    if st.button("A. Taurus", width=400):
        st.session_state.page = "Question 15"
        st.rerun()
    if st.button("B. Virgo", width=400):
        st.session_state.page = "Question 15"
        st.rerun()
    if st.button("C. Libra", width=400):
        st.session_state.page = "Question 15"
        st.rerun()
    if st.button("D. Cancer", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 15"
        st.rerun()
    if st.button("E. Aries", width=400):
        st.session_state.page = "Question 15"
        st.rerun()

# Defining the function that will run the Question 15 page


def Question_15():
    st.progress(0.75)
    st.markdown("<h2 style='text-align: center;'>Question 15</h2>",
                unsafe_allow_html=True)
    st.write(" #### The first iPhone was released in which of the following years?")
    if st.button("A. 2008", width=400):
        st.session_state.page = "Question 16"
        st.rerun()
    if st.button("B. 2005", width=400):
        st.session_state.page = "Question 16"
        st.rerun()
    if st.button("C. 2007", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 16"
        st.rerun()
    if st.button("D. 2003", width=400):
        st.session_state.page = "Question 16"
        st.rerun()
    if st.button("E. 2004", width=400):
        st.session_state.page = "Question 16"
        st.rerun()

# Defining the function that will run the Question 16 page


def Question_16():
    st.progress(0.8)
    st.markdown("<h2 style='text-align: center;'>Question 16</h2>",
                unsafe_allow_html=True)
    st.write(
        " #### Which organelle is commonly regarded as the powerhouse of the cell?")
    if st.button("A. Cell Membrane", width=400):
        st.session_state.page = "Question 17"
        st.rerun()
    if st.button("B. Cytoplasm", width=400):
        st.session_state.page = "Question 17"
        st.rerun()
    if st.button("C. Lysosome", width=400):
        st.session_state.page = "Question 17"
        st.rerun()
    if st.button("D. Nucleus", width=400):
        st.session_state.page = "Question 17"
        st.rerun()
    if st.button("E. Mitochondria", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 17"
        st.rerun()

# Defining the function that will run the Question 17 page


def Question_17():
    st.progress(0.85)
    st.markdown("<h2 style='text-align: center;'>Question 17</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which actor plays Ken in the 2023 movie Barbie?")
    if st.button("A. Ryan Gosling", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 18"
        st.rerun()
    if st.button("B. Liam Neeson", width=400):
        st.session_state.page = "Question 18"
        st.rerun()
    if st.button("C. Ryan Reynolds", width=400):
        st.session_state.page = "Question 18"
        st.rerun()
    if st.button("D. Timothee Chalamet", width=400):
        st.session_state.page = "Question 18"
        st.rerun()
    if st.button("E. Adam Sandler", width=400):
        st.session_state.page = "Question 18"
        st.rerun()

# Defining the function that will run the Question 18 page


def Question_18():
    st.progress(0.9)
    st.markdown("<h2 style='text-align: center;'>Question 18</h2>",
                unsafe_allow_html=True)
    st.write(" #### Who wrote To Kill a Mockingbird?")
    if st.button("A. Abraham Lincoln", width=400):
        st.session_state.page = "Question 19"
        st.rerun()
    if st.button("B. Harper Lee", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 19"
        st.rerun()
    if st.button("C. F. Scott Fitzgerald", width=400):
        st.session_state.page = "Question 19"
        st.rerun()
    if st.button("D. Jane Austen", width=400):
        st.session_state.page = "Question 19"
        st.rerun()
    if st.button("E. William Shakespeare", width=400):
        st.session_state.page = "Question 19"
        st.rerun()

# Defining the function that will run the Question 19 page


def Question_19():
    st.progress(0.95)
    st.markdown("<h2 style='text-align: center;'>Question 19</h2>",
                unsafe_allow_html=True)
    st.write(
        " #### Which of the following conflicts was resolved with the Treaty of Versailles?")
    if st.button("A. American Civil War", width=400):
        st.session_state.page = "Question 20"
        st.rerun()
    if st.button("B. Revolutionary War", width=400):
        st.session_state.page = "Question 20"
        st.rerun()
    if st.button("C. World War II", width=400):
        st.session_state.page = "Question 20"
        st.rerun()
    if st.button("D. World War I", width=400):
        st.session_state.score += 1
        st.session_state.page = "Question 20"
        st.rerun()
    if st.button("E. Korean War", width=400):
        st.session_state.page = "Question 20"
        st.rerun()

# Defining the function that will run the Question 20 page


def Question_20():
    st.progress(1.0)
    st.markdown("<h2 style='text-align: center;'>Question 20</h2>",
                unsafe_allow_html=True)
    st.write(" #### Which is the world's most populated city?")
    if st.button("A. Jakarta, Indonesia", width=400):
        st.session_state.score += 1
        st.session_state.page = "results"
        st.rerun()
    if st.button("B. Paris, France", width=400):
        st.session_state.page = "results"
        st.rerun()
    if st.button("C. Tokyo, Japan", width=400):
        st.session_state.page = "results"
        st.rerun()
    if st.button("D. New York, USA", width=400):
        st.session_state.page = "results"
        st.rerun()
    if st.button("E. Seoul, Korea", width=400):
        st.session_state.page = "results"
        st.rerun()

# Defining the function that will run the results page, including a score display, personalized messages based on score, and a restart button


def results():
    st.markdown("<h1 style='text-align: center;'>Quiz Results</h1>",
                unsafe_allow_html=True)
    st.write(
        f"### Congratulations, {st.session_state.name}! You finished the quiz.")
    st.write(f"### You got {st.session_state.score} questions out of 20!")
    st.write(f"### That makes your score {st.session_state.score * 5}%!")
    if st.session_state.score == 20:
        st.write("#### Perfect score! Wow!")
    elif st.session_state.score >= 15:
        st.write("#### Amazing job!")
    elif st.session_state.score >= 10:
        st.write("#### Good effort!")
    else:
        st.write("#### Better luck next time! Keep studying!")
    if st.button("Restart Quiz"):
        st.session_state.page = "home"
        st.session_state.score = 0
        st.rerun()


# Using session state to run different page functions based on the current page variable
if st.session_state.page == "home":
    home()
elif st.session_state.page == "Question 1":
    Question_1()
elif st.session_state.page == "Question 2":
    Question_2()
elif st.session_state.page == "Question 3":
    Question_3()
elif st.session_state.page == "Question 4":
    Question_4()
elif st.session_state.page == "Question 5":
    Question_5()
elif st.session_state.page == "Question 6":
    Question_6()
elif st.session_state.page == "Question 7":
    Question_7()
elif st.session_state.page == "Question 8":
    Question_8()
elif st.session_state.page == "Question 9":
    Question_9()
elif st.session_state.page == "Question 10":
    Question_10()
elif st.session_state.page == "Question 11":
    Question_11()
elif st.session_state.page == "Question 12":
    Question_12()
elif st.session_state.page == "Question 13":
    Question_13()
elif st.session_state.page == "Question 14":
    Question_14()
elif st.session_state.page == "Question 15":
    Question_15()
elif st.session_state.page == "Question 16":
    Question_16()
elif st.session_state.page == "Question 17":
    Question_17()
elif st.session_state.page == "Question 18":
    Question_18()
elif st.session_state.page == "Question 19":
    Question_19()
elif st.session_state.page == "Question 20":
    Question_20()
elif st.session_state.page == "results":
    results()
