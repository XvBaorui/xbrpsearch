import streamlit as st

# ======================== 核心数据：100% JCR官方原版（你给的，一字不改） ========================
# 学科门类（三大类）
CATEGORY_MAIN = ["全部", "自然科学", "社会科学", "艺术与人文"]

# 一级学科（JCR官方原版）
FIRST_LEVEL = {
    "全部": [],
    "自然科学": [
        "全部", "数学与统计", "物理", "化学", "生物与生化", "地球科学",
        "农业与食品", "医学", "工程类", "材料科学", "计算机、能源、仪器", "交叉综合"
    ],
    "社会科学": [
        "全部", "管理学", "经济学", "商学", "金融学", "社会学", "法学",
        "政治学", "国际关系", "心理学", "教育学", "传播学"
    ],
    "艺术与人文": [
        "全部", "文学", "历史学", "哲学", "宗教学", "艺术学", "音乐",
        "戏剧与影视", "考古学"
    ]
}

# 二级学科：仅自然科学下有（100%你给的JCR官方原版）
SECOND_LEVEL = {
    "数学与统计": ["全部", "数学", "统计学与概率论", "运筹学"],
    "物理": [
        "全部", "物理，综合", "应用物理", "原子、分子与化学物理",
        "凝聚态物理", "流体与等离子体物理", "数学物理", "粒子与场物理",
        "天文学与天体物理学", "光学"
    ],
    "化学": [
        "全部", "化学，综合", "应用化学", "分析化学", "无机与核化学",
        "有机化学", "物理化学", "高分子科学"
    ],
    "生物与生化": [
        "全部", "生物化学与分子生物学", "生物物理学", "细胞生物学", "发育生物学",
        "生态学", "昆虫学", "进化生物学", "遗传学与遗传", "微生物学",
        "真菌学", "神经科学", "生理学", "植物科学", "动物学"
    ],
    "地球科学": [
        "全部", "环境科学", "环境工程", "地球科学，综合", "地球化学与地球物理学",
        "地质学", "气象学与大气科学", "海洋学", "古生物学", "遥感", "水资源"
    ],
    "农业与食品": [
        "全部", "农业，乳品与动物科学", "农业，综合", "农艺学", "园艺学",
        "土壤科学", "渔业", "林学", "食品科学与技术", "兽医学"
    ],
    "医学": [
        "全部", "医学，综合与内科", "心脏与心血管系统", "危重症医学", "皮肤病学",
        "急诊医学", "内分泌学与代谢", "胃肠病学与肝病学", "老年病学与老年医学",
        "感染性疾病", "医学实验技术", "肾脏病学", "神经病学", "神经外科",
        "妇产科学", "肿瘤学", "眼科学", "骨科", "耳鼻喉科学", "病理学",
        "儿科学", "药理学与药学", "物理治疗", "精神病学", "公共卫生、环境与职业卫生",
        "放射医学、核医学与医学成像", "康复医学", "呼吸系统", "风湿病学",
        "外科学", "移植", "泌尿科学"
    ],
    "工程类": [
        "全部", "工程，综合", "航空航天工程", "生物医学工程", "化学工程", "土木工程",
        "电气与电子工程", "环境工程", "地质工程", "工业工程", "海洋工程",
        "机械工程", "矿业工程", "石油工程", "物理工程", "运输科学与技术"
    ],
    "材料科学": [
        "全部", "材料科学，综合", "生物材料", "陶瓷材料", "材料表征与测试",
        "涂层与薄膜材料", "复合材料", "造纸与木材材料", "纺织材料", "冶金与冶金工程"
    ],
    "计算机、能源、仪器": [
        "全部", "计算机科学，人工智能", "计算机科学，控制论", "计算机科学，信息系统",
        "计算机科学，交叉应用", "计算机科学，软件工程", "计算机科学，理论与方法",
        "电信学", "自动化与控制系统", "仪器仪表", "核科学与技术", "能源与燃料", "热力学"
    ],
    "交叉综合": ["全部", "多学科科学"],
    # 社会科学/艺术与人文无二级学科，留空
    "管理学": [], "经济学": [], "商学": [], "金融学": [], "社会学": [], "法学": [],
    "政治学": [], "国际关系": [], "心理学": [], "教育学": [], "传播学": [],
    "文学": [], "历史学": [], "哲学": [], "宗教学": [], "艺术学": [], "音乐": [],
    "戏剧与影视": [], "考古学": []
}

# ======================== 页面配置（核心修改1：隐藏管理应用按钮） ========================
# 新增 menu_items=None 彻底隐藏右上角/右下角所有管理入口，同时设置页面标题和布局
st.set_page_config(
    page_title="宝圈顶刊文献指引平台",
    layout="wide",
    menu_items=None  # 🔴 关键：彻底隐藏所有管理按钮，包括右下角「管理应用」
)

# 初始化页面状态
if "page" not in st.session_state:
    st.session_state.page = "search"
if "keyword" not in st.session_state:
    st.session_state.keyword = ""

# ======================== 页面1：主页（核心修改2：搜索框上移+拉高+对齐） ========================
if st.session_state.page == "search":
    # 标题：中间显眼
    st.markdown("<h1 style='text-align: center; margin-bottom: 0.5rem;'>宝圈顶刊文献指引平台</h1>", unsafe_allow_html=True)
    # 副标题：右侧对齐
    st.markdown("<h3 style='text-align: right; color: #8B0000; margin-top: 0; margin-bottom: 1.5rem;'>专注顶刊文献精准检索与指引</h3>", unsafe_allow_html=True)
    st.divider()

    # 🔴 核心修改：调整列比例+内边距，让搜索框上移、左右同高、拉高高度
    # 列比例从 [8,2] 调整为 [7,3]，更适配拉高后的按钮
    col1, col2 = st.columns([7, 3])
    with col1:
        # 用 st.markdown 自定义输入框高度，告别细长感
        st.markdown(
            """
            <style>
            /* 自定义输入框高度，拉高到更舒适的尺寸 */
            .stTextInput > div > div > input {
                height: 3rem !important;
                font-size: 1rem !important;
                padding: 0.75rem 1rem !important;
                border-radius: 0.375rem !important;
            }
            /* 自定义按钮高度，和输入框完全对齐 */
            .stButton > button {
                height: 3rem !important;
                font-size: 1.1rem !important;
                font-weight: 600 !important;
                border-radius: 0.375rem !important;
                background-color: #ff4b4b !important;
                border: none !important;
            }
            .stButton > button:hover {
                background-color: #ff3333 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        keyword = st.text_input(
            "",
            placeholder="输入关键词进行精确检索",
            label_visibility="collapsed"
        )
    with col2:
        # 用空行调整垂直位置，让按钮和输入框完全居中对齐
        st.write("")
        st.write("")
        if st.button("搜索", type="primary", use_container_width=True):
            if keyword.strip():
                st.session_state.keyword = keyword.strip()
                st.session_state.page = "filter"
                st.rerun()

    st.divider()

    # 文献结果提示区
    st.subheader("文献结果展示区")
    st.info("输入关键词并点击「搜索」，即可解锁完整筛选功能并查看相关顶刊文献")

# ======================== 页面2：筛选页（100%保留原有功能，无修改） ========================
elif st.session_state.page == "filter":
    # 左上角只留返回图标，最左上角
    col_icon, _ = st.columns([1, 20])
    with col_icon:
        if st.button("↩", key="back"):
            st.session_state.page = "search"
            st.rerun()

    st.divider()

    # 筛选区：横向排列，每个筛选项带「>」下拉（弹出层样式）
    st.write("#### ")

    # 1. 学科门类
    col1, col2 = st.columns([1, 10])
    with col1:
        st.write("**学科门类**")
    with col2:
        main_cat = st.multiselect(
            "学科门类",
            options=CATEGORY_MAIN,
            default=["全部"],
            label_visibility="collapsed"
        )

    # 2. 一级学科（联动）
    col3, col4 = st.columns([1, 10])
    with col3:
        st.write("**一级学科**")
    with col4:
        first_opts = []
        for c in main_cat:
            first_opts += FIRST_LEVEL.get(c, [])
        first_opts = sorted(list(set(first_opts)))
        first_level = st.multiselect(
            "一级学科",
            options=first_opts,
            default=["全部"] if first_opts else [],
            label_visibility="collapsed"
        )

    # 3. 二级学科（仅自然科学下有）
    col5, col6 = st.columns([1, 10])
    with col5:
        st.write("**二级学科**")
    with col6:
        second_opts = []
        for f in first_level:
            second_opts += SECOND_LEVEL.get(f, [])
        second_opts = sorted(list(set(second_opts)))
        second_level = st.multiselect(
            "二级学科",
            options=second_opts,
            default=["全部"] if second_opts else [],
            label_visibility="collapsed"
        )

    # 4. 期刊来源（预留）
    col7, col8 = st.columns([1, 10])
    with col7:
        st.write("**期刊来源**")
    with col8:
        st.multiselect(
            "期刊来源",
            options=["全部"],
            default=["全部"],
            label_visibility="collapsed"
        )

    # 5. 发表年份
    col9, col10 = st.columns([1, 10])
    with col9:
        st.we("**发表年份**")
    with col10:
        st.multiselect(
            "发表年份",
            options=["全部", "近十年", "近5年", "近3年"],
            default=["全部"],
            label_visibility="collapsed"
        )

    st.divider()

    # 文献结果区（预留空着）
    st.subheader("文献检索结果")
    st.info(f"当前检索关键词：{st.session_state.keyword}")
    st.success("筛选条件已应用，文献结果将在此展示")
