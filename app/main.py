import os
from flask import Flask, request
import random
import requests

app = Flask(__name__)

BASE_URL = os.getenv('BASE_URL', 'http://localhost')


@app.route('/gas/mattermost', methods=['POST'])
def prompt_gas():
    prompt = request.form.get('text')

    return {
        "response_type": "in_channel",
        "username": "Allure AI Gasmaster",
        "icon_url": "https://allure.id/assets/img/favicon.png",
        "attachments": [
            {
                "text": f"Proceed with this? \n\n#### {prompt}",
                "actions": [
                    {
                        "id": "confirm",
                        "name": "🚀 GAS",
                        "style": "primary",
                        "integration": {
                            "url": f"{BASE_URL}/gas/mattermost/gas",
                            "context": {
                                "gas": True,
                                "action_prompt": prompt
                            }
                        }
                    },
                    {
                        "id": "abort",
                        "name": "🙅 ABORT",
                        "style": "danger",
                        "integration": {
                            "url": f"{BASE_URL}/gas/mattermost/gas",
                            "context": {
                                "gas": False,
                                "action_prompt": prompt
                            }
                        }
                    }
                ]
            }
        ]
    }


@app.route('/gas/mattermost/gas', methods=['POST'])
def confirm_gas():
    print(request.data)
    user_name = request.json['user_name']
    prompt = request.json['context']['action_prompt']
    gas = request.json['context']['gas']

    if gas:
        return {
            "update": {
                "message": f"Action **{prompt}** confirmed by @{user_name}! 🚀🚀🚀",
                "props": {}
            }
        }
    else:
        return {
            "update": {
                "message": f"Action **{prompt}** aborted by @{user_name} :(",
                "props": {}
            }
        }
    
