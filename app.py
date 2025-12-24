from textblob import TextBlob

texts = [
    "I love this product! It's amazing.",
    "What a wonderful day!",
    "The service was excellent and the staff was very friendly.",
    "This movie was fantastic, I enjoyed every moment!",
    "The food tastes great and the presentation is beautiful.",
    "I’m really happy with my purchase!",
    "That performance was outstanding!",
    "This new phone is super fast and easy to use.",
    "I feel so proud of my progress.",
    "Everything went perfectly today!",
    "This is the worst experience ever.",
    "I hate waiting in line for so long.",
    "The product broke after one day of use.",
    "I’m disappointed with the quality of this item.",
    "The food was cold and tasteless.",
    "The customer service was terrible.",
    "What a waste of money!",
    "The movie was boring and too long.",
    "I regret buying this.",
    "Nothing went right today.",
    "It's okay, nothing special.",
    "The product works as expected.",
    "I received my order yesterday.",
    "The weather is average today.",
    "It was neither good nor bad.",
    "I don’t really care about this topic.",
    "The book had some interesting parts but was mostly dull.",
    "The phone looks nice but performs poorly.",
    "I’m not sure how I feel about this.",
    "It’s just another typical day."
]

for text in texts:
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print(f"Text: {text}")
    print(f"Polarity: {sentiment.polarity}")
    if sentiment.polarity > 0:
        print("Sentiment: Positive\n")
    elif sentiment.polarity < 0:
        print("Sentiment: Negative\n")
    else:
        print("Sentiment: Neutral\n")
