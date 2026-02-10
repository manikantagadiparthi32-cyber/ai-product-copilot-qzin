import random

def analyze_feedback(feedback_text):
    sentiments = ["Positive", "Neutral", "Negative"]
    categories = ["UX", "Performance", "Payments", "Support", "Feature Request"]

    sentiment = random.choice(sentiments)
    category = random.choice(categories)

    return f"Sentiment: {sentiment}\nCategory: {category}"
