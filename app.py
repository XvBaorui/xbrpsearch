import streamlit as st

# ====================== 永久锁死！谁也不准改！ ======================
# 平台名：宝圈
# 副标题：顶刊文献检索平台
# 没有横杠！没有JCR！没有我加的任何东西！
# ==================================================================

st.set_page_config(page_title="宝圈", layout="wide")

# 初始化页面
if "page" not in st.session_state:
    st.session_state.page = "search"
if "keyword" not in st.session_state:
    st.session_state.keyword = ""

# ---------------------- 页面1：搜索页 ----------------------
if st.session_state.page == "search":

    # 永久标题
    st.title("宝圈")
    st.subheader("顶刊文献检索平台")

    st.divider()

    # 搜索框
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        with st.form("search_form"):
            keyword = st.text_input(
                "",
                placeholder="输入关键词...",
                label_visibility="collapsed"
            )
            submitted = st.form_submit_button("🔍 搜索", type="primary", use_container_width=True)

        if submitted and keyword.strip():
            st.session_state.keyword = keyword.strip()
            st.session_state.page = "result"
            st.rerun()

# ---------------------- 页面2：搜索后才出现的筛选页 ----------------------
elif st.session_state.page == "result":

    # 顶部返回
    if st.button("🔙 返回搜索"):
        st.session_state.page = "search"
        st.rerun()

    st.title("宝圈")
    st.subheader("顶刊文献检索平台")
    st.divider()

    # 筛选区（你要的那种平铺样式）
    st.write("#### 筛选条件")

    # 学科1
    col_lab1, col_opt1 = st.columns([1, 9])
    with col_lab1:
        st.write("**学科门类**")
    with col_opt1:
        st.multiselect("学科门类", ["全部", "自然科学", "社会科学", "艺术与人文"], default=["全部"], label_visibility="collapsed", key="cat1")

    # 学科2
    col_lab2, col_opt2 = st.columns([1, 9])
    with col_lab2:
        st.write("**一级学科**")
    with col_opt2:
        st.multiselect("一级学科", ["全部", "化学", "物理", "生物", "材料"], default=["全部"], label_visibility="collapsed", key="cat2")

    # 期刊
    col_lab3, col_opt3 = st.columns([1, 9])
    with col_lab3:
        st.write("**期刊**")
    with col_opt3:
        st.multiselect("期刊", ["全部", "JACS", "Angew", "Nature", "Science"], default=["全部"], label_visibility="collapsed", key="cat3")

    # 年份
    col_lab4, col_opt4 = st.columns([1, 9])
    with col_lab4:
        st.write("**年份**")
    with col_opt4:
        st.multiselect("年份", ["全部", "近3年", "近5年", "近10年"], default=["全部"], label_visibility="collapsed", key="cat4")

    st.divider()

    # 文献结果
    st.write("#### 文献结果")
    st.info(f"关键词：{st.session_state.keyword}")
    st.success("下面是搜到的文献")
