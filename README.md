# Raspberry-Pi-OpenAI-Image-Recognition
Python script for Raspberry Pi that uses OpenAI's models to analyze images

This repository contains a Python script for Raspberry Pi that leverages OpenAI's API to analyze images captured via a connected camera. The script uses MQTT for message handling, allowing integration with IoT systems for publishing and subscribing to topics.

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

1. Clone this repository to your Raspberry Pi:
  git clone https://github.com/yourusername/rpi-openai-image-recognition.git
  cd rpi-openai-image-recognition
2. Install the required Python libraries:
  pip install paho-mqtt openai
3. Install fswebcam:
  sudo apt-get install fswebcam
4. Create a config.py file to store your OpenAI API key:
  #config.py
  API_KEY = "YOUR_OPENAI_API_KEY"
5. Update the script with your configuration:
  MQTT broker details (broker_address, broker_port, username, password).
  MQTT topics (subscribe_topic, publish_topic).
  Image capture location and resolution (capture_location, resolution).
  Desired OpenAI model and prompt.

# Usage

1. Connect your camera to the Raspberry Pi.
2. Run the script:
  python rpi_image_ai.py
3. The script will:
  Listen for MQTT messages on the configured subscribe_topic.
  Capture an image when a message is received.
  Send the image to OpenAI for analysis.
  Publish the analysis results to the configured publish_topic.

# Configuration Options

Image Resolution: Adjust the resolution of the captured images by modifying the resolution variable.
OpenAI Model: Choose from supported models (gpt-4o, chatgpt-4o-latest, gpt-4o-mini, o1) based on your API access and requirements.
MQTT Topics: Customize subscribe_topic and publish_topic for integration with your IoT system.

# Example Workflow

1. A device or service publishes a message to the subscribe_topic
2. The script captures an image using the camera
3. The image is analyzed by OpenAI based on the provided prompt
4. The result is published to the publish_topic

# Troubleshooting

Ensure that your MQTT broker is accessible from the Raspberry Pi.
Verify your OpenAI API key in config.py.
Test the camera functionality by running a standalone fswebcam command.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize and extend the script to suit your use case!
