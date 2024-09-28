from pyngrok import ngrok
import subprocess
import time

# Step 1: Start ngrok tunnel on port 8501 (default for Streamlit)
ngrok_tunnel = ngrok.connect(8501)
print("ngrok tunnel 'http' address:", ngrok_tunnel.public_url)

# Step 2: Run your Streamlit app
streamlit_process = subprocess.Popen(["streamlit", "run", "app.py"])

# Step 3: Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down Streamlit and ngrok...")
    streamlit_process.terminate()
    ngrok.kill()

    
