import streamlit as st
from utils import get_page_content, personalize_content

st.set_page_config(page_title="AI Landing Page Personalizer")

st.title("🚀 AI Landing Page Personalizer")
st.write("Enhance your landing page based on ad creatives using AI")

# Inputs
ad_input = st.text_area("📢 Enter Ad Creative (text or link)")
url_input = st.text_input("🌐 Enter Landing Page URL")

# Button
if st.button("Generate Personalized Page"):

    if not ad_input or not url_input:
        st.warning("Please fill both inputs")
    else:
        with st.spinner("Analyzing and generating..."):

            # Step 1: Get page content
            page_content = get_page_content(url_input)

            # Step 2: AI personalization
            result = personalize_content(ad_input, page_content)

        # Display results
        st.success("Done!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧾 Original Content")
            st.write(page_content)

        with col2:
            st.subheader("✨ Personalized Content")
            st.write(result)