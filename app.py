from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt="""You are a professional medical AI assistant. Analyze the provided image carefully and respond to the patient's spoken concerns. 
            Provide a detailed medical assessment including:
            1. What you observe in the image
            2. Possible medical conditions or diagnoses
            3. Detailed explanation of the condition
            4. Recommended treatments and remedies
            5. When to seek immediate medical attention
            6. Prevention tips if applicable
            
            Always respond as if speaking directly to the patient. Use clear, compassionate language.
            Start with 'Based on what I can see and your description...' 
            Provide comprehensive information while being reassuring and professional.
            Make your response detailed and informative (4-6 sentences minimum)."""

# Custom CSS for animated button and glitch heading
custom_css = """
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap");

/* Glitch Effect for Main Heading */
.glitch-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2rem 0;
    background: #0d0d0d;
    padding: 2rem;
    border-radius: 15px;
}

.glitch-text {
    font-size: 4rem;
    font-weight: bold;
    position: relative;
    color: #fff;
    animation: glitch 2s infinite;
    font-family: 'Arial', sans-serif;
}

.glitch-text::before,
.glitch-text::after {
    content: 'AI Doctor Assistant';
    position: absolute;
    top: 0;
    left: 0;
    color: #ff005e;
    background: transparent;
    clip-path: polygon(0 0, 100% 0, 100% 30%, 0 30%);
    animation: glitch 2s infinite;
}

.glitch-text::after {
    color: #00d4ff;
    clip-path: polygon(0 70%, 100% 70%, 100% 100%, 0 100%);
}

@keyframes glitch {
    0%, 100% {
        transform: translate(0);
    }
    20% {
        transform: translate(-2px, 2px);
    }
    40% {
        transform: translate(2px, -2px);
    }
    60% {
        transform: translate(-1px, 1px);
    }
    80% {
        transform: translate(1px, -1px);
    }
}

/* Subtitle styling */
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 2rem;
    font-weight: 500;
}

@media screen and (max-width: 600px) {
    .glitch-text {
        font-size: 2.5rem;
    }
    .subtitle {
        font-size: 1rem;
    }
}

/* Animated Button Styling */
.animated-button {
    position: relative !important;
    display: inline-block !important;
    padding: 25px 30px !important;
    margin: 20px 0 !important;
    color: #03e9f4 !important;
    background: transparent !important;
    border: none !important;
    text-decoration: none !important;
    text-transform: uppercase !important;
    transition: 0.5s !important;
    letter-spacing: 4px !important;
    overflow: hidden !important;
    font-family: "Raleway", sans-serif !important;
    font-weight: bold !important;
    font-size: 16px !important;
    cursor: pointer !important;
}

.animated-button:hover {
    background: #03e9f4 !important;
    color: #050801 !important;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 200px #03e9f4 !important;
}

.animated-button span {
    position: absolute;
    display: block;
}

.animated-button span:nth-child(1) {
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}

@keyframes animate1 {
    0% { left: -100%; }
    50%, 100% { left: 100%; }
}

.animated-button span:nth-child(2) {
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(180deg, transparent, #03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}

@keyframes animate2 {
    0% { top: -100%; }
    50%, 100% { top: 100%; }
}

.animated-button span:nth-child(3) {
    bottom: 0;
    right: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.5s;
}

@keyframes animate3 {
    0% { right: -100%; }
    50%, 100% { right: 100%; }
}

.animated-button span:nth-child(4) {
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(360deg, transparent, #03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}

@keyframes animate4 {
    0% { bottom: -100%; }
    50%, 100% { bottom: 100%; }
}

/* Center the button */
.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px 0;
}
"""

def process_inputs(audio_filepath, image_filepath):
    try:
        print(f"Processing inputs - Audio: {audio_filepath}, Image: {image_filepath}")
        
        if not audio_filepath:
            print("No audio provided")
            return "No audio provided", "Please record your voice describing your symptoms", None
        
        if not image_filepath:
            print("No image provided")
            return "No image provided", "Please upload a medical image for analysis", None
            
        print("Starting speech-to-text processing...")
        # Process speech to text
        speech_to_text_output = transcribe_with_groq(
            stt_model="whisper-large-v3",
            audio_filepath=audio_filepath,
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
        )
        print(f"Speech-to-text result: {speech_to_text_output}")

        print("Starting image analysis...")
        # Analyze image with query
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
        print(f"Doctor response: {doctor_response}")

        print("Generating voice response...")
        # Generate voice response
        voice_file = text_to_speech_with_elevenlabs(
            input_text=doctor_response, 
            output_filepath="final.mp3"
        )
        print(f"Voice file generated: {voice_file}")
        
        return speech_to_text_output, doctor_response, voice_file
    
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(f"Error occurred: {error_msg}")
        return error_msg, "Please check your inputs and try again", None

# Create simple interface with animated button
with gr.Blocks(title="AI Doctor Assistant") as demo:
    
    # Glitch Header
    gr.HTML("""
    <div class="glitch-container">
        <h1 class="glitch-text">AI Doctor Assistant</h1>
    </div>
    <div class="subtitle">
        Advanced Medical Image Analysis with Voice Interaction
    </div>
    """)
    
    # Input Section
    gr.Markdown("## Input Section")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🎤 Voice Input")
            audio_input = gr.Audio(
                sources=["microphone"], 
                type="filepath",
                label="Record your symptoms"
            )
            
            # Instructions moved here
            gr.Markdown("""
            ## How to Use:
            1. **Record Audio**: Click the microphone and describe your symptoms
            2. **Upload Image**: Select a clear medical image for analysis  
            3. **Submit**: Click the analyze button to get AI medical insights
            4. **Listen**: Play the audio response for detailed recommendations
            
            ⚠️ **Disclaimer**: This is for educational purposes only. Always consult healthcare professionals for medical advice.
            """)
            
        with gr.Column():
            gr.Markdown("### 📸 Medical Image")
            image_input = gr.Image(
                type="filepath",
                label="Upload medical image"
            )
    
    # Submit Button with Animation
    submit_btn = gr.Button(" Analyze with AI Doctor!", variant="Info", size="md", elem_classes="animated-button")
    
    # Output Section
    gr.Markdown("## Results")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📝 Speech to Text")
            text_output = gr.Textbox(
                label="Your spoken symptoms",
                lines=4,
                interactive=False
            )
            
            gr.Markdown("### 🔊 Audio Response")
            audio_output = gr.Audio(
                label="Listen to doctor's response",
                interactive=False
            )
            
        with gr.Column():
            gr.Markdown("### 🩺 Detailed Doctor's Analysis")
            doctor_output = gr.Textbox(
                label="Comprehensive medical assessment and recommendations",
                lines=12,
                interactive=False,
                placeholder="Detailed medical analysis will appear here with observations, possible conditions, treatments, and recommendations..."
            )
    
    # Connect functionality
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[text_output, doctor_output, audio_output]
    )
    
    # Footer
    gr.Markdown("""<div style="text-align: center; margin-top: 2rem; padding: 1rem; border-top: 1px solid #e0e0e0;">
    <strong>AI Doctor Assistant</strong> - Powered by Advanced AI Technology<br>
    © 2025 Built for accessible healthcare technology
    By Faizan Khan
    </div>""", elem_id="footer")

if __name__ == "__main__":
    demo.launch(debug=False, css=custom_css, share=False, server_name="0.0.0.0", server_port=7860)

# For Vercel deployment
app = demo