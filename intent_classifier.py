import os
import openai

OPENAI_API_KEY="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"
openai.api_key = OPENAI_API_KEY

# while True:
#     # get user input
#     user_input = input(">> ")
#     # check if user wants to exit
#     if user_input == "exit":
#         exit(0)


    # response = openai.Completion.create(
    # engine="davinci",
    # # prompt="listen to WestBam album allergic on google music: PlayMusic\nshow me the picture creatures of light and darkness: SearchCreativeWork\nwhat is the weather like in the city of Frewen in the country of Venezuela: GetWeather\ntell me something about Japanese Culture: Search\nWhat is a Manga?: Search\nHow do I get past boredom?: Search\nWhy was Mussolini murdered?: Search\nWhat is Java?: Search",
    # prompt=user_input,
    # temperature=0,
    # max_tokens=10,
    # top_p=1,
    # best_of=3,
    # frequency_penalty=0,
    # presence_penalty=0,
    # #   stop=["\n"]
    # )


response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)

print(response)