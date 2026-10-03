import os, smtplib, anthropic
s.send_message(msg)
import os, smtplib, anthropic
from email.mime.text import MIMEText

client = anthropic.Anthropic()

prompt = """Tum TrendTadka (Hindi YouTube channel: cars,
gaming, AI tools, viral content) ke content agent ho.

1. Web search se dekho aaj Instagram Reels aur YouTube
   Shorts pe kaunse topics viral ho rahe hain
   (cars, gaming, AI tools). Sirf ideas dekho.
2. Top 3 viral ideas likho, har ek ke saath wajah.
3. Sabse best idea chuno aur uspe 100% ORIGINAL
   60 second Hinglish script likho (hook, body, outro).
   Kisi ki script ya video copy mat karna.
4. 3 title options, description aur 10 tags do.
5. Veo 3 ke liye 4 scene-by-scene English prompts do."""

resp = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=3500,
    tools=[{"type": "web_search_20250305",
            "name": "web_search", "max_uses": 6}],
    messages=[{"role": "user", "content": prompt}],
)
text = "".join(b.text for b in resp.content if b.type == "text")

me = os.environ["GMAIL"]
msg = MIMEText(text)
msg["Subject"] = "TrendTadka: Aaj ka viral idea + video package"
msg["From"] = me
msg["To"] = me
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login(me, os.environ["GMAIL_APP_PASSWORD"])
    s.send_message(msg)
