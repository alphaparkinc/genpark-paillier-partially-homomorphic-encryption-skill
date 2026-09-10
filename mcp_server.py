from client import PaillierHomomorphic
import json

def handle_request(req):
    pail = PaillierHomomorphic()
    action = req.get("action")
    if action == "encrypt":
        m = req.get("m", 0)
        return {"status": "ok", "ciphertext": pail.encrypt(m)}
    elif action == "decrypt":
        c = req.get("ciphertext", 0)
        return {"status": "ok", "plaintext": pail.decrypt(c)}
    elif action == "add":
        c1 = req.get("c1", 0)
        c2 = req.get("c2", 0)
        return {"status": "ok", "ciphertext": pail.add_encrypted(c1, c2)}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "encrypt", "m": 42})))
