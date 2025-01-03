# Raspberry-Pi-OpenAI-Image-Recognition

This repository contains a Python script for Raspberry Pi that uses OpenAI's API to analyze images captured via a connected camera. The script uses MQTT for message handling, allowing integration with IoT systems for publishing and subscribing to topics.

# Features

Captures images using a camera connected to the Raspberry Pi.
Sends the captured images to OpenAI's API for analysis.
Publishes the results of the image analysis to an MQTT topic.
Fully configurable for custom MQTT settings, image resolution, and OpenAI prompts.

# Prerequisites

Raspberry Pi with a camera module or a compatible USB camera.
Python 3.x installed on the Raspberry Pi.
Paho MQTT library for MQTT communication.
OpenAI Python client library for API interaction.
An OpenAI API key.
MQTT broker credentials (IP, port, username, password).
fswebcam installed for capturing images.

# Installation

1. Clone this repository in the directory of your choice:

```
$ cd /your/directory/here/rpi-openai-image-recognition
$ git clone https://github.com/VancePeterson/Raspberry-Pi-OpenAI-Image-Recognition.git
```
  
3. Install the required Python libraries:
```
$ pip install paho-mqtt
$ pip install openai
```

5. Install fswebcam:
```
$ sudo apt-get install fswebcam
```

6. Create a config.py file to store your OpenAI API key:
```
#config.py
API_KEY = "YOUR_OPENAI_API_KEY"
```

7. Update the script with your configuration:
MQTT broker details (broker_address, broker_port, username, password), MQTT topics (subscribe_topic, publish_topic), image capture location and resolution (capture_location, resolution), and desired OpenAI model and prompt.

# Usage

1. Connect your camera to the Raspberry Pi.
2. Run the script:
  python rpi_image_ai.py
3. The script will:<br />
- Listen for MQTT messages on the configured subscribe_topic<br />
- Capture an image when a message is received<br />
- Send the image to OpenAI for analysis<br />
- Publish the analysis results to the configured publish_topic.<br />

# Configuration Options

- Image Resolution: Adjust the resolution of the captured images by modifying the resolution variable.<br />
- OpenAI Model: Choose from supported models (gpt-4o, chatgpt-4o-latest, gpt-4o-mini, o1) based on your API access and requirements.<br />
- MQTT Topics: Customize subscribe_topic and publish_topic for integration with your IoT system.

# Example Workflow

1. The MQTT client receives a message on the subscribed topic, triggering the on_message function.
2. The script runs the fswebcam command to capture an image and save it to the specified location.
3. The captured image is read from disk and encoded into a Base64 string for transmission.
4. The Base64-encoded image and prompt are sent to OpenAI’s API for analysis using the selected model.
5. The script waits for a response from OpenAI and extracts the analyzed content from the API’s result.
6. The result from OpenAI is published to the specified MQTT topic, or an error message is sent if an issue occurs.

# Troubleshooting

Ensure that your MQTT broker has a static IP address and is accessible from the RPi.
Verify your OpenAI API key in config.py.
Test the camera functionality by running a standalone fswebcam command.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize and extend the script to suit your use case!
