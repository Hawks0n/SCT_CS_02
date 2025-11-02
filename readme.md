# Image Encryption Tool

A simple Python-based image encryption and decryption tool that uses pixel manipulation and XOR operations to secure images.  
Developed as part of a Cybersecurity Internship Task.


## 🔒 How It Works

This tool performs basic encryption by applying a **mathematical XOR operation** on each pixel using a user-provided key (1–255).  
It also reverses the pixel array for added obfuscation.

Mathematically:
Encrypted Pixel = Original Pixel XOR Key
Decrypted Pixel = Encrypted Pixel XOR Key

## Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Hawks0n/SCT_CS_02.git
cd image_encryption_tool
2️⃣ Create a virtual environment (optional but recommended)
bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3️⃣ Install dependencies
bash
Copy code
pip install pillow
🖼️ Usage
🔐 Encrypt an image
bash
python3 image_encryption_tool.py
Enter image path: images/wolf.jpg
Enter encryption key (1-255): 90
Encrypt or Decrypt? (e/d): e
Output → encrypted_wolf.png

🔓 Decrypt an image
bash
python3 image_encryption_tool.py
Enter image path: images/encrypted_wolf.png
Enter encryption key (1-255): 90
Encrypt or Decrypt? (e/d): d
Output → decrypted_wolf.png

📁 Project Structure
image_encryption_tool/
├── image_encryption_tool.py
├── images/
│   ├── wolf.jpg
│   ├── encrypted_wolf.png
│   └── decrypted_wolf.png
└── README.md
🧠 Notes
Works best with .jpg or .png images.

The same key must be used for both encryption and decryption.

The process is fully reversible if the same key is used.

👤 Author
Shashank.M.S AKA Hawks0n
Cybersecurity Intern @ SkillCraftTechnology
Built for educational and cybersecurity research purposes.
