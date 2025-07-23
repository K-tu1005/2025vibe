import streamlit as st
import random

# 전체 메뉴 (이름, 열량, 가격 포함)
default_menus = {
    "한식": [
        {"name": "김치찌개", "cal": 450, "price": 8000},
        {"name": "비빔밥", "cal": 550, "price": 9000},
        {"name": "불고기", "cal": 600, "price": 11000},
        {"name": "된장찌개", "cal": 400, "price": 7000},
        {"name": "삼겹살", "cal": 800, "price": 12000}
    ],
    "중식": [
        {"name": "짜장면", "cal": 700, "price": 7000},
        {"name": "짬뽕", "cal": 750, "price": 8000},
        {"name": "탕수육", "cal": 900, "price": 13000},
        {"name": "마라탕", "cal": 850, "price": 11000},
        {"name": "볶음밥", "cal": 650, "price": 7500}
    ],
    "일식": [
        {"name": "스시", "cal": 500, "price": 15000},
        {"name": "라멘", "cal": 650, "price": 9000},
        {"name": "우동", "cal": 450, "price": 7000},
        {"name": "가츠동", "cal": 700, "price": 8500},
        {"name": "규동", "cal": 650, "price": 8000}
    ],
    "양식": [
        {"name": "파스타", "cal": 750, "price": 11000},
        {"name": "스테이크", "cal": 900, "price": 20000},
        {"name": "피자", "cal": 850, "price": 15000},
        {"name": "햄버거", "cal": 800, "price": 8000},
        {"name": "샐러드", "cal": 300, "price": 7000}
    ],
    "분식": [
        {"name": "떡볶이", "cal": 600, "price": 5000},
        {"name": "순대", "cal": 450, "price": 4000},
        {"name": "오뎅", "cal": 250, "price": 3000},
        {"name": "라볶이", "cal": 750, "price": 6000},
        {"name": "김밥", "cal": 400, "price": 3000}
    ],
    "패스트푸드": [
        {"name": "치킨버거", "cal": 850, "price": 6500},
        {"name": "감자튀김", "cal": 400, "price": 2500},
        {"name": "핫도그", "cal": 500, "price": 3500},
        {"name": "치킨너겟", "cal": 600, "price": 5000}
    ],
    "베이커리": [
        {"name": "크로와상", "cal": 350, "price": 3000},
        {"name": "샌드위치", "cal": 550, "price": 6000},
        {"name": "베이글", "cal": 400, "price": 3500},
        {"name": "스콘", "cal": 450, "price": 3200}
    ],
    "채식": [
        {"name": "채소비빔밥", "cal": 450, "price": 8000},
        {"name": "두부스테이크", "cal": 500, "price": 9000},
        {"name": "비건샐러드", "cal": 350, "price": 8500}
    ],
    "디저트": [
        {"name": "케이크", "cal": 450, "price": 5000},
        {"name": "아이스크림", "cal": 300, "price": 3000},
        {"name": "팥빙수", "cal": 550, "price": 6000}
    ]
}

# 페이지 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")
st.title("🍽️ 오늘 뭐 먹지?")
st.write("점심 메뉴를 **열량**과 **가격** 정보와 함께 추천해드립니다!")

# 세션 상태에 사용자 메뉴 저장
if "custom_menus" not in st.session_state:
    st.session_state.custom_menus = {k: v.copy() for k, v in default_menus.items()}

# 카테고리 선택
categories = list(st.session_state.custom_menus.keys())
selected_categories = st.multiselect("🍛 먹고 싶은 음식 종류를 선택하세요:", categories, default=categories)

# 제외할 메뉴 이름만 리스트로 추출
def get_menu_names(menu_list):
    return [m["name"] for m in menu_list]

all_selected_menus = sum([st.session_state.custom_menus[cat] for cat in selected_categories], [])
excluded_names = st.multiselect("🚫 제외하고 싶은 메뉴를 선택하세요:", get_menu_names(all_selected_menus))

# 추천 버튼
if st.button("🎲 메뉴 추천받기!"):
    filtered_menus = [
        menu for cat in selected_categories
        for menu in st.session_state.custom_menus[cat]
        if menu["name"] not in excluded_names
    ]
    
    if filtered_menus:
        chosen = random.choice(filtered_menus)
        st.success(f"오늘의 추천 메뉴는 **{chosen['name']}** 입니다!")
        st.info(f"🔥 열량: {chosen['cal']} kcal / 💰 가격: ₩{chosen['price']:,}")
    else:
        st.warning("추천할 수 있는 메뉴가 없어요. 선택 범위를 다시 확인해 주세요!")

# 사용자 메뉴 추가
with st.expander("➕ 메뉴 직접 추가하기"):
    new_menu_name = st.text_input("메뉴 이름:")
    new_menu_cal = st.number_input("칼로리 (kcal):", min_value=0, max_value=2000, step=10)
    new_menu_price = st.number_input("가격 (₩):", min_value=0, max_value=50000, step=500)
    new_menu_cat = st.selectbox("카테고리 선택:", categories)
    
    if st.button("✅ 메뉴 추가"):
        if new_menu_name:
            new_menu = {"name": new_menu_name, "cal": new_menu_cal, "price": new_menu_price}
            st.session_state.custom_menus[new_menu_cat].append(new_menu)
            st.success(f"{new_menu_name} 메뉴가 {new_menu_cat}에 추가되었습니다.")
        else:
            st.warning("메뉴 이름을 입력해주세요.")

# 현재 메뉴 보기
with st.expander("📋 현재 메뉴 목록 보기"):
    for cat in selected_categories:
        st.markdown(f"### 🍽️ {cat}")
        for menu in st.session_state.custom_menus[cat]:
            st.markdown(f"- **{menu['name']}** (🔥 {menu['cal']} kcal / 💰 ₩{menu['price']:,})")
