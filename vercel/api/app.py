#,                         ︵
#                        /'_/) 
#                      /¯ ../ 
#                    /'..../ 
#                  /¯ ../ 
#                /... ./
#   ¸•´¯/´¯ /' ...'/´¯`•¸  
# /'.../... /.... /.... /¯\
#('  (...´.(,.. ..(...../',    \
# \'.............. .......\'.    )      
#   \'....................._.•´/
#     \ ....................  /
#       \ .................. |
#         \  ............... |
#           \............... |
#             \ .............|
#               \............|
#                 \ .........|
#                   \ .......|
#                     \ .....|
#                       \ ...|
#                         \ .|
#                           \\
#                             \('-') 
#   ,,                           |_|\
#                               | |
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED

#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED
#DONT CHANGE CREDIT 
#IF YOU CHANGE MY CREDIT, I'LL FUCK YOUR MOM

from flask import Flask, request, jsonify, send_file, session, redirect, url_for, render_template_string
import asyncio
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from google.protobuf.json_format import MessageToJson
import binascii
import aiohttp
import requests
import json
import like_pb2
import like_count_pb2
import uid_generator_pb2
from werkzeug.security import generate_password_hash, check_password_hash
import os

#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED
#DONT CHANGE CREDIT 
#IF YOU CHANGE MY CREDIT, I'LL FUCK YOUR MOM

app = Flask(__name__)

if not os.environ.get('SECRET_KEY'):
    import sys
    print("ERROR: SECRET_KEY environment variable is required!")
    print("Generate one with: python -c 'import os; print(os.urandom(24).hex())'")
    print("Set it in Replit Secrets or your deployment platform")
    sys.exit(1)

if not os.environ.get('ADMIN_PASSWORD'):
    import sys
    print("ERROR: ADMIN_PASSWORD environment variable is required!")
    print("Set it in Replit Secrets or your deployment platform")
    sys.exit(1)

app.secret_key = os.environ.get('SECRET_KEY')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
ADMIN_PASSWORD_HASH = generate_password_hash(ADMIN_PASSWORD)

def load_tokens(server_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if server_name == "IND":
        with open(os.path.join(base_dir, "token_ind.json"), "r") as f:
            return json.load(f)
    elif server_name in {"BR", "US", "SAC", "NA"}:
        with open(os.path.join(base_dir, "token_br.json"), "r") as f:
            return json.load(f)
    else:
        with open(os.path.join(base_dir, "token_bd.json"), "r") as f:
            return json.load(f)

def encrypt_message(plaintext):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(plaintext, AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return binascii.hexlify(encrypted_message).decode('utf-8')

def create_protobuf_message(user_id, region):
    message = like_pb2.like()
    message.uid = int(user_id)
    message.region = region
    return message.SerializeToString()

async def send_request(encrypted_uid, token, url):
    edata = bytes.fromhex(encrypted_uid)
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/x-www-form-urlencoded",
        'Expect': "100-continue",
        'X-Unity-Version': "2018.4.11f1",
        'X-GA': "v1 1",
        'ReleaseVersion': "OB50"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=edata, headers=headers) as response:
                return response.status
    except Exception as e:
        print(f"Request failed: {e}")
        return 500

async def send_multiple_requests(uid, server_name, url, num_requests):
    region = server_name
    protobuf_message = create_protobuf_message(uid, region)
    encrypted_uid = encrypt_message(protobuf_message)
    tasks = []
    tokens = load_tokens(server_name)
    
    for i in range(num_requests):
        token = tokens[i % len(tokens)]["token"]
        tasks.append(send_request(encrypted_uid, token, url))
    
    results = await asyncio.gather(*tasks)
    return results

def create_protobuf(uid):
    message = uid_generator_pb2.uid_generator()
    message.krishna_ = int(uid)
    message.teamXdarks = 1
    return message.SerializeToString()

def enc(uid):
    protobuf_data = create_protobuf(uid)
    encrypted_uid = encrypt_message(protobuf_data)
    return encrypted_uid

def make_request(encrypt, server_name, token):
    if server_name == "IND":
        url = "https://client.ind.freefiremobile.com/GetPlayerPersonalShow"
    elif server_name in {"BR", "US", "SAC", "NA"}:
        url = "https://client.us.freefiremobile.com/GetPlayerPersonalShow"
    else:
        url = "https://clientbp.ggblueshark.com/GetPlayerPersonalShow"

    edata = bytes.fromhex(encrypt)
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/x-www-form-urlencoded",
        'Expect': "100-continue",
        'X-Unity-Version': "2018.4.11f1",
        'X-GA': "v1 1",
        'ReleaseVersion': "OB50"
    }

    response = requests.post(url, data=edata, headers=headers)
    hex_data = response.content.hex()
    binary = bytes.fromhex(hex_data)
    return decode_protobuf(binary)

def decode_protobuf(binary):
    try:
        items = like_count_pb2.Info()
        items.ParseFromString(binary)
        return items
    except Exception as e:
        print(f"Error decoding Protobuf data: {e}")
        return None

@app.route('/')
def admin_panel():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_file('admin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if check_password_hash(ADMIN_PASSWORD_HASH, password):
            session['logged_in'] = True
            return redirect(url_for('admin_panel'))
        else:
            return render_template_string(LOGIN_HTML, error='Invalid password')
    return render_template_string(LOGIN_HTML)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

LOGIN_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MaxLikes API - Login</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .login-container {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            max-width: 400px;
            width: 100%;
        }
        
        .login-header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .login-header h1 {
            color: #667eea;
            font-size: 2em;
            margin-bottom: 10px;
        }
        
        .login-header p {
            color: #666;
            font-size: 1em;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }
        
        .form-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s;
        }
        
        .form-group input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            cursor: pointer;
            transition: transform 0.2s;
            font-weight: 600;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .error {
            background: #fee;
            border: 1px solid #fcc;
            color: #c00;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .lock-icon {
            font-size: 3em;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <div class="lock-icon">🔐</div>
            <h1>MaxLikes API</h1>
            <p>Admin Panel Login</p>
        </div>
        
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        
        <form method="POST">
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter admin password" autocomplete="current-password" required autofocus>
            </div>
            
            <button type="submit" class="btn">🚀 Login</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/like', methods=['GET'])
def handle_requests():
    uid = request.args.get("uid")
    server_name = request.args.get("server_name", "").upper()
    key = request.args.get("key")
    like_param = request.args.get("like")

    if key != "gst":
        return jsonify({"error": "Invalid or missing API key 🔑"}), 403

    if not uid or not server_name:
        return jsonify({"error": "UID and server_name are required"}), 400

    def process_request():
        tokens_data = load_tokens(server_name)
        token = tokens_data[0]['token']
        encrypt = enc(uid)
        
        total_tokens = len(tokens_data)
        
        if like_param:
            if like_param.lower() == "max":
                num_requests = total_tokens
            else:
                try:
                    num_requests = int(like_param)
                    if num_requests > total_tokens:
                        num_requests = total_tokens
                    elif num_requests < 1:
                        num_requests = 1
                except ValueError:
                    num_requests = total_tokens
        else:
            num_requests = total_tokens

        before = make_request(encrypt, server_name, token)
        if before is None:
            return {
                "error": "Failed to connect to game server. Tokens may be invalid or expired.",
                "status": 503
            }
        jsone = MessageToJson(before)
        data = json.loads(jsone)
        before_like = int(data['AccountInfo'].get('Likes', 0))

        if server_name == "IND":
            url = "https://client.ind.freefiremobile.com/LikeProfile"
        elif server_name in {"BR", "US", "SAC", "NA"}:
            url = "https://client.us.freefiremobile.com/LikeProfile"
        else:
            url = "https://clientbp.ggblueshark.com/LikeProfile"

        results = asyncio.run(send_multiple_requests(uid, server_name, url, num_requests))
        
        successful_requests = sum(1 for status in results if status == 200)
        failed_requests = len(results) - successful_requests
        success_rate = (successful_requests / len(results) * 100) if results else 0

        after = make_request(encrypt, server_name, token)
        if after is None:
            return {
                "error": "Failed to retrieve updated data from game server.",
                "status": 503
            }
        jsone = MessageToJson(after)
        data = json.loads(jsone)

        after_like = int(data['AccountInfo']['Likes'])
        id = int(data['AccountInfo']['UID'])
        name = str(data['AccountInfo']['PlayerNickname'])

        like_given = after_like - before_like
        status = 1 if like_given != 0 else 2

        result = {
            "LikesGivenByAPI": like_given,
            "LikesAfterCommand": after_like,
            "LikesBeforeCommand": before_like,
            "PlayerNickname": name,
            "UID": id,
            "status": status,
            "TotalTokensAvailable": total_tokens,
            "TokensUsed": num_requests,
            "SuccessfulRequests": successful_requests,
            "FailedRequests": failed_requests,
            "SuccessRate": f"{success_rate:.1f}%"
        }
        return result

    result = process_request()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    
    
    
    
    
#,                         ︵
#                        /'_/) 
#                      /¯ ../ 
#                    /'..../ 
#                  /¯ ../ 
#                /... ./
#   ¸•´¯/´¯ /' ...'/´¯`•¸  
# /'.../... /.... /.... /¯\
#('  (...´.(,.. ..(...../',    \
# \'.............. .......\'.    )      
#   \'....................._.•´/
#     \ ....................  /
#       \ .................. |
#         \  ............... |
#           \............... |
#             \ .............|
#               \............|
#                 \ .........|
#                   \ .......|
#                     \ .....|
#                       \ ...|
#                         \ .|
#                           \\
#                             \('-') 
#   ,,                           |_|\
#                               | |
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
#FUCKED BY JOBAYAR AHMED @JOBAYAR_AHMED 
