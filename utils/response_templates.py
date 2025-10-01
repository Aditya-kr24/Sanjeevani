import random

normal_responses = {
    "hi": ["Hey there! 👋", "Hi! How's your day going?", "Hello! Glad to see you here."],
    "hello": ["Hello! How are you doing today?", "Hey! How's everything going?"],
    "how are you": ["I'm doing great, thanks for asking! How about you? 😊", 
                    "I'm fine! Hope you're doing well too."],
    "im good" : ["Glad to hear that! 😊", "That's nice to hear!❤️"],
    "thanks": ["You're welcome 🌸", "Anytime! I'm here for you."],
    "default": ["That's interesting, tell me more!", 
                "Got it 👍 Tell me how you're feeling.", 
                "Hmm, I'd like to hear more about that."]
}

def get_smalltalk(text: str) -> str:
    text = text.lower()
    for key in normal_responses:
        if key in text:
            return random.choice(normal_responses[key])
    return random.choice(normal_responses["default"])
