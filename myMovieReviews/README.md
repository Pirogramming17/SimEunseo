##### 구현한 기능: 1,2,3,4,5,6,7,8,9,10,11
##### 구현하지 못한 기능: X

🔥🔥🔥 챌린지 참여합니다! 🔥🔥🔥</br>

##### 프론트엔드
	1. 기록장이라는 컨셉을 가지고 열심히 꾸며보았습니다😎
	2. media query를 사용하여 반응형을 구현하였습니다😎
		- 리스트 페이지에서 창을 줄일수록 한 줄에 띄워지는 review의 개수가 3->2->1개로 바뀜
		- review 작성/수정 페이지에서 창의 너비에 따라 폼의 너비와 여백이 달라짐
	3. hover할 때 transition과 각종 color등 디자인적인 요소에 신경썼습니다😎
##### 백엔드
	1. 장르를 단순 입력이 아닌 선택 기능으로 변경하였습니다😎
	2. 분 단위로 입력된 러닝타임을 디테일 페이지에서 시간 단위로 변환하여 나타나게 하였습니다😎
	3. 작성시간, 개봉년도, 제목, 별점 순의 정렬 기능을 넣었고, 추가로 오름차순과 내림차순도 선택할 수 있도록 하였습니다😎
##### 유의사항
	1. 리스트 페이지는 http://127.0.0.1:8000/review 입니다.
	2. create/update 시 항목을 입력할 때 자료형이 맞지 않으면 에러가 나게 됩니다. 개봉년도, 별점, 러닝타임은 숫자로, 나머지는 문자열로 입력해야 합니다. 별점의 경우 자료형이 decimal이기 때문에 1을 입력하면 1.0으로 변환됩니다.

##### list페이지
![list_page](https://user-images.githubusercontent.com/55528304/179341307-631d21c8-5e75-4917-9698-cacaa0fca1b8.png)
##### detail페이지
![detail_page](https://user-images.githubusercontent.com/55528304/179341312-2d93aefc-5931-4131-82d0-7e1e1bd0810b.png)
##### create페이지
![create_page](https://user-images.githubusercontent.com/55528304/179341321-60cf2e2c-15ae-4109-863f-798b4de36167.png)
##### update
![update_page](https://user-images.githubusercontent.com/55528304/179341323-16be126b-5fab-444f-8948-f718894d79bb.png)
