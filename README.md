# Vibeleftpad

AI-powered left padding using GPT. Because why use simple string methods when you can use artificial intelligence?

## Usage

Install the package:
```bash
pip install vibeleftpad
```

Set your OpenAI API key as an environment variable.
```bash
export OPENAI_API_KEY=your_key_here
```

```python
from vibeleftpad import leftpad

result = leftpad("hello", 10)
print(result)  # "     hello"

result = leftpad("world", 8, "0")
print(result)  # "000world"

result = leftpad("test", 10, "-")
print(result)  # "------test"
```

## Test

```bash
pytest tests/
```

## Dependencies

- openai
- pydantic
- typing-extensions

⚠️ Requires OpenAI API key. Experimental project - not for production use. This is a parody of the infamous leftpad incident.


## DISCLAIMER

Will not work half the time :) Enjoy!