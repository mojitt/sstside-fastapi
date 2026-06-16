from openai import OpenAI
import os



def request_travel_plan(prompt: str) -> str:
    """
    GPT-4o에 여행 일정 생성 요청 후 응답 문자열 반환
    """
    
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.responses.create(
        model="gpt-4o",
        input=prompt,
        max_output_tokens=3000,
        temperature=0.5,
        text={
            "format": {
                "type": "json_object"
            }
        }
    )
    return response.output_text


def request_qna_answer(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-4o",
        input=prompt,
        max_output_tokens=300,
        temperature=0.3
    )

    return response.output_text

def classify_qna_question(question: str) -> str:
    """
    SST 고객지원 관련 질문인지 분류
    YES 또는 NO 반환
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-4o",
        input=f"""
다음 질문이 SST 여행 플랫폼의 고객지원 관련 질문인지 판단해라.

고객지원 관련:
- 공지사항
- FAQ
- 로그인
- 회원가입
- 게시글
- 댓글
- 신고
- 좋아요
- 마이페이지
- 여행 일정 생성
- AI 일정 생성
- 사이트 이용 방법

관련 없는 질문:
- 맛집 추천
- 여행지 추천
- 날씨
- 뉴스
- 일반 상식
- 프로그래밍 질문
- 공부 질문

질문:
{question}

반드시 YES 또는 NO만 출력해라.
""",
        max_output_tokens=16,
        temperature=0
    )

    return response.output_text.strip().upper()