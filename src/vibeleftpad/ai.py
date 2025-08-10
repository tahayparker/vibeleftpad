import os
from typing_extensions import Literal
import openai
from pydantic import BaseModel
from typing import TypeVar


class VibeleftpadResponse(BaseModel):
    padded_string: str


class VibeleftpadRequest(BaseModel):
    string: str
    length: int
    pad_char: str = " "


def leftpad(string: str, length: int, pad_char: str = " ") -> str:
    response = structured_output(
        content=VibeleftpadRequest(string=string, length=length, pad_char=pad_char).model_dump_json(),
        response_format=VibeleftpadResponse,
    )
    return response.padded_string


T = TypeVar("T", bound=BaseModel)


def structured_output(
    content: str,
    response_format: T,
    model: str = "gpt-4o-mini",
) -> T:
    api_key = os.environ["OPENAI_API_KEY"]
    client = openai.OpenAI(api_key=api_key)

    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that pads strings on the left. Given a string, target length, and padding character, add the padding character to the left of the string until it reaches the target length. If the string is already longer than or equal to the target length, return it unchanged. Think hard before answering. Make sure that the answer is correct. Count the characters multiple times and ensure that the final output is accurate."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": content,
                    },
                ],
            }
        ],
        response_format=response_format,
    )
    response_model = response.choices[0].message.parsed
    return response_model
