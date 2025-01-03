import paho.mqtt.client as mqtt 
import subprocess
import os
import base64
import config # Location of file containing API Key
from openai import OpenAI

# MQTT Broker IP
broker_address = "YOUR BROKER IP HERE"
# MQTT Broker Port
broker_port = 1883 #Default is 1883
# MQTT Broker Username
username = "YOUR USERNAME HERE"
# MQTT Broker Password
password = "YOUR PASSWORD HERE"
# MQTT Subscribe Topic
subscribe_topic = "YOUR LISTEN TOPIC HERE"
# MQTT Publish Topic
publish_topic = "YOUR PUBLISH TOPIC HERE"

# Captured Image Location (Example: /home/pi/images/testimage.jpg)
capture_location = "YOUR CAPTURED IMAGE LOCATION"
# Set resolution of image
resolution = "1920x1080"
# Command to take picture via FSWEBCAM
camera_command = f"fswebcam -r {resolution} --no-banner {capture_location}"

# Current image-compatible models. Be aware of varying API call limits for each model.
model = "gpt-4o"
#model = "chatgpt-4o-latest" #Model currently used in ChatGPT
#model = "gpt-4o-mini"
#model = "o1"

# Enter your prompt for API call
prompt = "YOUR PROMPT HERE"

# OpenAI Configuration
client = OpenAI(api_key=config.API_KEY) # Change depending on where API Key is stored

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def ask_openai(image_path):
    print("Waiting on OpenAI...")
    base64_image = encode_image(image_path)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg:base64,{base64_image}"},
                        },
                    ],
                }
            ],
        )
        print({response.choices[0].message.content})
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return "Error in OpenAI interaction"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe(subscribe_topic)

def on_message(client, userdata, msg):
    print("Message Received!")
    print(f"Topic: {msg.topic} Payload:{msg.payload}")
    try:
        os.system(camera_command)
        result = ask_openai(capture_location)
        client.publish(publish_topic, result)
    except Exception as e:
        print(f"Error in on_message: {e}")
        client.publish(publish_topic, "Error in processing")

def main():
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker_address, broker_port, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
