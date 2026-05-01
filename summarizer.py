import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# this is the version 3 (best) of all the 3 prompt messages.
SYSTEM_PROMPT = """You are an expert technical recruiter and hiring manager. Your task is to analyze the provided interview transcript and generate a structured summary.

You must output EXACTLY three sections formatted exactly as follows, with no extra introductory or concluding conversational text:

**Topics covered**
- [Bullet points of main themes, technical concepts, or behavioral topics discussed]

**Profile**
[Role/Title] - [Seniority Level]
Justification: [1-2 sentences explaining why based strictly on the transcript evidence]

**Candidate summary**
[A single short paragraph of 3-6 sentences detailing their background, core strengths, notable concerns or areas of friction, and an overall impression.]"""

filepath = sys.argv[1]
transcript = open(filepath, encoding="utf-8").read()

print(f"Processing '{filepath}'...\n")
print("-" * 50)

response = Groq().chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Here is the transcript:\n\n{transcript}"},
    ],
    temperature=0.2,
    max_tokens=1500,
    top_p=1,
)

print(response.choices[0].message.content)
print("-" * 50)
