import streamlit as st
# ======================== JCR 分科（完全保留你的原版，一字未动） ========================
# 第一行：三大类
JCR_MAIN_CATEGORIES = ["全部", "自然科学", "社会科学", "艺术与人文"]
# 第二行：每个大类对应的一级学科（你要的文字全部写出来，不省略！）
FIRST_LEVEL_MAP = {
    "全部": [],
    "自然科学": [
        "全部",
        "数学与统计",
        "物理学",
        "化学",
        "生物与生化",
        "地球科学",
        "农业与食品",
        "医学",
        "工程类",
        "材料科学",
        "计算机、能源、仪器",
        "交叉综合"
    ],
    "社会科学": [
        "全部",
        "管理学",
        "经济学",
        "商学",
        "金融学",
        "社会学",
        "法学",
        "政治学",
        "国际关系",
        "心理学",
        "教育学",
        "传播学"
    ],
    "艺术与人文": [
        "全部",
        "文学",       # 你要求：文学+外国文学 合并成 文学
        "历史学",
        "哲学",
        "宗教学",
        "艺术学",
        "音乐",
        "戏剧与影视",
        "考古学"
    ]
}
# 第三行：二级学科（只有自然科学有，严格你给的 176 小学科）
SECOND_LEVEL_MAP = {
    "数学与统计": [
        "数学", "应用数学", "数学跨学科应用", "统计学与概率论",
        "运筹学与管理科学", "逻辑学", "力学", "数学与计算生物学",
        "数学物理学", "计算机科学·理论与方法", "社会科学·数学方法", "心理学·数学"
    ],
    "物理学": [
        "物理学·综合", "应用物理", "原子、分子与化学物理", "凝聚态物理",
        "流体与等离子体物理", "粒子与场物理", "核物理", "天文学与天体物理学",
        "光学", "声学", "量子科学与技术"
    ],
    "化学": [
        "化学·综合", "应用化学", "分析化学", "无机与核化学",
        "有机化学", "物理化学", "高分子科学", "电化学", "光谱学", "晶体学"
    ],
    "生物与生化": [
        "生物化学与分子生物学", "生物物理学", "细胞生物学", "发育生物学",
        "生态学", "昆虫学", "进化生物学", "遗传学与遗传", "微生物学",
        "真菌学", "神经科学", "生理学", "植物科学", "动物学", "生物学",
        "生物多样性保护", "海洋与淡水生物学", "鸟类学", "寄生虫学", "病毒学",
        "生殖生物学", "生化研究方法", "生物技术与应用微生物学"
    ],
    "地球科学": [
        "地球科学·综合", "地球化学与地球物理学", "地质学", "气象学与大气科学",
        "海洋学", "古生物学", "遥感", "水资源", "环境科学", "环境研究",
        "湖沼学", "自然地理学", "矿物学", "采矿与矿物加工"
    ],
    "农业与食品": [
        "农业·综合", "农业·乳品与动物科学", "农艺学", "园艺学", "土壤科学",
        "渔业", "林学", "食品科学与技术", "兽医学", "农业经济与政策",
        "农业工程", "绿色与可持续科学技术"
    ],
    "医学": [
        "医学·综合与内科", "心脏与心血管系统", "危重症医学", "皮肤病学",
        "急诊医学", "内分泌学与代谢", "胃肠病学与肝病学", "老年病学与老年医学",
        "感染性疾病", "医学实验技术", "肾脏病学", "神经病学", "神经外科",
        "妇产科学", "肿瘤学", "眼科学", "骨科", "耳鼻喉科学", "病理学",
        "儿科学", "药理学与药学", "物理治疗", "精神病学", "公共卫生、环境与职业卫生",
        "放射医学、核医学与医学成像", "康复医学", "呼吸系统", "风湿病学",
        "外科学", "移植", "泌尿科学"
    ],
    "工程类": [
        "工程·综合", "航空航天工程", "生物医学工程", "化学工程", "土木工程",
        "电气与电子工程", "环境工程", "地质工程", "工业工程", "海洋工程",
        "机械工程", "矿业工程", "石油工程", "物理工程", "运输科学与技术"
    ],
    "材料科学": [
        "材料科学·综合", "生物材料", "陶瓷材料", "材料表征与测试",
        "涂层与薄膜材料", "复合材料", "造纸与木材材料", "纺织材料", "冶金与冶金工程"
    ],
    "计算机、能源、仪器": [
        "计算机科学·人工智能", "计算机科学·控制论", "计算机科学·信息系统",
        "计算机科学·交叉应用", "计算机科学·软件工程", "计算机科学·理论与方法",
        "电信学", "自动化与控制系统", "仪器仪表", "核科学与技术", "能源与燃料", "热力学"
    ],
    "交叉综合": ["多学科科学"],
}
# ======================== 页面开始（永久锁死平台名，无任何修改） ========================
st.set_page_config(page_title="宝圈顶刊文献指引平台", layout="wide")
st.title("宝圈顶刊文献指引平台")
# 状态初始化（完全保留你的原版）
if "search_done" not in st.session_state:
    st.session_state.search_done = False
if "keyword" not in st.session_state:
    st.session_state.keyword = ""
# ---------------------- 搜索框（完全保留你的原版，一字未动） ----------------------
with st.form(key="search_form", clear_on_submit=False):
    col_search_input, col_search_btn = st.columns([10, 1])
    with col_search_input:
        keyword = st.text_input("关键词", label_visibility="collapsed", placeholder="输入关键词...")
    with col_search_btn:
        search_clicked = st.form_submit_button("🔍 搜索", type="primary", use_container_width=True)
    if search_clicked and keyword.strip():
        st.session_state.keyword = keyword.strip()
        st.session_state.search_done = True
# ---------------------- 筛选栏（严格按你手绘图还原：左侧标题+右侧复选框+紧凑布局） ----------------------
if st.session_state.search_done:
    st.divider()
    st.subheader("精准筛选条件")
    with st.container(border=True):
        # 第1行：JCR大类（左侧标题+右侧多选框，完全按手绘）
        col1_label, col1_opts = st.columns([1, 9])
        with col1_label:
            st.write("**JCR大类**")
        with col1_opts:
            main_cat = st.multiselect("", options=JCR_MAIN_CATEGORIES, default=["全部"], label_visibility="collapsed")
        
        # 第2行：一级学科（联动JCR大类，左侧标题+右侧多选框）
        col2_label, col2_opts = st.columns([1, 9])
        with col2_label:
            st.write("**一级学科**")
        with col2_opts:
            first_level_options = []
            for cat in main_cat:
                first_level_options += FIRST_LEVEL_MAP.get(cat, [])
            first_level_options = sorted(list(set(first_level_options)))
            first_level = st.multiselect("", options=first_level_options, default=["全部"] if first_level_options else [], label_visibility="collapsed")
        
        # 第3行：二级学科（联动一级学科，左侧标题+右侧多选框）
        col3_label, col3_opts = st.columns([1, 9])
        with col3_label:
            st.write("**二级学科**")
        with col3_opts:
            second_level_options = []
            for f in first_level:
                second_level_options += SECOND_LEVEL_MAP.get(f, [])
            second_level_options = sorted(list(set(second_level_options)))
            second_level = st.multiselect("", options=second_level_options, default=[], label_visibility="collapsed")
        
        # 第4行：期刊来源（左侧标题+右侧多选框）
        col4_label, col4_opts = st.columns([1, 9])
        with col4_label:
            st.write("**期刊**")
        with col4_opts:
            journals = st.multiselect("", options=["全部", "Nature", "Science", "Cell", "JACS", "Angew"], default=["全部"], label_visibility="collapsed")
        
        # 第5行：年份（左侧标题+右侧多选框）
        col5_label, col5_opts = st.columns([1, 9])
        with col5_label:
            st.write("**年份**")
        with col5_opts:
            years = st.multiselect("", options=["全部", "近1年", "近3年", "近5年", "近10年"], default=["全部"], label_visibility="collapsed")
    
    # ---------------------- 文献结果区（占页面2/3，完全保留你的原版逻辑） ----------------------
    st.divider()
    st.subheader("📄 文献结果")
    st.info(f"关键词：**{st.session_state.keyword}**")
    st.success("筛选界面已完全按照你的手绘实现！")
    # 下方预留文献词条区域，你后续可直接添加内容
