import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="JIYEON'S 1ST B-DAY", page_icon="⚡", layout="centered")

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 통합 스타일 설정
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Noto+Sans+KR:wght@300;700;900&display=swap');
.stApp { background-color: #000 !important; font-family: 'Noto Sans KR', sans-serif; color: #fff; }
.block-container { padding: 1rem 0rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
footer, header, #MainMenu { display: none !important; }
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

# 프로필 바 (f-string 최소화)
st.markdown(f'<div class="profile-bar"><div class="profile-img"><img src="{b64_photos[0]}"></div><div class="user-id">JIYEON\'S 1ST B-DAY</div></div>', unsafe_allow_html=True)

# 4. 앨범 컴포넌트
album_html = f"""
<style>
    body {{ margin: 0; background: #000; overflow: hidden; }}
    .main-box {{ position: relative; width: 100%; height: 420px; overflow: hidden; }}
    #m {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }}
    .overlay-text {{ position: absolute; bottom: 15px; left: 15px; font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 3.5rem; line-height: 0.8; color: #fff; mix-blend-mode: overlay; opacity: 0.7; pointer-events: none; }}
    .row {{ display: flex; overflow-x: auto; justify-content: center; gap: 6px; padding: 10px 10px 15px; background: #000; scrollbar-width: none; }}
    .t {{ width: 80px; height: 80px; flex-shrink: 0; object-fit: cover; opacity: 0.4; cursor: pointer; border-radius: 4px; border: 2px solid transparent; }}
    .active {{ opacity: 1 !important; border: 2px solid #fff; }}
</style>
<div class="main-box"><img id="m" src="{b64_photos[0]}"></div>
<div class="row">{"".join([f'<img class="t" src="{p}" onclick="s(this, \'{p}\', {i})">' for i, p in enumerate(b64_photos)])}</div>
<script>
    function s(el, src, i) {{
        document.getElementById('m').src = src;
        document.querySelectorAll('.t').forEach(t => t.classList.remove('active'));
        el.classList.add('active');
    }}
    document.querySelector('.t').classList.add('active');
</script>
"""
components.html(album_html, height=540)

# 5. [해결] 캡션, 아이콘, 정보 카드 통합 렌더링
# f-string을 빼고 순수 HTML로 작성하여 코드 노출을 완벽 차단했습니다.
st.markdown("""
<div style="padding: 0px 20px 40px; background: #000; position: relative; z-index: 10;">
    <div style="padding: 10px 5px 25px 5px; line-height: 1.6;">
        <span style="font-weight: 700; font-size: 0.95rem; margin-right: 8px;">JIYEON'S 1ST B-DAY</span>
        <span style="font-size: 0.9rem; color: #efefef;">지연이가 세상에 온 지 벌써 일 년이 되었어요! 🐣<br>소중한 분들과 함께 지연이의 첫 생일을 기념하고 싶습니다.<br>귀한 발걸음 하셔서 많이 축하해 주세요. ❤️</span>
        <p style="font-size: 0.8rem; color: #8e8e8e; margin-top: 8px; margin-bottom: 0;">#첫돌 #돌잔치 #공주님 #초대합니다</p>
    </div>
    <div style="display: flex; gap: 18px; margin-bottom: 25px; padding-left: 5px; border-top: 0.5px solid #222; padding-top: 20px;">
        <span style="font-size: 1.5rem; cursor: default;">❤️</span>
        <span style="font-size: 1.5rem; cursor: default;">💬</span>
        <span style="font-size: 1.5rem; cursor: default;">✈️</span>
    </div>
    <div style="font-weight: 900; font-size: 2.2rem; line-height: 1.1; margin-bottom: 30px; font-family: 'Montserrat', sans-serif; letter-spacing: -1px; color: #FFF;">
        <span style="color: #FFDE4D;">PRIVATE INVITATION:</span><br>JIYEON'S 1ST BIRTHDAY
    </div>
    <div style="border-left: 4px solid #FFDE4D; padding-left: 18px; margin-bottom: 40px;">
        <p style="font-size: 0.8rem; color: #888; margin: 0; letter-spacing: 1px; font-weight: 700;">SCHEDULE</p>
        <p style="font-size: 1.15rem; font-weight: 700; margin: 6px 0 22px; color: #FFF;">2026. 10. 24 (SAT) 13:00</p>
        <p style="font-size: 0.8rem; color: #888; margin: 0; letter-spacing: 1px; font-weight: 700;">LOCATION</p>
        <p style="font-size: 1.15rem; font-weight: 700; margin: 6px 0 6px; color: #FFF;">행복 가든 스테이</p>
        <p style="font-size: 0.9rem; color: #777; margin: 0;">서울 강남구 행복로 123</p>
    </div>
    <div style="display: flex; gap: 10px; padding-bottom: 20px;">
        <a href="https://map.kakao.com" target="_blank" style="flex: 1; background: #252525; color: #fff; text-decoration: none; padding: 16px 0; text-align: center; font-size: 0.8rem; font-weight: 700; border-radius: 8px; letter-spacing: 1px;">KAKAO MAP</a>
        <a href="https://map.naver.com" target="_blank" style="flex: 1; background: #FFDE4D; color: #000; text-decoration: none; padding: 16px 0; text-align: center; font-size: 0.8rem; font-weight: 700; border-radius: 8px; letter-spacing: 1px;">NAVER MAP</a>
    </div>
    <p style="color: #444; font-size: 0.8rem; margin-top: 40px; font-style: italic; letter-spacing: 1px; text-align: center;">Copyright © 2026 JIYEON. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
