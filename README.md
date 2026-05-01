# Interview Transcript Summarizer

A small CLI that takes an interview transcript (`.txt`) and prints a structured candidate summary *Topics covered*, *Profile* (role + seniority + justification), and a 3-6 sentence *Candidate summary* using the Groq API.

## How to run

1. Clone the repo and `cd` into it.
2. Python 3.8+ is required. Install the two dependencies:
   ```bash
   pip install groq python-dotenv
   ```
3. Copy `.env.example` to `.env` and put your Groq API key in it:
   ```bash
   cp .env.example .env
   # then edit .env so it contains: GROQ_API_KEY="gsk_..."
   ```
4. Run against a transcript file:
   ```bash
   python summarizer.py sample_transcript_assignment_1.txt
   ```
   The summary prints to stdout, terminal.

## LLM provider and model

- **Provider:** [Groq](https://groq.com/)
- **Model:** `openai/gpt-oss-120b` (via Groq)
- **Inference settings:** `temperature=0.2`, `max_tokens=1500`, `top_p=1` low temperature to keep the summary grounded in the transcript and reduce hallucinated detail.

The single-call prompt that is in the `summarizer.py` is the iteration-3 prompt.

## My learnings

**What surprised me.** How much of the quality gain came from format discipline rather than from the model getting smarter or the prompt getting longer. Iteration 1 (a plain natural-language ask) and iteration 3 (a strict template) hit the same model with very similar instructions, but iteration 3's outputs are easier to read, compare and get an idea because the section headers, seniority line, and paragraph length are specified. The other surprise was that the persona-only iteration 2 ("act as a recruiter") introduced a hallucination, increasing the candidate's tenure by few years, because the persona implicitly allows the model to provide unnecessary info. Adding "based strictly on the transcript evidence" in iteration 3 was a small change with a noticeable effect on grounding.

**What I'd improve with another day.** Three things. First, force a single canonical role string in the Profile section instead of letting the model hedge with "Senior Front-End / Full-Stack Engineer", this is a one-line prompt tweak. Second, add a self-check pass: feed the generated summary plus the transcript back to the model and ask it to flag any sentence that isn't supported by the transcript. Third, right now the script only handles one transcript at a time and prints to the terminal. I'd add a `--out` flag to save the summary to a file, support for running on many transcripts at once, and an option to output JSON so other tools can read the fields directly.

**Limitations of the final prompt.** It assumes there's enough in the transcript to judge seniority and if the transcript is very short or patchy, the model will still guess a level, which can be misleading. It also can't point out what's *missing* (e.g. "the candidate never showed system-design depth"), it only talks about what was actually said. And since it sends the whole transcript in one call, very long transcripts won't fit and would need to be split into smaller chunks and summarised piece by piece.
