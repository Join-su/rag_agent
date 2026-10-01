
from .page86 import page86_ai_msg


def sub():
    print("메인에서 실행하는 서브함수")


def main() -> None:
    print("app")
    sub()

    ai_msg = page86_ai_msg()
    print(f"~~~~~{ai_msg} 여기는 app.py의 main()")