
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie




#https://www.webfx.com/tools/emoji-cheat-sheet/  ----> for easy emojis

st.set_page_config(page_title="My Portfolio", page_icon=":woman_student:", layout="wide")

st.markdown("""
<style>
/* Page background */
.stApp {
    background-color: #FDF6F0;  /* Soft pastel cream */
    color: #000000;  /* Black text for readability */
}

/* Titles and subtitles */
.title-text {
    color: #FF6B6B;  /* Warm coral accent for main title */
}

.subtitle-text {
    color: #333333;  /* Dark gray for subtitle */
}

/* Headings inside containers (Experience, Projects, etc.) */
h2, h3, h4 {
    color: #FF6B6B; /* Accent color for section headings */
}

/* Links */
a {
    color: #4B7BEC; /* Pastel blue links */
}
a:hover {
    color: #FF6B6B; /* Hover accent */
}

/* Skills logos section */
.skills-title {
    color: #FF6B6B; /* Accent color for skills title */
}

/* LinkedIn button */
.linkedin-btn {
    background: linear-gradient(90deg, #FFA69E, #FF6B6B); /* Soft pastel gradient */
    color: #FFFFFF;
}
.linkedin-btn:hover {
    background: linear-gradient(90deg, #FF6B6B, #FFA69E);
}

/* General text */
.stMarkdown, p, li {
    color: #000000; /* Black text for readability */
}

/* Card/Container styling (optional subtle shadow for readability) */
.stContainer {
    background-color: #FFF9F5; /* Slightly lighter than main background */
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




#loading assets i.e emojis

lottie_coding = load_lottieurl("https://lottie.host/2134b202-e89f-452c-bf66-30c6def49e47/3i8RzqZ9zd.json")
lottie_coding2= load_lottieurl("https://lottie.host/1d1441cd-8267-44bc-a40c-eff3b7498321/Z2XOOYQywO.json")
lottie_coding3= load_lottieurl("https://lottie.host/56167e44-4ddd-41f5-9a28-ab92e3923c83/yJgcgBEo6N.json")

img_im1= Image.open("webpage/Images/img_one.webp")
img_im2= Image.open("webpage/Images/img_two.jpeg")
img_im3= Image.open("webpage/Images/img_three.jpeg")
img_im4= Image.open("webpage/Images/img_four.jpg")
img_im5= Image.open("webpage/Images/img_five.jpg")
img_im6= Image.open("webpage/Images/img_six.jpg")
img_im7= Image.open("webpage/Images/profile.jpg")
# --- Header Section ---
with st.container():
    col1, col2 = st.columns([3, 1])  # wider text column, smaller image column

    with col1:
        st.markdown(
            """
            <style>
                /* --- Title Animation --- */
                .title-text {
                    font-size: 45px;
                    font-weight: bold;
                    white-space: nowrap;
                    overflow: hidden;
                    border-right: 3px solid #ff4b4b;
                    width: 0;
                    animation: typing 4s steps(40, end) forwards, blink 0.75s;
                    margin-bottom: 5px;  /* reduced gap below title */
                }
                @keyframes typing {
                    from { width: 0 }
                    to { width: 100% }
                }
                @keyframes blink {
                    from, to { border-color: transparent }
                    50% { border-color: #ff4b4b; }
                }
                .subtitle-text {
                    font-size: 24px;
                    opacity: 0;
                    animation: fadeIn 2s ease-in forwards;
                    animation-delay: 4.2s;
                    margin-top: 5px;  /* reduced gap above subtitle */
                    line-height: 1.3;  /* tighter line spacing */
                }
                @keyframes fadeIn {
                    from { opacity: 0 }
                    to { opacity: 1 }
                }

                /* --- LinkedIn Button --- */
                .linkedin-btn {
                     display: inline-block;
                       margin-top: 15px;              /* less gap above button */
                      padding: 8px 18px;             /* smaller & neat */
                       font-size: 15px;               /* slightly smaller text */
                           font-weight: 600;              /* medium bold, aesthetic */
                      text-decoration: none !important; /* remove underline */
                      color: #060608;                /* black text for readability */

                     border-radius: 20px;           /* softer curve */
                      background: linear-gradient(90deg, #A1FFCE, #FAFFD1); /* pastel gradient */

                     box-shadow: 0px 2px 6px rgba(0,0,0,0.2); /* lighter shadow */
                      transition: all 0.25s ease;
                    }

                .linkedin-btn:hover {
                   transform: scale(1.05);        /* gentle zoom */
                     box-shadow: 0px 4px 10px rgba(0, 119, 181, 0.4); /* soft hover glow */
                    }                  
            </style>

            <div>
                <h1 class="title-text">Heyy Guyss, I'm Parakh Prakash !!</h1>
                <h3 class="subtitle-text">IT Engineer | Tech Enthusiast | Creative Problem Solver</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Intro Text (Bigger Font, Reduced Gaps) ---
st.markdown(
    """
    <style>
        .skills-title {
            font-size: 26px;
            font-weight: bold;
            margin: 5px auto 5px auto;  /* small top/bottom margin, centered */
            text-align: center;         /* center the title */
        }
        .skills-logos {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;    /* center the logos */
            gap: 15px;
            margin-top: 5px;            /* shift section a little up */
            margin-bottom: 10px;
        }
        .skills-logos img {
            width: 55px;
            height: 55px;
            object-fit: contain;
            transition: transform 0.3s ease;
        }
        .skills-logos img:hover {
            transform: scale(1.15);
        }
    </style>

    <div class="skills-title"> Skills & Tools</div>
    <div class="skills-logos">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" title="Python">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" alt="SQL" title="SQL">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" alt="ML" title="Machine Learning">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML" title="HTML">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS" title="CSS">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" title="JavaScript">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap" title="Bootstrap">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" alt="Flask" title="Flask">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" title="Git">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" title="GitHub">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" alt="Figma" title="Figma">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" alt="C++" title="C++">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://www.linkedin.com/in/parakh-prakash-451440215" target="_blank" class="linkedin-btn">
            📌 Find me on LinkedIn
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
with col2:
    st.image(img_im7, caption="That's me!", width=220)


# --- WHAT I DO ---
# with st.container():
    # st.write("---")
    # left_column, right_column = st.columns(2)
    # with left_column:
    #     st.header("💻 What I Do")
    #     st.write("----")
    #     st.write(
    #         """
            
    #         ✨ I love turning ideas into reality through code, creativity, and problem solving.  
    #         """
    #     )
    #     st.write("[🔗 Connect with me on LinkedIn >](https://www.linkedin.com/in/parakh-prakash-451440215)")
    # with right_column:  
        # st_lottie(lottie_coding, height=300, key="coding1")


# --- INTERNSHIPS ---
with st.container():
    st.write("---")
    st.header("🛠️ Experience")
    st.write("Some amazing experiences that shaped my journey 🌟")

    # Internship 1
    image_column, text_column = st.columns((1,2))
    with image_column:
        st_lottie(lottie_coding2, height=300, key="coding2")   # Replace with your image
    with text_column:
        st.subheader("🎥 Video Data Annotation Intern - V2 Solutions (Feb – Apr 2025)")
        st.write(
            """
            - Worked on **Adobe’s AI training project** by analyzing and describing stock videos.  
            - Enhanced my **attention to detail, visual interpretation, and technical writing**.  
            - Key Skills: Video Annotation, Adobe AI Training, Descriptive Writing, Stock Video Analysis.  
            """
        )

        st.subheader("🐍 Python Programming Intern - CodSoft (Jul – Aug 2023)")
        st.write(
            """
            - Built **3 projects**: Calculator, Password Generator, and To-Do List in Python.  
            - Strengthened my **Python basics** and used GitHub for version control.  
            - Key Skills: Python, GitHub, Coding.  
            """
        )

        st.subheader("🛡️ Cyber Security Intern - SIES GST (Dec 2022 – Feb 2023)")
        st.write(
            """
            - Explored **vulnerability scanners** like Snyk, Grype, and Syft on Docker images.  
            - Learned about **Docker, Containerization, and Cyber Security tools**.  
            - Key Skills: Cyber Security, Docker, GitHub.  
            """
        )

    # Internship 2
    # image_column, text_column = st.columns((1,2))
    # with image_column:
    #     st_lottie(lottie_coding, height=300, key="coding3")
    # with text_column:
    #     st.subheader("🐍 Python Programming Intern - CodSoft (Jul – Aug 2023)")
    #     st.write(
    #         """
    #         - Built **3 projects**: Calculator, Password Generator, and To-Do List in Python.  
    #         - Strengthened my **Python basics** and used GitHub for version control.  
    #         - Key Skills: Python, GitHub, Coding.  
    #         """
    #     )

    # Internship 3
    # image_column, text_column = st.columns((1,2))
    # with image_column:
    #     st_lottie(lottie_coding, height=300, key="coding4")
    # with text_column:
    #     st.subheader("🛡️ Cyber Security Intern - SIES GST (Dec 2022 – Feb 2023)")
    #     st.write(
    #         """
    #         - Explored **vulnerability scanners** like Snyk, Grype, and Syft on Docker images.  
    #         - Learned about **Docker, Containerization, and Cyber Security tools**.  
    #         - Key Skills: Cyber Security, Docker, GitHub.  
    #         """
    #     )


# --- PROJECTS ---
with st.container():
    st.write("---")
    st.header("📂 Projects")
    st.write("Cool projects I’ve built along the way 🎯")

    # Left text, right animation
    text_column, image_column = st.columns((2,1))
    with text_column:

        st.subheader("🤖 Deep-fake Detection using Machine Learning")
        st.write(
        """
        Key Skills: Machine Learning, Python, Flask, Colab  
        ◦ Developed a deepfake media detector using multiple ML models, seamlessly integrated with a **Flutter-based application** for efficient detection of fake images and videos.  
        """
        )

        st.subheader("🗺️ AI-Trip Planner using ML")
        st.write(
        """
        Link: [GitHub Repo](https://git.new/mhngSFm)  
        Key Skills: Google Colab, GitHub, ML, Python  
        ◦ Created and presented a **prize-winning mini project**, a trip planner app hosted on **render.com**.  
        ◦ Effectively plans and organizes trips based on user preferences, showcasing adaptability and innovation.  
        """
        )

        st.subheader("📊 Interactive Data Visualization Web App")
        st.write(
        """
        Link: [GitHub Repo](https://git.new/k9jOFZw)  
        Key Skills: JavaScript, HTML5 Canvas, CSS, Data Aggregation, Animation  
        ◦ Developed an **interactive visualization tool** for CSV/JSON datasets with dynamic bar & pie charts,  
        aggregation options, graphics rendering, and smooth animations for effective data storytelling.  
        """
        )

        st.subheader("🌐 Portfolio Web Application")
        st.write(
        """
        Key Skills: Python, Streamlit, Streamlit-Lottie, PIL  
        ◦ Built an **interactive personal portfolio web app** with animations and responsive UI to showcase projects, internships, research, and achievements.  
        """
        )

        st.subheader("🎨 Detecto App Wireframing - Figma")
        st.write(
        """
        Link: [Figma Design](refer.is/1tu6crof)  
        Key Skills: Figma, Interactive UI, Prototyping  
        ◦ Designed and prototyped **‘Detecto’**, a computer vision application for detecting objects in images/videos.  
        ◦ Created intuitive interfaces and interactive flows in Figma for a seamless user experience.  
        """
        )
  

    with image_column:
        st_lottie(lottie_coding3, height=300, key="coding5")


    # Project 2
    # text_column, image_column = st.columns((2,1))
    # with text_column:
    #     st.subheader("🗺️ AI Trip Planner using ML")
    #     st.write(
    #     """
    #     - Created a **trip planner app** that organizes trips based on user preferences.  
    #     - Hosted on **render.com**, this project even won a prize 🏆.  
    #     - Key Skills: ML, Python, Google Colab, GitHub.  
    #     """
    #     )
    # with image_column:
    #     st_lottie(lottie_coding, height=300, key="coding6")

    # Project 3
    # text_column, image_column = st.columns((2,1))
    # with text_column:
    #     st.subheader("🎮 2D Shooting Game")
    #     st.write(
    #     """
    #     - Designed and implemented a **fun 2D game** with scoreboards and boosters.  
    #     - Tech used: JavaScript, HTML, CSS, Bootstrap.  
    #     """
    #     )
    # with image_column:
    #     st_lottie(lottie_coding, height=300, key="coding7")


# --- EDUCATION ---
# with st.container():

#     st.write("---")
#     st.header("🎓 Education")
#     image_column, text_column = st.columns((1,2))
#     # with image_column:
#         # st_lottie(lottie_coding, height=300, key="coding11") 
#     with text_column: 
#         st.write(
#         """
#         - **B.E. Information Technology (Honors in Cyber Security)** – SIES GST, CGPA: 8.65 (2020–2024)  
#         - **12th HSC** – Ramnivas Ruia Jr. College, 77.2% (2020)  
#         - **10th SSC** – St. Anthony’s Girls High School, 95.2% (2018)  
#         """
#              )

# --- PUBLICATIONS ---
with st.container():
    st.write("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>📖 Publications & Research</h2>
            <p>
                - <i><a href="https://www.gssrr.org/index.php/JournalOfBasicAndApplied/article/view/17084" target="_blank">Comparative Study and Analysis of Deep Fake Detection using ML</a></i> – <b>Indian Journal of Natural Sciences</b>, Aug 2024 <br><br>
                - <i><a href="https://journals.stmjournals.com/joipprp/article=2024/view=171885/" target="_blank">An Analysis of Multimodal Fusion in Deepfake Detection for Video Samples</a></i> – <b>ICATM-2024</b>, Apr 2024
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # with image_column:
    #     st_lottie(lottie_coding, height=300, key="coding12")
    

# # --- ACHIEVEMENTS ---
# with st.container():
#     st.write("---")
#     st.header("🏆 Achievements")
#     st.write(
#         """
#         - Regional Qualifier – **Smart India Hackathon** (Text to Video PIB Press Releases)  
#         - **Best Paper Award** – ICATM-2024, Paper on Multimodal Fusion in Deepfake Detection  
#         - 1st Place – **Projexions’24 Poster Presentation**  
#         """
#     )

# --- EXTRA CURRICULAR ---
with st.container():
    st.write("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>🎭 Things that fuel my life</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    
    

    # Image display in a creative grid
    img_im1 = "webpage/Images/img_one.webp"
    img_im2 = "webpage/Images/img_two.jpeg"
    img_im3 = "webpage/Images/img_three.jpeg"
    img_im4 = "webpage/Images/img_four.jpg"
    img_im5 = "webpage/Images/img_five.jpg"
    img_im6 = "webpage/Images/img_six.jpg"

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.image(img_im1, caption="Event 1", use_container_width=True)
        st.image(img_im4, caption="Event 4", use_container_width=True)

    with col2:
        st.image(img_im2, caption="Event 2", use_container_width=True)
        st.image(img_im5, caption="Event 5", use_container_width=True)

    with col3:
        st.image(img_im3, caption="Event 3", use_container_width=True)
        st.image(img_im6, caption="Event 6", use_container_width=True)
