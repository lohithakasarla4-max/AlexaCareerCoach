import streamlit as st
import streamlit.components.v1 as components
import random

# Page configuration
st.set_page_config(
    page_title="Alexa Career Coach", 
    page_icon="🎙️", 
    layout="centered"
)

# Custom CSS for modern dark UI
custom_css = """
<style>
    /* Main Background and Text Color */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header Container */
    .main-header {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 210, 255, 0.15);
        margin-bottom: 25px;
    }
    
    .main-header h1 {
        color: #58a6ff;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .main-header p {
        color: #8b949e;
        font-size: 1.05rem;
    }

    /* Input Card Styling */
    .stTextArea label, .stTextInput label {
        color: #58a6ff !important;
        font-weight: 600;
    }
    
    .stTextArea textarea, .stTextInput input {
        background-color: #161b22 !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }

    /* Custom Gradient Button */
    .stButton>button {
        background: linear-gradient(90deg, #1f6beb 0%, #238636 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 24px !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(31, 107, 235, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    /* Alexa Voice Output Box */
    .alexa-box {
        background-color: #161b22;
        border-left: 5px solid #58a6ff;
        border-radius: 8px;
        padding: 18px;
        margin-top: 15px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .alexa-box h3 {
        color: #58a6ff;
        margin-top: 0;
        font-size: 1.2rem;
    }
    
    .alexa-box p {
        color: #e6edf3;
        font-size: 1.1rem;
        font-style: italic;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Header Banner
st.markdown("""
<div class="main-header">
    <h1>🎙️ Alexa Career Coach</h1>
    <p>Simulated Alexa+ AI Voice Companion • Resume Gap Analysis & Mock Interviews</p>
</div>
""", unsafe_allow_html=True)

# Energetic Web Speech API
def speak_energetic(text):
    clean_text = text.replace('"', '\\"').replace('\n', ' ')
    speech_js = f"""
    <script>
    function speak() {{
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        msg.rate = 1.15;
        msg.pitch = 1.25;
        msg.volume = 1.0;
        
        var voices = window.speechSynthesis.getVoices();
        for (var i = 0; i < voices.length; i++) {{
            if (voices[i].lang.includes("en") && (voices[i].name.includes("Google") || voices[i].name.includes("Natural") || voices[i].name.includes("Zira"))) {{
                msg.voice = voices[i];
                break;
            }}
        }}
        window.speechSynthesis.speak(msg);
    }}
    speak();
    </script>
    """
    components.html(speech_js, height=0)

# Sidebar Navigation
st.sidebar.markdown("### ⚙️ Alexa+ Controls")
mode = st.sidebar.selectbox("Select Experience Mode", ["Resume Skill Gap Analysis", "Mock Interview Session"])

if mode == "Resume Skill Gap Analysis":
    st.subheader("📄 Resume & Job Description Matcher")
    resume_text = st.text_area("Paste Your Resume Text:", height=150)
    jd_text = st.text_area("Paste Target Job Description:", height=150)
    
    if st.button("🚀 Analyze with Alexa+ Agent"):
        if resume_text and jd_text:
            score = random.randint(86, 96)
            
            st.markdown(f"### 🎯 Alignment Score: `{score}%`")
            
            speech_message = f"Awesome news! I've analyzed your resume and you scored a fantastic {score} percent! To make your application stand out even more, consider highlighting more hands-on experience with cloud deployment workflows and Docker containers!"
            
            st.markdown(f"""
            <div class="alexa-box">
                <h3>🗣️ Alexa Voice Response:</h3>
                <p>"{speech_message}"</p>
            </div>
            """, unsafe_allow_html=True)
            
            speak_energetic(speech_message)
            
            st.markdown("### 🔍 Key Recommendations")
            st.write("✅ **Strengths:** Strong core programming skills, clean project structure, and web development experience.")
            st.write("⚠️ **Suggested Missing Keywords:** `AWS Lambda`, `Docker`, `CI/CD pipelines`.")
        else:
            st.warning("Please paste both your resume and job description to run analysis.")

else:
    st.subheader("💬 Interactive Mock Interview")
    role = st.text_input("Target Role Title:", "Software Engineer - Python & AI")
    
    if st.button("🎤 Begin Voice Interview"):
        interview_prompt = "Welcome to your mock interview! Let's dive right in with your first question: Can you explain how you handle database migrations in a Flask application? Take a breath and give it your best shot!"
        
        st.markdown(f"""
        <div class="alexa-box">
            <h3>🗣️ Alexa Interviewer Prompt:</h3>
            <p>"{interview_prompt}"</p>
        </div>
        """, unsafe_allow_html=True)
        
        speak_energetic(interview_prompt)
        
        user_answer = st.text_area("Your Voice Response (Simulated Text Entry):", height=100)
        if user_answer:
            feedback = "Fantastic answer! Your explanation of database handling was super clear. Mentioning transaction rollbacks will make it truly top tier!"
            st.success(feedback)
            speak_energetic(feedback)