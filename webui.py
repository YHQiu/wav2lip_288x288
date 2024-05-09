import os
import subprocess
import uuid
import gradio as gr

output = "output"
os.makedirs(output, exist_ok=True)

def inference(checkpoint_path, face, audio):
    # Call the inference.py module using subprocess
    output_name = f"{uuid.uuid4()}.mp4"
    command = f"python inference.py --checkpoint_path {checkpoint_path} --face {face} --audio {audio} --outfile {os.path.join(output, output_name)}"
    subprocess.call(command, shell=True)
    # Assuming inference.py outputs the result file path
    return os.path.join(output, output_name)

with gr.Blocks() as app:
        model_path = gr.inputs.Textbox(label="Checkpoint Path")
        face = gr.Video(label="Face")
        audio = gr.Audio(label="Audio")
        show = gr.Video(label="Face Show")
        btn = gr.Button()
        btn.click(
            fn=inference,
            inputs=[model_path, face, audio],
            outputs=[show]
        )

if __name__ == "__main__":
    app.launch(server_name='0.0.0.0', server_prot=8108)