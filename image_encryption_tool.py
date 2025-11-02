#!/usr/bin/env python3
import os
from PIL import Image
import numpy as np
import hashlib

def md5_bytes(arr: np.ndarray) -> str:
    """Return MD5 hex digest of raw bytes of numpy array."""
    return hashlib.md5(arr.tobytes()).hexdigest()

def load_image(path: str):
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    img = Image.open(path)
    if img.mode not in ("RGB", "RGBA", "L"):
        img = img.convert("RGBA")
    return img

def encrypt_image(image_path: str, key: int, out_prefix: str = "encrypted"):
    img = load_image(image_path).convert("RGBA")
    arr = np.array(img, dtype=np.uint8)

    print("[+] Original MD5:", md5_bytes(arr))
    enc = (arr ^ np.uint8(key)).reshape(-1)
    enc = enc[::-1].copy().reshape(arr.shape)

    out_name = f"{out_prefix}_{os.path.basename(image_path).rsplit('.',1)[0]}.png"
    Image.fromarray(enc).save(out_name)
    print("[+] Saved encrypted image ->", out_name)
    print("[+] Encrypted MD5:", md5_bytes(enc))
    print("[+] Encryption complete.")
    return out_name

def decrypt_image(image_path: str, key: int, out_prefix: str = "decrypted"):
    img = load_image(image_path).convert("RGBA")
    arr = np.array(img, dtype=np.uint8)

    print("[+] Encrypted MD5:", md5_bytes(arr))
    dec = arr.reshape(-1)[::-1].copy()
    dec = (dec ^ np.uint8(key)).reshape(arr.shape)

    out_name = f"{out_prefix}_{os.path.basename(image_path).rsplit('.',1)[0]}.png"
    Image.fromarray(dec).save(out_name)
    print("[+] Saved decrypted image ->", out_name)
    print("[+] Decrypted MD5:", md5_bytes(dec))
    print("[+] Decryption complete.")
    return out_name

if __name__ == "__main__":
    img_path = input("Enter image path: ").strip()
    img_path = os.path.expanduser(img_path)

    try:
        key = int(input("Enter encryption key (1-255): ").strip())
        assert 1 <= key <= 255
    except Exception:
        print("Invalid key. Use integer 1–255.")
        raise SystemExit(1)

    mode = input("Encrypt or Decrypt? (e/d): ").lower().strip()
    if mode == "e":
        encrypt_image(img_path, key)
    elif mode == "d":
        decrypt_image(img_path, key)
    else:
        print("Invalid option. Use e or d.")
        raise SystemExit(1)


