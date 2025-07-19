# Telegram LLM Chatbot

## Project Background

This project was created to enable access to Large Language Models (LLMs) during flights using airline-provided free WiFi messaging services. Many airlines (e.g., Air Canada, Delta) offer complimentary WiFi for text-based messaging apps like Telegram, WhatsApp, or iMessage, but restrict full internet access behind a paywall. These services typically allow only text messages (no images, videos, or heavy data), making it challenging to use web-based AI tools like ChatGPT directly.

The idea is to build a Telegram chatbot that acts as a proxy: users send text queries via Telegram on the plane's WiFi, and the bot processes them on a remote server using an LLM API, sending back text responses. This bypasses WiFi limitations since Telegram handles the messaging, and the heavy computation (LLM inference) happens server-side. This repo provides a simple, extensible template. It's optimized for text-only interactions to comply with airline WiFi rules and uses free LLM APIs to keep costs low.

## Features
- Text-based chatbot powered by Google Gemini (free tier).
- Environment variable management for secure API keys.
- Open-source and customizable for other LLMs or messaging platforms.

## Prerequisites
- Telegram account and BotFather to create a bot token.
- Google AI Studio account for a free Gemini API key[](https://aistudio.google.com/).
- Basic Python knowledge.

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/telegram-simple-llm-bot.git
cd telegram-simple-llm-bot
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file based on `.env.example` and fill in your keys:
```
TELEGRAM_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```
- Get `TELEGRAM_TOKEN`: Use Telegram's @BotFather to create a new bot.
- Get `GEMINI_API_KEY`: Sign up at Google AI Studio and generate an API key.

## Usage
1. Run the bot locally for testing:
```
python bot.py
```
2. In Telegram, search for your bot and start chatting (use /start to begin).
3. For production, deploy to your preferred hosting service (e.g., run in background with `nohup python bot.py &` and monitor logs).

## Integrating Other LLMs
If you want to switch from Google Gemini to another LLM (e.g., for better performance or different features), follow these steps:

1. **Choose an LLM API**: Select a free/low-cost provider like OpenAI (GPT-3.5-turbo, free credits available), Hugging Face Inference API (free for open models), or Anthropic Claude (API key required).
2. **Update requirements.txt**: Add the SDK, e.g., `openai==1.0.0` for OpenAI.
3. **Modify bot.py**:
- Import the new library (e.g., `import openai`).
- Add a new env variable in `.env` (e.g., `OPENAI_API_KEY=your_key`).
- Replace the Gemini setup and `handle_message` logic:
```python
  # Example for OpenAI
  openai.api_key = os.getenv('OPENAI_API_KEY')
  # In handle_message:
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": user_message}]
  )
  bot_reply = response['choices'][0]['message']['content']
```
- Adjust for the specific API's response format.
4. **Test Thoroughly**: Run locally, check rate limits, and ensure text-only responses.
5. **Costs and Limits**: Free tiers vary—e.g., OpenAI has usage quotas; monitor to avoid charges.

## Contributing
Feel free to fork and submit pull requests. Issues welcome for bugs or feature ideas.

## License
This project is licensed under the MIT License.
