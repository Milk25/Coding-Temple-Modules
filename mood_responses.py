def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "That's great hearing this! Feep striving for better experience!",
        "sad": "That sad hearing this or getting this note.",
        "excited": "Awesome that were going out there.",
        "angry": "Too bad that your were angry with your brother.",
        "anxious": "Is that the case your anxious about thye circumstances.",
        "bored": "To bored to stay home!"
    }


    return responses.get(mood, "i'm not sure how to respond to that mood, but I hope you have a good day!")