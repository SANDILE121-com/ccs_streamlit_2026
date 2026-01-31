import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MthembnEi Mathonsi | Research Profile",
    page_icon="🎓",
    layout="centered"
)

# Header
st.title("🎓 Mthembeni Mathonsi")
st.subheader("BSc Honours in Applied Mathematics | Researcher")

st.markdown(
    """
    📍 University of Zululand  
    📧 Email: sandilemthon@gmail.com  

    ---
    """
)

# About Me
st.header("👤 About Me")
st.write(
    """
    I am **Mthembeni Mathonsi**, a BSc Honours student in **Applied Mathematics**
    with a strong interest in mathematical modelling, numerical methods,
    and image processing. My academic goal is to apply mathematics and
    computational techniques to solve real-world problems, particularly
    in healthcare and data-driven fields.
    """
)

# Research Interests
st.header("🔬 Research Interests")
st.markdown(
    """
    - Numerical Methods  
    - Applied Mathematics  
    - Medical Image Processing  
    - Image Denoising Techniques  
    - Scientific Computing  
    """
)

# Current Research
st.header("📘 Current Research")
st.write(
    """
    **Title:** *Enhanced Medical Image Denoising with Spectrum-Based Techniques and Edge Preservation*

    This research focuses on improving medical image quality by using
    spectrum-based methods (such as Fourier-based techniques) while
    preserving important edge features that are critical for diagnosis.
    """
)

# Skills
st.header("🛠 Skills & Tools")
st.markdown(
    """
    - Python (NumPy, Pandas, Matplotlib)
    - Streamlit
    - Mathematical Modelling
    - Data Analysis
    - Linear Algebra & Calculus
    """
)

# Future Goals
st.header("🚀 Future Goals")
st.write(
    """
    I aim to pursue postgraduate studies and become a problem solver
    who uses mathematics, data, and computation to uplift communities
    and contribute to scientific and technological development.
    """
)

# Footer
st.markdown("---")
st.markdown("© 2026 | Mthembini Mathonsi | Research Profile")
