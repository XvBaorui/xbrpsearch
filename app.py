import streamlit as st

# ======================== 100% JCR官方原版分科数据（你给的，一字不改） ========================
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

# 二级学科：100% 你提供的 JCR官方原版 Science 大类（一字不改）
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

# ======================== 页面配置与初始化 ========================
st.set_page_config(page_title="宝圈顶刊文献指引平台", layout="wide")

# 初始化页面状态
if "page" not in st.session_state:
    st.session_state.page = "search"
if "keyword" not in st.session_state:
    st.session_state.keyword = ""

# ======================== 页面1：搜索页（100%还原你截图样式） ========================
if st.session_state.page == "search":
    # 永久锁死标题+副标题（和你截图一字不差）
    st.title("宝圈顶刊文献指引平台")
    st.subheader("专注顶刊文献精准检索与指引")
    st.divider()

    # 百度式搜索框：输入框+红色按钮并排
    col1, col2, col3 = st.columns([3, 6, 1])
    with col1:
        st.write("")
    with col2:
        keyword = st.text_input(
            "",
            placeholder="输入关键词进行精确检索",
            label_visibility="collapsed"
        )
    with col3:
        if st.button("开始精确检索", type="primary", use_container_width=True):
            if keyword.strip():
                st.session_state.keyword = keyword.strip()
                st.session_state.page = "results"
                st.rerun()

    st.divider()

    # 文献结果提示区（和你截图一致）
    st.subheader("文献结果展示区")
    st.info("输入关键词并点击「开始精确检索」，即可解锁完整筛选功能并查看相关顶刊文献")

# ======================== 页面2：结果筛选页（你要的任务3） ========================
elif st.session_state.page == "results":
    # 顶部返回按钮
    if st.button("🔙 返回搜索"):
        st.session_state.page = "search"
        st.rerun()

    # 标题+副标题
    st.title("宝圈顶刊文献指引平台")
    st.subheader("专注顶刊文献精准检索与指引")
    st.divider()

    # 筛选区：学科门类→一级学科→二级学科（仅自然科学有二级）
    st.subheader("筛选条件")

    # 1. 学科门类
    col1_label, col1_opts = st.columns([1, 9])
    with col1_label:
        st.write("**学科门类**")
    with col1_opts:
        main_cat = st.multiselect(
            "学科门类筛选",
            options=CATEGORY_MAIN,
            default=["全部"],
            label_visibility="collapsed",
            key="main_cat"
        )

    # 2. 一级学科（联动）
    col2_label, col2_opts = st.columns([1, 9])
    with col2_label:
        st.write("**一级学科**")
    with col2_opts:
        first_level_options = []
        for cat in main_cat:
            first_level_options += FIRST_LEVEL.get(cat, [])
        first_level_options = sorted(list(set(first_level_options)))
        first_level = st.multiselect(
            "一级学科筛选",
            options=first_level_options,
            default=["全部"] if first_level_options else [],
            label_visibility="collapsed",
            key="first_level"
        )

    # 3. 二级学科（仅自然科学下有）
    col3_label, col3_opts = st.columns([1, 9])
    with col3_label:
        st.write("**二级学科**")
    with col3_opts:
        second_level_options = []
        for f in first_level:
            second_level_options += SECOND_LEVEL.get(f, [])
        second_level_options = sorted(list(set(second_level_options)))
        second_level = st.multiselect(
            "二级学科筛选",
            options=second_level_options,
            default=["全部"] if second_level_options else [],
            label_visibility="collapsed",
            key="second_level"
        )

    # 4. 期刊来源
    col4_label, col4_opts = st.columns([1, 9])
    with col4_label:
        st.write("**期刊来源**")
    with col4_opts:
        journals = st.multiselect(
            "期刊来源筛选",
            options=["全部", "JACS", "Angew", "Nature", "Science", "Cell"],
            default=["全部"],
            label_visibility="collapsed",
            key="journals"
        )

    # 5. 年份
    col5_label, col5_opts = st.columns([1, 9])
    with col5_label:
        st.write("**发表年份**")
    with col5_opts:
        years = st.multiselect(
            "年份筛选",
            options=["全部", "近1年", "近3年", "近5年", "近10年"],
            default=["全部"],
            label_visibility="collapsed",
            key="years"
        )

    st.divider()

    # 文献结果区
    st.subheader("文献检索结果")
    st.info(f"当前检索关键词：**{st.session_state.keyword}**")
    st.success("筛选条件已应用，下方为匹配的文献列表")
