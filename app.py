import streamlit as st
import re
from datetime import datetime

# ====================== 全局配置 ======================
st.set_page_config(
    page_title="宝圈顶刊文献指引平台",
    layout="wide",
    menu_items={},
    initial_sidebar_state="collapsed"
)

# 全局样式（简约学术风、全端适配、仿知网/百度）
st.markdown("""
<style>
html, body {
    font-family: "Microsoft YaHei", sans-serif;
    background-color: #f9f9f9;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
/* 筛选栏左侧标题样式 */
.filter-label {
    background-color: #333;
    color: white;
    padding: 0.6rem 1rem;
    border-radius: 0.3rem;
    font-weight: bold;
    text-align: center;
}
/* 搜索框 */
.search-input input {
    height: 3rem !important;
    font-size: 1rem !important;
}
.search-btn button {
    height: 3rem !important;
    font-size: 1.1rem !important;
    background-color: #d93025 !important;
    color: white !important;
    border: none;
}
/* 隐藏右下角工具栏 */
[data-testid="stToolbar"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

# ====================== 会话状态初始化 ======================
if "users" not in st.session_state:
    st.session_state.users = {}  # {username: {"pwd":..., "profile":...}}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "need_profile" not in st.session_state:
    st.session_state.need_profile = False
if "search_keyword" not in st.session_state:
    st.session_state.search_keyword = ""
if "page" not in st.session_state:
    st.session_state.page = "auth"  # auth, profile, home, search

# ====================== 学科联动数据 ======================
SUBJECT_MAP = {
    "化学类": [
        "化学·综合", "应用化学", "分析化学", "无机与核化学", "有机化学",
        "物理化学", "高分子科学", "电化学", "光谱学", "晶体学"
    ],
    "生物与生化类": [
        "生物化学与分子生物学", "生物物理学", "细胞生物学", "发育生物学",
        "生态学", "昆虫学", "进化生物学", "遗传学与遗传", "微生物学",
        "真菌学", "神经科学", "生理学", "植物科学", "动物学", "生物学",
        "生物多样性保护", "海洋与淡水生物学", "鸟类学", "寄生虫学",
        "病毒学", "生殖生物学", "生化研究方法", "生物技术与应用微生物学"
    ],
    "农业与食品类": [
        "农业·综合", "农业·乳品与动物科学", "农艺学", "园艺学", "土壤科学",
        "渔业", "林学", "食品科学与技术", "兽医学", "农业经济与政策",
        "农业工程", "绿色与可持续科学技术"
    ],
    "工程类": [
        "工程·综合", "航空航天工程", "生物医学工程", "化学工程", "土木工程",
        "电气与电子工程", "环境工程", "地质工程", "工业工程", "海洋工程",
        "机械工程", "矿业工程", "石油工程", "物理工程", "运输科学与技术"
    ],
    "材料科学类": [
        "材料科学·综合", "生物材料", "陶瓷材料", "材料表征与测试",
        "涂层与薄膜材料", "复合材料", "造纸与木材材料", "纺织材料",
        "冶金与冶金工程"
    ]
}

# ====================== 工具函数 ======================
def check_username_format(s):
    return re.fullmatch(r"^[A-Za-z0-9]+$", s) is not None

def check_pwd_format(s):
    return re.fullmatch(r"^[A-Za-z0-9]+$", s) is not None

# ====================== 页面1：登录/注册 ======================
def page_auth():
    st.title("用户登录 / 注册")
    tab1, tab2 = st.tabs(["登录", "注册"])

    with tab1:
        username = st.text_input("账号（字母+数字）", key="login_user")
        pwd = st.text_input("密码", type="password", key="login_pwd")
        if st.button("登录"):
            if not username or not pwd:
                st.warning("请输入账号和密码")
            elif username not in st.session_state.users:
                st.error("账号不存在")
            elif st.session_state.users[username]["pwd"] != pwd:
                st.error("密码错误")
            else:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                profile = st.session_state.users[username].get("profile", None)
                if profile is None:
                    st.session_state.need_profile = True
                    st.session_state.page = "profile"
                else:
                    st.session_state.page = "home"
                st.rerun()

    with tab2:
        new_user = st.text_input("设置账号（字母+数字）", key="reg_user")
        new_pwd = st.text_input("设置密码（字母+数字）", type="password", key="reg_pwd")
        confirm_pwd = st.text_input("确认密码", type="password", key="reg_cfm")
        if st.button("注册"):
            if not check_username_format(new_user):
                st.warning("账号只能包含大小写字母和数字")
            elif not check_pwd_format(new_pwd):
                st.warning("密码只能包含大小写字母和数字")
            elif new_pwd != confirm_pwd:
                st.error("两次密码不一致")
            elif new_user in st.session_state.users:
                st.error("账号已存在")
            else:
                st.session_state.users[new_user] = {
                    "pwd": new_pwd,
                    "profile": None
                }
                st.success("注册成功！请完善资料")
                st.session_state.logged_in = True
                st.session_state.current_user = new_user
                st.session_state.need_profile = True
                st.session_state.page = "profile"
                st.rerun()

# ====================== 页面2：完善资料 ======================
def page_profile():
    st.title("完善个人资料")
    st.markdown("⚠️ 昵称与头像为必填项")

    nickname = st.text_input("昵称（必填）")
    avatar = st.file_uploader("上传头像（必填，仅图片）", type=["png","jpg","jpeg"])
    unit = st.text_input("工作单位（选填）")
    birthday = st.date_input("出生年月日（选填）", min_value=datetime(1940,1,1))
    tags = st.multiselect("感兴趣的学科标签（选填，可多选）", list(SUBJECT_MAP.keys()))

    if st.button("提交资料"):
        if not nickname:
            st.warning("请填写昵称")
        elif avatar is None:
            st.warning("请上传头像")
        else:
            st.session_state.users[st.session_state.current_user]["profile"] = {
                "nickname": nickname,
                "avatar": avatar.name if avatar else None,
                "unit": unit,
                "birthday": str(birthday),
                "tags": tags
            }
            st.session_state.need_profile = False
            st.session_state.page = "home"
            st.success("资料完善成功，进入平台")
            st.rerun()

# ====================== 页面3：主页（搜索页） ======================
def page_home():
    # 标题
    st.markdown("<h1 style='text-align:center; font-weight:bold;'>宝圈顶刊文献指引平台</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:right; color:#d93025; margin-bottom:2rem;'>专注顶刊文献精确检索与指引</h3>", unsafe_allow_html=True)

    # 搜索栏（支持回车）
    col1, col2 = st.columns([9, 2])
    with col1:
        keyword = st.text_input("", placeholder="输入关键词检索文献", label_visibility="collapsed", key="search_input")
    with col2:
        st.write("")
        search_clicked = st.button("搜索", type="primary", use_container_width=True)

    # 触发搜索：按钮 或 回车
    if (search_clicked or st.session_state.get("search_input")) and keyword.strip():
        st.session_state.search_keyword = keyword.strip()
        st.session_state.page = "search_result"
        st.rerun()

    st.divider()
    st.info("输入关键词后点击搜索或按回车，即可进入检索筛选页面")

# ====================== 页面4：搜索结果+筛选 ======================
def page_search_result():
    st.markdown(f"<h3 style='margin-bottom:1rem;'>检索关键词：{st.session_state.search_keyword}</h3>", unsafe_allow_html=True)
    st.divider()

    st.subheader("筛选条件")

    # 一级学科
    col_l1, col_r1 = st.columns([1, 11])
    with col_l1:
        st.markdown('<div class="filter-label">一级学科</div>', unsafe_allow_html=True)
    with col_r1:
        first_opts = ["全部"] + list(SUBJECT_MAP.keys())
        selected_first = st.multiselect("", first_opts, default=["全部"], label_visibility="collapsed", key="first")

    # 二级学科（联动）
    col_l2, col_r2 = st.columns([1, 11])
    with col_l2:
        st.markdown('<div class="filter-label">二级学科</div>', unsafe_allow_html=True)
    with col_r2:
        second_list = ["全部"]
        if "全部" not in selected_first:
            for cat in selected_first:
                second_list += SUBJECT_MAP.get(cat, [])
        second_list = sorted(list(set(second_list)))
        st.multiselect("", second_list, default=["全部"], label_visibility="collapsed", key="second")

    # 年份
    col_l3, col_r3 = st.columns([1, 11])
    with col_l3:
        st.markdown('<div class="filter-label">发表年份</div>', unsafe_allow_html=True)
    with col_r3:
        year_opts = ["全部", "近3年", "近5年", "近10年"]
        st.multiselect("", year_opts, default=["全部"], label_visibility="collapsed", key="year")

    st.divider()
    st.subheader("文献检索结果")
    st.info("文献数据待导入，此处将展示标题、作者、期刊、年份、摘要、链接等信息")

    # 返回
    if st.button("← 返回搜索页"):
        st.session_state.page = "home"
        st.rerun()

# ====================== 路由 ======================
if not st.session_state.logged_in:
    page_auth()
else:
    if st.session_state.need_profile:
        page_profile()
    else:
        if st.session_state.page == "home":
            page_home()
        elif st.session_state.page == "search_result":
            page_search_result()
