import streamlit as st
import time
import base64

# -------------------------- 任务2：你的元宝+放大镜Logo（100%嵌入，全场景显示） --------------------------
# 完美还原你这张图的SVG代码
LOGO_SVG = """
<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <!-- 元宝底座 -->
    <path d="M20 70 L80 70 L85 85 L15 85 Z"/>
    <!-- 元宝两侧 -->
    <path d="M20 70 C20 50, 10 40, 30 35 L70 35 C90 40, 80 50, 80 70"/>
    <!-- 放大镜 -->
    <circle cx="50" cy="45" r="20"/>
    <path d="M60 55 L70 65"/>
    <path d="M45 35 L35 25"/>
</svg>
"""
# 转成base64，保证任何设备/浏览器都能加载，不会路径/报错
LOGO_B64 = base64.b64encode(LOGO_SVG.encode()).decode()
LOGO_DATA_URL = f"data:image/svg+xml;base64,{LOGO_B64}"

# -------------------------- 任务1：全设备兼容基础配置 --------------------------
st.set_page_config(
    page_title="宝圈顶刊文献指引平台",
    page_icon=LOGO_DATA_URL,  # 浏览器标签页就是你的元宝Logo
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 状态管理：控制搜索页/结果页切换 --------------------------
if "search_done" not in st.session_state:
    st.session_state.search_done = False
    st.session_state.keyword = ""

# -------------------------- 任务3：百度式极简主页 --------------------------
if not st.session_state.search_done:
    # 主页：你的元宝大Logo + 平台标题 + 单行搜索框
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 100px;">
            <img src="{LOGO_DATA_URL}" width="80" height="80" alt="元宝放大镜Logo">
            <h1 style="font-size: 36px; color: #2E86AB; margin-top: 20px; margin-bottom: 30px;">宝圈顶刊文献指引平台</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 单行搜索框+搜索按钮（仿百度，输入框占绝大部分，按钮在右侧）
    col_input, col_btn = st.columns([11, 1])
    with col_input:
        keyword = st.text_input(
            "",
            placeholder="请输入关键词检索顶刊文献...",
            label_visibility="collapsed"
        )
    with col_btn:
        if st.button("搜索", type="primary", use_container_width=True):
            if keyword.strip():
                st.session_state.keyword = keyword.strip()
                st.session_state.search_done = True
                st.rerun()
            else:
                st.warning("请输入关键词后再搜索")

# -------------------------- 任务3：搜索结果页（筛选+结果，完全按你要的布局） --------------------------
else:
    # 顶部：小元宝Logo + 平台标题（紧凑版）
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 20px;">
            <img src="{LOGO_DATA_URL}" width="40" height="40" alt="元宝放大镜Logo">
            <h2 style="font-size: 28px; color: #2E86AB; margin: 0;">宝圈顶刊文献指引平台</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()

    # -------------------------- 筛选区：占页面上1/3，左侧标题+右侧多选框 --------------------------
    st.subheader("精准筛选条件")
    with st.container(border=True):
        # 1. 学科门类：左侧标题，右侧是你要的小方框多选
        col_subject, col_subject_opt = st.columns([2, 8])
        with col_subject:
            st.write("**学科门类**")
        with col_subject_opt:
            subject = st.multiselect(
                "",
                options=["全部", "自然科学", "社会科学", "艺术与人文"],
                default=["全部"],
                label_visibility="collapsed"
            )

        # 2. 一级学科
        col_first, col_first_opt = st.columns([2, 8])
        with col_first:
            st.write("**一级学科**")
        with col_first_opt:
            first_level = st.multiselect(
                "",
                options=["全部", "化学", "物理学", "生物学", "材料科学", "工程学"],
                default=["全部"],
                label_visibility="collapsed"
            )

        # 3. 二级学科
        col_second, col_second_opt = st.columns([2, 8])
        with col_second:
            st.write("**二级学科**")
        with col_second_opt:
            second_level = st.multiselect(
                "",
                options=["全部", "应用化学", "有机化学", "物理化学", "高分子化学"],
                default=["全部"],
                label_visibility="collapsed"
            )

        # 4. 期刊来源
        col_journal, col_journal_opt = st.columns([2, 8])
        with col_journal:
            st.write("**期刊来源**")
        with col_journal_opt:
            journal = st.multiselect(
                "",
                options=["全部", "Nature", "Science", "JACS", "Angew"],
                default=["全部"],
                label_visibility="collapsed"
            )

        # 5. 年份
        col_year, col_year_opt = st.columns([2, 8])
        with col_year:
            st.write("**年份**")
        with col_year_opt:
            year = st.multiselect(
                "",
                options=["全部", "近3年", "近5年", "近10年"],
                default=["全部"],
                label_visibility="collapsed"
            )

    st.divider()

    # -------------------------- 结果展示区：占页面下2/3 --------------------------
    st.subheader(f"检索关键词：「{st.session_state.keyword}」")
    with st.spinner("正在检索相关顶刊文献..."):
        time.sleep(1)
    st.success("✅ 检索完成！以下是匹配结果：")
    with st.container(border=True):
        st.markdown(f"### 1. 《{st.session_state.keyword}领域最新研究进展》")
        st.write("期刊：Nature Chemistry | 年份：2025 | 分区：Top 1")
        st.markdown(f"### 2. 《基于{st.session_state.keyword}的催化性能优化》")
        st.write("期刊：Journal of the American Chemical Society | 年份：2025 | 分区：Top 1")

    # 返回搜索页按钮
    if st.button("返回搜索页"):
        st.session_state.search_done = False
        st.rerun()

# -------------------------- 页脚 --------------------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 14px;'>© 2026 宝圈顶刊文献指引平台 | 精准检索 · 学术助手</p>",
    unsafe_allow_html=True
)
