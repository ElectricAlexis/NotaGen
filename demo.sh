#!/bin/bash

# See #2 and #3: https://github.com/ElectricAlexis/NotaGen/blob/main/gradio/README.md
REPO_ID="ElectricAlexis/NotaGen"
FILENAME="weights_notagenx_p_size_16_p_length_1024_p_layers_20_h_size_1280.pth"
echo "Downloading model weights from Hugging Face..."
"$HOME"/.local/bin/huggingface-cli download --local-dir ./gradio "$REPO_ID" "$FILENAME"

# See #3
cd gradio
echo "Starting Gradio demo..."
python demo.py
