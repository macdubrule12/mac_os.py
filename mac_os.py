import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="MAC.OS",
    layout="wide"
)

# --- DARK AESTHETIC STYLING ---
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #f5f5f5;
}
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    font-weight: 500;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 MAC.OS")
st.caption("A personal operating system.")

st.divider()

tabs = st.tabs([
    "🧠 Home",
    "🔧 Systems",
    "🎨 Gallery",
    "📚 Research",
    "🚀 Lab",
    "🗓 DubieDash",
    "🔮 Birth Chart"
])

# ---------------- HOME ----------------
with tabs[0]:
    st.header("Current State")

    st.markdown(f"""
    **Last Updated:** {datetime.now().strftime("%B %d, %Y")}
    
    **Location:** Washington, D.C.  
    **Mode:** Builder / Analyst / Artist  
    """)

    st.subheader("Currently Building")
    st.markdown("""
    - AI workflow systems  
    - Policy intelligence compression tools  
    - Personal dashboard infrastructure  
    """)

    st.subheader("Thinking About")
    st.markdown("""
    - AI x national security  
    - Institutional integration  
    - Creative system design  
    """)

# ---------------- SYSTEMS ----------------
with tabs[1]:
    st.header("AI Systems")

    with st.expander("📬 Job Board Automation"):
        st.markdown("""
        Status: 🟢 Live  
        Stack: GitHub Actions + Webhook + Email  
        Purpose: Weekly policy job intelligence  
        """)

    with st.expander("📊 Hearings Dashboard"):
        st.markdown("""
        Status: 🟢 Active  
        Stack: Streamlit + RSS  
        Purpose: Legislative tracking  
        """)

    with st.expander("🧩 Policy Signal Compressor"):
        st.markdown("""
        Status: 🟡 Concept  
        Purpose: Structured risk extraction  
        """)

# ---------------- GALLERY ----------------
with tabs[2]:
    st.header("Art Archive")

    st.markdown("Upload images here later. Grid layout coming soon.")

# ---------------- RESEARCH ----------------
with tabs[3]:
    st.header("Research & Writing")

    st.markdown("""
    - AI x Energy Policy  
    - Intelligence & Security  
    - Organizational AI Adoption  
    """)

# ---------------- LAB ----------------
with tabs[4]:
    st.header("Experimental Lab")

    st.markdown("""
    - Agent architectures  
    - AI-native workflow design  
    - DubieDash family system (future build)  
    """)

# ---------------- DUBIEDASH ----------------
with tabs[5]:
    st.header("DubieDash (Coming Soon)")

    st.markdown("""
    Family command center prototype.
    
    Future Features:
    - Shared calendar sync  
    - Flight tracking  
    - Location sharing  
    - AI itinerary builder  
    """)

# ---------------- BIRTH CHART ----------------
with tabs[6]:
    st.header("Birth Chart")

    st.markdown("""
    May 12, 2004  
    7:57 AM  
    McAllen, TX  

    Structured builder with aesthetic instinct.
    """)