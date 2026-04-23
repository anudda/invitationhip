import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="JIYEON'S 1ST B-DAY", page_icon="⚡", layout="centered")

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 스타일 설정 (프로필 바 여백 수정)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Noto+Sans+KR:wght@300;700;900&display=swap');
.stApp { background-color: #000 !important; font-family: 'Noto Sans KR', sans-serif; color: #fff; }
.block-container { padding: 1rem 0rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
footer, header, #MainMenu { display: none !important; }

/* 프로필 바: 아이콘과 아이디 사이 간격 강화 */
.profile-bar { display: flex; align-items: center; padding: 15px; background: #000; border-bottom: 0.5px solid #222; }
.profile-img { width: 34px; height: 34px; border-radius: 50%; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding: 2px; margin-right: 15px; flex-shrink: 0; }
.profile-img img { width: 100%; height: 100%; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
.user-id { font-size: 0.9rem; font-weight: 700; color: #fff; letter-spacing: 0.5px; }

iframe { border: none; margin: 0 !important; display: block; width: 100%; }
</style>
""", unsafe_allow_html=True)

# 3. 데이터 준비
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
b64_photos = [get_b64(p) for p in photos]

st.markdown(f"""
<div class="profile-bar">
    <div class="profile-img"><img src="{b64_photos[0]}"></div>
    <div class="user-id">jiyeon_is_coming_2026</div>
</div>
""", unsafe_allow_html=True)

# 4. 힙 매거진 슬라이더 (PC 겹침 방지 여백 추가)
album_html = f"""
<style>
    body {{ margin: 0; background: #000; overflow: hidden; padding-bottom: 20px; }}
    .main-box {{ position: relative; width: 100%; height: 420px; overflow: hidden; }}
    #m {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }}
    .overlay-text {{ position: absolute; bottom: 15px; left: 15px; font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 3.5rem; line-height: 0.8; color: #fff; mix-blend-mode: overlay; opacity: 0.7; pointer-events: none; }}
    /* 썸네일 영역 하단 여백 확보 */
    .row {{ display: flex; overflow-x: auto; gap: 4px; padding: 10px 5px 25px; background: #000; scrollbar-width: none; }}
    .row::-webkit-scrollbar {{ display: none; }}
    .t {{ width: 85px; height: 85px; flex-shrink: 0; object-fit: cover; opacity: 0.4; cursor: pointer; border-radius: 4px; }}
    .active {{ opacity: 1 !important; border: 2px solid #fff; }}
</style>
<div class="main-box">
    <img id="m" src="{b64_photos[0]}">
    <div class="overlay-text">01<br>ST.</div>
</div>
<div class="row">
    {"".join([f'<img class="t" src="{p}" onclick="s(this, \'{p}\', {i})">' for i, p in enumerate(b64_photos)])}
</div>
<script>
    function s(el, src, i) {{
        document.getElementById('m').src = src;
        document.querySelector('.overlay-text').innerHTML = "0" + (i+1) + "<br>ST.";
        document.querySelectorAll('.t').forEach(t => t.classList.remove('active'));
        el.classList.add('active');
    }}
    document.querySelector('.t').classList.add('active');
</script>
"""
# 높이를 넉넉히 주어 PC에서도 아래 요소와 겹치지 않게 조절
components.html(album_html, height=570)

# 5. 하단 정보 카드 (여백 최적화)
st.markdown("""
<div style="padding: 10px 20px 40px; background: #000; position: relative; z-index: 10;">
    <div style="display: flex; gap: 18px; margin-bottom: 25px; padding-left: 5px;">
        <span style="font-size: 1.5rem; cursor: pointer;">❤️</span>
        <span style="font-size: 1.5rem; cursor: pointer;">💬</span>
        <span style="font-size: 1.5rem; cursor: pointer;">✈️</span>
    </div>
    <div style="font-weight: 900; font-size: 2.2rem; line-height: 1.1; margin-bottom: 30px; font-family: 'Montserrat', sans-serif; letter-spacing: -1px; color: #FFF;">
        <span style="color: #FFDE4D;">LIMITED EDITION:</span><br>JIYEON'S 1ST BIRTHDAY
    </div>
    <div style="border-left: 4px solid #FFDE4D; padding-left: 18px; margin-bottom: 40px;">
        <p style="font-size: 0.8rem; color: #888; margin: 0; letter-spacing: 1px; font-weight: 700;">SCHEDULE</p>
        <p style="font-size: 1.15rem; font-weight: 700; margin: 6px 0 22px; color: #FFF;">2026. 10. 24 (SAT) 13:00</p>
        <p style="font-size: 0.8rem; color: #888; margin: 0; letter-spacing: 1px; font-weight: 700;">LOCATION</p>
        <p style="font-size: 1.15rem; font-weight: 700; margin: 6px 0 6px; color: #FFF;">행복 가든 스테이</p>
        <p style="font-size: 0.9rem; color: #777; margin: 0;">서울 강남구 행복로 123</p>
    </div>
    <div style="display: flex; gap: 10px; padding-bottom: 20px;">
        <a href="https://map.kakao.com" target="_blank" style="flex: 1; background: #252525; color: #fff; text-decoration: none; padding: 16px 0; text-align: center; font-size: 0.8rem; font-weight: 700; border-radius: 8px; letter-spacing: 1px;">NAVIGATE</a>
        <a href="https://map.naver.com" target="_blank" style="flex: 1; background: #FFDE4D; color: #000; text-decoration: none; padding: 16px 0; text-align: center; font-size: 0.8rem; font-weight: 700; border-radius: 8px; letter-spacing: 1px;">MAP</a>
    </div>
    <p style="color: #444; font-size: 0.8rem; margin-top: 40px; font-style: italic; letter-spacing: 1px; text-align: center;">Created with love for Jiyeon.</p>
</div>
""", unsafe_allow_html=True)
