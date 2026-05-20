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