# Discord-Bot-with-Gpt3
*This is an interactive bot made with OpenAi's Gpt3 Technology, I have used the sarcastic Q&A bot for this one, Although the bot replies accurate to most of the question you ask but sometimes it is a bit random and is wierd :D*

Sometimes this bot can get very rude :p

This bot can hosted on Heroku or run locally in a Docker container.

## How can I use it on Heroku?
1. Provide your OpenAI key in the environment file
2. Provide your Discord Bot's secret key, in the main Bot.py file at the last line
3. That's it and you can host it on heroku just by using Heroku CLI and uploading all the files I have here

## Running it in Docker
Build a docker image

    docker build -t bossbot:latest .

Run the container providing your OpenAI key as an environment variable

    docker run -d \
      --name=bossbot \
      -e OPENAI_API_KEY=<your_openai_key> \
      --restart unless-stopped \
      bossbot
