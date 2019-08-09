# likelion7th_hackaton
 멋쟁이사자처럼 7기 해커톤 레포지토리입니다. (주제: 내가 원하는 카페 서비스) 
 
 # Requirements
 <ul>
    <li>가상환경 myvenv 설치</li>
    <li> cd cafeproject 하시고 pip install django-taggit</li>
    <li>pip install django-taggit-templatetags</li>
    <li>makemigrations, migrate</li>
    <li> 같은 경로에서 git rm --cached *.pyc 명령어 입력 (pyc 파일 변경 사항 미적용되도록)</li>
</ul>
 <br/>

 
# 기능
- [ ] 디자인
- [x] 태그로 검색
- [ ] 1~3등 카페 추천 (좋아요 수 기준)
- [x] 회원가입
- [x] 로그인
- [ ] 지도 API로 카페 위치 제공
- [ ] 게시물 업로드 기능 (카페 이름, 위치, 태그, 사진, 글)
- [x] 댓글 기능 (유저별로 이름 다르게)
- [ ] 좋아요 기능 (유저별로 이름 다르게, 숫자 count)
- [ ] 좋아요 수가 바뀌거나 게시물이 삭제되면 재정렬
