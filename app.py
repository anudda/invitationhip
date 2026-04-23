import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="JIYEON'S 1ST B-DAY", page_icon="⚡", layout="centered")

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 스타일 설정 (코드 노출 방지를 위해 빈 줄 제거)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Noto+Sans+KR:wght@300;700;900&display=swap');
.stApp { background-color: #000 !important; font-family: 'Noto Sans KR', sans-serif; color: #fff; }
.block-container { padding: 1.5rem 0rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
footer, header, #MainMenu { display: none !important; }
.profile-bar { display: flex; align-items: center; padding: 12px 15px; background: #000; border-bottom: 0.5px solid #222; }
.profile-img { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding: 2px; margin-right: 10px; }
.profile-img img { width: 100%; height: 100%; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
.user-id { font-size: 0.85rem; font-weight: 700; color: #fff; }
iframe { border: none; margin: 0 !important; display: block; }
</style>
""", unsafe_allow_html=True)

# 3. 데이터 준비 및 프로필 바
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
b64_photos = [get_b64(p) for p in photos]

st.markdown(f"""
<div class="profile-bar">
    <div class="profile-img"><img src="{b64_photos[0]}"></div>
    <div class="user-id">jiyeon_is_coming_2026</div>
</div>
""", unsafe_allow_html=True)

# 4. 힙 매거진 슬라이더
album_html = f"""
<style>
    body {{ margin: 0; background: #000; overflow: hidden; }}
    .main-box {{ position: relative; width: 100%; height: 450px; overflow: hidden; }}
    #m {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1); }}
    .overlay-text {{ position: absolute; bottom: 20px; left: 20px; font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 4rem; line-height: 0.8; color: #fff; mix-blend-mode: overlay; opacity: 0.8; pointer-events: none; }}
    .row {{ display: flex; overflow-x: auto; gap: 2px; padding: 5px 0; background: #000; }}
    .t {{ width: 25vw; height: 25vw; flex-shrink: 0; object-fit: cover; opacity: 0.4; cursor: pointer; }}
    .active {{ opacity: 1 !important; border-top: 2px solid #fff; }}
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
components.html(album_html, height=580)

# 5. [해결] 하단 정보 카드 (빈 줄 없이 꽉 채운 구조)
st.markdown("""
<div style="padding: 25px 20px; background: #000; position: relative; z-index: 10;">
    <div style="display: flex; gap: 15px; margin-bottom: 25px;">
        <span style="font-size: 1.4rem;">❤️</span>
        <span style="font-size: 1.4rem;">💬</span>
        <span style="font-size: 1.4rem;">✈️</span>
    </div>
    <div style="font-weight: 900; font-size: 2.1rem; line-height: 1.1; margin-bottom: 30px; font-family: 'Montserrat', sans-serif; letter-spacing: -1px; color: #FFF;">
        <span style="color: #FFDE4D;">LIMITED EDITION:</span><br>JIYEON'S 1ST BIRTHDAY
    </div>
    <div style="border-left: 4px solid #FFDE4D; padding-left: 15px; margin-bottom: 40px; text-align: left;">
        <p style="font-size: 0.8rem; color: #888; margin: 0; letter-spacing: 1px;">SCHEDULE</p>
        <p style="font-size: 1.1rem; font-weight: 700; margin: 5px 0 20px; color: #FFF;">2026. 10. 24 (SAT) 13:00</p>
        <p style="font-size: 0.8rem; color: #888; margin: 0; letter-spacing: 1px;">LOCATION</p>
        <p style="font-size: 1.1rem; font-weight: 700; margin: 5px 0 5px; color: #FFF;">행복 가든 스테이</p>
        <p style="font-size: 0.85rem; color: #666; margin: 0;">서울 강남구 행복로 123</p>
    </div>
    <div style="display: flex; gap: 8px;">
        <a href="https://map.kakao.com" target="_blank" style="flex: 1; background: #222; color: #fff; text-decoration: none; padding: 16px 0; text-align: center; font-size: 0.75rem; font-weight: 700; border-radius: 4px; letter-spacing: 1px;">NAVIGATE</a>
        <a href="https://map.naver.com" target="_blank" style="flex: 1; background: #FFDE4D; color: #000; text-decoration: none; padding: 16px 0; text-align: center; font-size: 0.75rem; font-weight: 700; border-radius: 4px; letter-spacing: 1px;">MAP</a>
    </div>
    <p style="color: #555; font-size: 0.8rem; margin-top: 50px; font-style: italic; letter-spacing: 1px; text-align: center;">With love and gratitude.</p>
</div>
""", unsafe_allow_html=True)
