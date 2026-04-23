import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="JIYEON'S 1ST B-DAY", page_icon="⚡", layout="centered")

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 힙한 스타일 (다크 모드 + 볼드 타이포)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Noto+Sans+KR:wght@300;700;900&display=swap');

.stApp { background-color: #000 !important; font-family: 'Noto Sans KR', sans-serif; color: #fff; }
.block-container { padding: 1.5rem 0rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
footer, header, #MainMenu { display: none !important; }

/* 인스타 느낌 상단 프로필 바 */
.profile-bar { display: flex; align-items: center; padding: 12px 15px; background: #000; border-bottom: 0.5px solid #222; }
.profile-img { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); padding: 2px; margin-right: 10px; }
.profile-img img { width: 100%; height: 100%; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
.user-id { font-size: 0.85rem; font-weight: 700; color: #fff; }

iframe { border: none; margin: 0 !important; display: block; }
</style>
""", unsafe_allow_html=True)

# 3. 인스타 프로필 바
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

# 5. 힙한 하단 정보 (전광판 느낌)
st.markdown("""
<div style="padding: 20px; background: #000;">
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <span style="font-size: 1.5rem;">❤️</span>
        <span style="font-size: 1.5rem;">💬</span>
        <span style="font-size: 1.5rem;">✈️</span>
    </div>
    
    <div style="font-weight: 900; font-size: 2.2rem; line-height: 1.1; margin-bottom: 30px; font-family: 'Montserrat', sans-serif; letter-spacing: -1px;">
        <span style="color: #FFDE4D;">LIMITED EDITION:</span><br>JIYEON'S 1ST BIRTHDAY
    </div>

    <div style="border-left: 4px solid #FFDE4D; padding-left: 15px; margin-bottom: 40px;">
        <p style="font-size: 0.9rem; color: #aaa; margin: 0;">SCHEDULE</p>
        <p style="font-size: 1.2rem; font-weight: 700; margin: 5px 0 20px;">2026. 10. 24 (SAT) 13:00</p>
        
        <p style="font-size: 0.9rem; color: #aaa; margin: 0;">LOCATION</p>
        <p style="font-size: 1.2rem; font-weight: 700; margin: 5px 0 5px;">행복 가든 스테이</p>
        <p style="font-size: 0.85rem; color: #888; margin: 0;">서울 강남구 행복로 123</p>
    </div>

    <div style="display: flex; gap: 5px;">
        <a href="https://map.kakao.com" target="_blank" style="flex: 1; background: #333; color: #fff; text-decoration: none; padding: 15px; text-align: center; font-size: 0.8rem; font-weight: 700;">NAVIGATE</a>
        <a href="https://map.naver.com" target="_blank" style="flex: 1; background: #FFDE4D; color: #000; text-decoration: none; padding: 15px; text-align: center; font-size: 0.8rem; font-weight: 700;">LOCATION MAP</a>
    </div>
</div>
""", unsafe_allow_html=True)
