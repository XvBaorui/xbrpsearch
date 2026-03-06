import streamlit as st
import time

# -------------------------- 任务一：页面基础配置与兼容 --------------------------
st.set_page_config(
    page_title="宝圈顶刊文献指引平台",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 任务二：替换为元宝+放大镜图标（视觉优化） --------------------------
st.markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 20px;'>
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 9h16M4 15h16M12 9v6"/>
        </svg>
        <h1 style='margin: 0; color: #2E86AB;'>宝圈顶刊文献指引平台</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; color: #A23B72; margin-top: 0;'>专注顶刊文献精准检索与指引</h3>",
    unsafe_allow_html=True
)

# -------------------------- 关键词检索区（保留原有核心功能） --------------------------
st.divider()
keyword = st.text_input(
    "输入关键词进行精确检索",
    placeholder="例如：应用化学、催化、材料、化工设计...",
    help="支持中英文关键词，多个关键词用逗号分隔"
)

# -------------------------- 任务三：方案A —— 点「开始精确检索」后才展开筛选界面 --------------------------
if st.button("开始精确检索", type="primary"):
    if not keyword.strip():
        st.error("❌ 请输入检索关键词后再提交！")
    else:
        with st.spinner("🔍 正在检索相关顶刊文献，请稍候..."):
            time.sleep(1.2)  # 模拟检索过程
        
        st.success(f"✅ 检索完成！共为您找到与【{keyword.strip()}】相关的顶刊文献，可通过下方筛选器进一步精准定位")
        
        # -------------------------- 筛选区：5行完整筛选（方案A：检索后才显示） --------------------------
        st.divider()
        st.subheader("🎯 精准筛选条件")
        
        # 1. 学科门类
        subject_category = st.multiselect(
            "学科门类",
            options=["全部", "自然科学大类", "社会科学大类", "艺术与人文大类"],
            default=["全部"],
            help="选择您感兴趣的学科大方向"
        )
        
        # 2. 一级学科（根据学科门类联动）
        if "自然科学大类" in subject_category or "全部" in subject_category:
            first_level_nature = st.multiselect(
                "一级学科（自然科学）",
                options=["全部", "数学与统计", "物理学", "化学", "生物与生化", "地球科学", "农业与食品", "医学", "工程类", "材料科学", "计算机能源与仪器"],
                default=["全部"]
            )
        else:
            first_level_nature = ["全部"]
        
        if "社会科学大类" in subject_category or "全部" in subject_category:
            first_level_social = st.multiselect(
                "一级学科（社会科学）",
                options=["全部", "管理学", "经济学", "商学", "金融学", "社会学", "法律", "政治学", "国际关系", "心理学·综合", "教育·综合", "特殊教育", "职业研究", "地理学·人文", "传播学", "图书馆与信息科学", "人类学", "人口学", "伦理学", "社会问题", "社会科学其他"],
                default=["全部"]
            )
        else:
            first_level_social = ["全部"]
        
        if "艺术与人文大类" in subject_category or "全部" in subject_category:
            first_level_arts = st.multiselect(
                "一级学科（艺术与人文）",
                options=["全部", "文学", "语言学", "诗歌", "戏剧", "音乐", "艺术·综合", "建筑历史与评论", "电影、广播、电视", "哲学", "宗教学", "历史", "考古学", "古典文学", "地区研究", "人文研究·跨学科"],
                default=["全部"]
            )
        else:
            first_level_arts = ["全部"]
        
        # 3. 二级学科（仅自然科学大类显示）
        if "自然科学大类" in subject_category or "全部" in subject_category:
            st.subheader("🔬 二级学科（仅自然科学）")
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
            # 其他自然科学二级学科，后续可按同样格式补充
        
        # 4. 期刊来源（先搭框架，后续慢慢加顶刊）
        journal_source = st.multiselect(
            "期刊来源",
            options=["全部"],  # 后续添加 Nature、JACS、中科院1区、中国卓越计划等
            default=["全部"],
            help="后续将逐步录入顶刊名称与分区筛选选项"
        )
        
        # 5. 年份
        year = st.multiselect(
            "年份",
            options=["全部", "近10年", "近5年", "近3年"],
            default=["全部"]
        )
        
        # -------------------------- 结果展示区（示例，后续可对接真实数据） --------------------------
        st.divider()
        st.subheader("📄 文献结果展示区")
        with st.container(border=True):
            st.markdown(f"### 基于关键词「{keyword.strip()}」的检索结果（示例）")
            st.write(f"1. 《{keyword.strip()}领域最新研究进展》- Nature Chemistry - 2025")
            st.write(f"2. 《基于{keyword.strip()}的催化性能优化》- Journal of the American Chemical Society - 2025")
            st.write("🔗 点击文献标题可查看全文（功能待完善）")
else:
    # 未检索时的引导提示
    st.divider()
    st.subheader("📄 文献结果展示区")
    st.info("💡 输入关键词并点击「开始精确检索」，即可解锁完整筛选功能并查看相关顶刊文献")

# -------------------------- 页脚优化 --------------------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 14px;'>© 2026 宝圈顶刊文献指引平台 | 精准检索 · 学术助手</p>",
    unsafe_allow_html=True
)
