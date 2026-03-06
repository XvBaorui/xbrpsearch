import streamlit as st
import time
import base64

# -------------------------- 任务2：全应用图标统一（元宝+放大镜） --------------------------
# 你的元宝+放大镜图标完整SVG（100%还原你给的图）
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
# 转成base64，避免前端DOM冲突
LOGO_B64 = base64.b64encode(LOGO_SVG.encode()).decode()
LOGO_DATA_URL = f"data:image/svg+xml;base64,{LOGO_B64}"

st.set_page_config(
    page_title="宝圈顶刊文献指引平台",
    page_icon=LOGO_DATA_URL,  # 浏览器标签页图标
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 任务3：百度式极简主页 --------------------------
if "search_submitted" not in st.session_state:
    st.session_state.search_submitted = False
    st.session_state.current_keyword = ""

# 未搜索时：只展示搜索框+按钮
if not st.session_state.search_submitted:
    # 顶部Logo+标题（用img标签加载base64图标，无DOM冲突）
    st.markdown(
        f"""
        <div style='text-align:center; margin-top:80px; margin-bottom:30px;'>
            <img src="{LOGO_DATA_URL}" width="80" height="80" alt="元宝放大镜Logo">
            <h1 style='margin:15px 0 0; color:#2E86AB; font-size:32px;'>宝圈顶刊文献指引平台</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 单行搜索框+按钮（仿百度）
    col_input, col_btn = st.columns([11, 1])
    with col_input:
        keyword = st.text_input(
            "",
            placeholder="输入关键词检索顶刊文献...",
            label_visibility="collapsed"
        )
    with col_btn:
        if st.button("搜索", type="primary", use_container_width=True):
            if keyword.strip():
                st.session_state.current_keyword = keyword.strip()
                st.session_state.search_submitted = True
                st.rerun()
            else:
                st.error("请输入关键词后再搜索")

# -------------------------- 任务3：搜索后 —— 筛选+结果页 --------------------------
else:
    # 顶部小Logo+标题
    st.markdown(
        f"""
        <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:20px;'>
            <img src="{LOGO_DATA_URL}" width="32" height="32" alt="元宝放大镜Logo">
            <h2 style='margin:0; color:#2E86AB;'>宝圈顶刊文献指引平台</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    st.subheader(f"🔍 检索关键词：「{st.session_state.current_keyword}」")

    # -------------------------- 筛选区（复选框小方框样式） --------------------------
    st.subheader("🎯 精准筛选条件")
    with st.container(border=True):
        # 1. 学科门类
        subject_category = st.multiselect(
            "学科门类",
            options=["全部", "自然科学大类", "社会科学大类", "艺术与人文大类"],
            default=["全部"]
        )

        # 2. 一级学科
        if "自然科学大类" in subject_category or "全部" in subject_category:
            first_level_nature = st.multiselect(
                "一级学科（自然科学）",
                options=["全部", "数学与统计", "物理学", "化学", "生物与生化", "地球科学", "农业与食品", "医学", "工程类", "材料科学", "计算机能源与仪器"],
                default=["全部"]
            )
        if "社会科学大类" in subject_category or "全部" in subject_category:
            first_level_social = st.multiselect(
                "一级学科（社会科学）",
                options=["全部", "管理学", "经济学", "商学", "金融学", "社会学", "法律", "政治学", "国际关系", "心理学·综合", "教育·综合", "特殊教育", "职业研究", "地理学·人文", "传播学", "图书馆与信息科学", "人类学", "人口学", "伦理学", "社会问题", "社会科学其他"],
                default=["全部"]
            )
        if "艺术与人文大类" in subject_category or "全部" in subject_category:
            first_level_arts = st.multiselect(
                "一级学科（艺术与人文）",
                options=["全部", "文学", "语言学", "诗歌", "戏剧", "音乐", "艺术·综合", "建筑历史与评论", "电影、广播、电视", "哲学", "宗教学", "历史", "考古学", "古典文学", "地区研究", "人文研究·跨学科"],
                default=["全部"]
            )

        # 3. 二级学科（仅自然科学）
        if "自然科学大类" in subject_category or "全部" in subject_category:
            st.caption("🔬 二级学科（仅自然科学）")
            if "化学" in first_level_nature or "全部" in first_level_nature:
                second_level_chem = st.multiselect(
                    "化学",
                    options=["全部", "化学·综合", "应用化学", "分析化学", "无机与核化学", "有机化学", "物理化学", "高分子科学", "电化学", "光谱学", "晶体学"],
                    default=["全部"]
                )
            if "物理学" in first_level_nature or "全部" in first_level_nature:
                second_level_phys = st.multiselect(
                    "物理学",
                    options=["全部", "物理学·综合", "应用物理", "原子、分子与化学物理", "凝聚态物理", "流体与等离子体物理", "粒子与场物理", "核物理", "天文学与天体物理学", "光学", "声学", "量子科学与技术"],
                    default=["全部"]
                )

        # 4. 期刊来源
        journal_source = st.multiselect(
            "期刊来源",
            options=["全部"],
            default=["全部"]
        )

        # 5. 年份
        year = st.multiselect(
            "年份",
            options=["全部", "近10年", "近5年", "近3年"],
            default=["全部"]
        )

    # -------------------------- 结果展示区 --------------------------
    st.divider()
    st.subheader("📄 文献结果展示区")
    with st.spinner("正在检索..."):
        time.sleep(1)
    st.success(f"✅ 找到与「{st.session_state.current_keyword}」相关的顶刊文献")
    with st.container(border=True):
        st.markdown(f"### 基于关键词「{st.session_state.current_keyword}」的检索结果")
        st.write(f"1. 《{st.session_state.current_keyword}领域最新研究进展》- Nature Chemistry - 2025")
        st.write(f"2. 《基于{st.session_state.current_keyword}的催化性能优化》- JACS - 2025")

    # 返回搜索页按钮
    if st.button("返回搜索页"):
        st.session_state.search_submitted = False
        st.rerun()

# -------------------------- 页脚 --------------------------
st.divider()
st.markdown(
    "<p style='text-align:center; color:#6c757d; font-size:14px;'>© 2026 宝圈顶刊文献指引平台 | 精准检索 · 学术助手</p>",
    unsafe_allow_html=True
)
