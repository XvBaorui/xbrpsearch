import streamlit as st
st.config.set_option("client.showErrorDetails", False)
st.set_page_config(
    page_title="宝圈顶刊文献指引平台",
    page_icon="📚",
    layout="wide"
)

st.title("📚 宝圈顶刊文献指引平台")
st.subheader("专注顶刊文献精准检索与指引")

keyword = st.text_input("输入关键词进行精确检索", placeholder="例如：应用化学、催化、材料、化工设计...")

if st.button("开始精确检索"):
    st.success("✅ 检索框架已启动，后续可接入数据实现真正检索")

st.divider()
st.subheader("📄 文献结果展示区")
st.info("基础框架已完成，功能可后续逐步扩展")

st.divider()

st.caption("© 2026 宝圈顶刊文献指引平台 | 精准检索 · 学术助手")
