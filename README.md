# 🎈 Streamlit + Change your text in a twitter-like way!

### Get OpenAI API key

You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

### Set your the OpenAI API key in your environment value "OPENAI_API_KEY"

```sh
OPENAI_API_KEY='xxxxxxxxxx'
```

## Run it locally

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```
