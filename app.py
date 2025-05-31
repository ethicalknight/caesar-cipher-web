from flask import Flask, render_template, request
import random
import os
from utils.cipher import caesar_cipher

app = Flask(__name__)
os.makedirs("output", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    original = ""
    mode = ""
    
    if request.method == "POST":
        original = request.form["message"]
        if original.startswith("ENC:"):
            try:
                parts = original[4:].split("::", 1)
                shift = int(parts[0])
                message = parts[1]
                result = caesar_cipher(message, shift, mode='decrypt')
                mode = "Decryption"
            except:
                result = "Invalid encrypted format!"
        else:
            shift = random.randint(1, 25)
            encrypted = caesar_cipher(original, shift)
            result = f"ENC:{shift}::{encrypted}"
            mode = "Encryption"

        with open("output/result.txt", "w") as f:
            f.write(result)

    return render_template("index.html", result=result, original=original, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)
