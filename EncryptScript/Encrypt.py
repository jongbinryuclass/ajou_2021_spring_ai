import json
from base64 import b64encode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

def read_txt(fileName):
    with open(fileName, 'rt') as f:
        list_data = [a.strip('\n') for a in f.readlines()]
    return list_data

def write_json(fileName, data):
    with open(fileName, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_key(key_path):
    with open(key_path, "rb") as f:
        key = f.read()
    return key

def encrypt_data(key_path, ans_list, encrypt_store_path='ans.json'):
    key = load_key(key_path)
    data = " ".join([str(i) for i in ans_list])
    encode_data = data.encode()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(encode_data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    write_json(encrypt_store_path, {'iv':iv, 'ciphertext':ct})

if __name__=="__main__":
    # 1.이메일을 통해서 전달 받은 키 파일의 경로 입력
    key_path = "key.pem"
    raw_ans_path = ['ans1.txt', 'ans2.txt'] # 본인의 예측 결과 파일 이름
    encrypted_ans_path = ['ans1.json', 'ans2.json'] # 제출 파일 이름(이름 바꾸지 말것!)
    for raw_path, encrypted_path in zip(raw_ans_path, encrypted_ans_path):
        # 2. 예측한 결과를 텍스트 파일로 저장했을 경우 리스트로 다시 불러오기
        # 본인이 원하는 방식으로 리스트 형태로 예측 값을 불러오기만 하면 됨(순서를 지킬것)
        ans = read_txt(raw_path)
        # 3. 암호화!(pycrytodome 설치)
        encrypt_data(key_path, ans, encrypted_path)