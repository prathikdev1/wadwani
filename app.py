import streamlit as st

st.set_page_config(
    page_title="PolliDrone AI",
    page_icon="🚁",
    layout="wide"
)

st.markdown("""
<style>
.hero {
    text-align: center;
    padding: 3rem;
    background: linear-gradient(135deg,#0f5132,#198754);
    color: white;
    border-radius: 15px;
}
.feature-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #f5f5f5;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🚁 PolliDrone AI</h1>
    <h3>Precision Pollination. Maximum Yield.</h3>
    <p>
    AI-powered drone pollination for greenhouse operators and
    high-value crop farmers.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("🌾 The Problem")

st.write("""
Natural pollinators are declining due to climate change,
pesticides, and habitat loss. Farmers face increasing labor
costs and inconsistent pollination, resulting in reduced crop
yield and profitability.
""")

st.markdown("---")

st.header("💡 Our Solution")

st.write("""
PolliDrone AI uses artificial intelligence, computer vision,
and autonomous drone technology to identify flowers and
perform precise pollination at scale.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>📈 Higher Yield</h3>
    Consistent and accurate pollination improves productivity.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    <h3>🤖 AI Precision</h3>
    Intelligent flower detection and targeting.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>💰 Lower Costs</h3>
    Reduce dependence on seasonal labor.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    <h3>🌱 Sustainable</h3>
    Supports future food security and sustainable farming.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.header("🎯 Unique Value Proposition")

st.success(
    "AI-powered drone pollination delivers precise, reliable, "
    "and cost-effective pollination, helping farmers maximize "
    "yields despite labor shortages and declining pollinator populations."
)

st.markdown("---")

st.header("📞 Contact Us")

st.write("📧 contact@pollidrone.ai")
st.write("📱 +91-7703900579")

if st.button("Book a Demo"):
    st.balloons()
    st.success("Thank you! Our team will contact you soon.")
