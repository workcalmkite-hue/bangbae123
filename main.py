# -*- coding: utf-8 -*-
"""
간단한 자기소개 출력 프로그램
아래 정보들을 자신에게 맞게 수정해서 사용하세요.
"""

# ====== 여기 정보만 바꾸면 됩니다 ======
name = "홍길동"
job = "중학교 기술 교사"
hobbies = ["코딩 가르치기", "새로운 기술 배우기", "등산"]
skills = ["Python", "HTML/CSS", "수업 자료 만들기"]
message = "학생들과 함께 즐겁게 배우는 것을 좋아합니다!"
# ====================================


def print_line(char="-", length=40):
    print(char * length)


def introduce():
    print_line("=")
    print(f"안녕하세요! 저는 {name}입니다.")
    print(f"직업: {job}")
    print_line()

    print("취미:")
    for hobby in hobbies:
        print(f"  - {hobby}")
    print_line()

    print("잘 다루는 기술:")
    for skill in skills:
        print(f"  - {skill}")
    print_line()

    print(message)
    print_line("=")


if __name__ == "__main__":
    introduce()
