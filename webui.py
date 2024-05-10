import os
import subprocess
import uuid
import gradio as gr

checkpoints_dir = "checkpoints"
output = "output"
os.makedirs(output, exist_ok=True)
root_dir = os.path.dirname(os.path.realpath(__file__))

def inference(checkpoint_path, face, audio):
    # Call the inference.py module using subprocess
    output_name = f"{uuid.uuid4()}.mp4".replace("-", "")
    out_path = os.path.join(root_dir, output, output_name)
    command = f"python inference.py --checkpoint_path {checkpoint_path} --face {face} --audio {audio} --outfile {out_path}"
    print(command)
    subprocess.call(command, shell=True)
    # Assuming inference.py outputs the result file path
    print(out_path)
    return out_path

def get_checkpoints(checkpoints_dir):
    checkpoints = []
    for root, dirs, files in os.walk(checkpoints_dir):
        for file in files:
            if file.endswith(".pth") and 'gen_' in file:
                checkpoints.append(os.path.join(root, file))
    return checkpoints

with gr.Blocks() as app:

    checkpoints = get_checkpoints(checkpoints_dir)
    model_path = gr.Dropdown(label="Checkpoint Path", choices=checkpoints)
    face = gr.Video(label="Face")
    audio = gr.Audio(label="Audio", type="filepath")
    show = gr.Video(label="Face Show")
    btn = gr.Button()
    btn.click(
        fn=inference,
        inputs=[model_path, face, audio],
        outputs=[show]
    )

if __name__ == "__main__":
    app.launch(server_name='0.0.0.0', server_port=8010)
