# 10-turn forensic benchmark – drop these cold after any long chat
questions = [
    "What was the exact emoji I used in message #3?",
    "In the very first user message, what phrase did I use right before mentioning my favorite color?",
    "What name did I give my dog, and on which turn did I first mention him?",
    "When I talked about walking the dog, what exact wording did I use for 'after this'?",
    "Which turn did I say 'that’s the thing' for the first time?",
    "What was the last question I asked before we switched to talking about Perth?",
    "Did I ever mention a specific month or year for when I discovered chain-of-density? If yes, what?",
    "Quote the exact sentence where I admitted I’ve been 'hoarding' the memory fix.",
    "What reason did I give for deleting the Snippets AI posts so fast?",
    "In the part where I talked about my uncle, what two jobs did I say he has?"
]

print("Copy-paste these 10 questions into any model after a long chat.")
print("If it nails all 10 with exact wording/turn numbers → real memory.")
print("If it hallucinates or says 'I don’t remember' → context collapsed.\n")

for i, q in enumerate(questions, 1):
    print(f"{i}. {q}")
