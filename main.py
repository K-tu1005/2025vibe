import streamlit as st
st.title('나의 첫 웹 서비스 만들기!!')
import streamlit as st
import random

# 기본 메뉴 데이터
default_menus = {
    "한식": ["김치찌개", "비빔밥", "불고기", "된장찌개", "삼겹살"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "볶음밥"],
    "일식": ["스시", "라멘", "우동", "가츠동", "규동"],
    "양식": ["파스타", "스테이크", "피자", "햄버거", "샐러드"]
}

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

st.title("🍽️ 오늘 뭐 먹지?")
st.write("점심 메뉴 고민된다면? 아래에서 골라보세요!")

# 세션 상태에 사용자 메뉴 저장
if "custom_menus" not in st.session_state:
    st.session_state.custom_menus = {k: v.copy() for k, v in default_menus.items()}

# 카테고리 선택
categories = list(st.session_state.custom_menus.keys())
selected_categories = st.multiselect("먹고 싶은 음식 종류를 선택하세요:", categories, default=categories)

# 제외할 메뉴 선택
all_selected_menus = sum([st.session_state.custom_menus[cat] for cat in selected_categories], [])
excluded_menus = st.multiselect("제외하고 싶은 메뉴를 선택하세요:", all_selected_menus)

# 추천 버튼
if st.button("🍱 메뉴 추천받기!"):
    filtered_menus = [menu for cat in selected_categories for menu in st.session_state.custom_menus[cat] if menu not in excluded_menus]
    
    if filtered_menus:
        selected_menu = random.choice(filtered_menus)
        st.success(f"오늘의 추천 메뉴는 **{selected_menu}** 입니다!")
    else:
        st.warning("추천할 수 있는 메뉴가 없어요. 선택 범위를 다시 확인해 주세요!")

# 사용자 메뉴 추가 기능
with st.expander("➕ 메뉴 직접 추가하기"):
    new_menu = st.text_input("메뉴 이름을 입력하세요:")
    new_category = st.selectbox("카테고리를 선택하세요:", categories)
    if st.button("메뉴 추가"):
        if new_menu:
            st.session_state.custom_menus[new_category].append(new_menu)
            st.success(f"{new_menu} 메뉴가 {new_category}에 추가되었습니다.")
        else:
            st.warning("메뉴 이름을 입력해주세요.")

# 현재 메뉴 확인
with st.expander("📋 현재 메뉴 목록 보기"):
    for cat in selected_categories:
        st.markdown(f"**{cat}**: {', '.join(st.session_state.custom_menus[cat])}")
