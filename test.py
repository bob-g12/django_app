print("Hello,world")
input_1 = input()
print(input_1)
while True:
    input_2 = input()
    if input_2 == "http://localhost:3000/":
        if "ネットワークエラー":
            print("GET / HTTP/1.1 503 xxx`")
        if "webページが見つからない":
            print("GET / HTTP/1.1 404 xxx`")
        print("GET / HTTP/1.1 200 xxx`")    
    if input_2 == "http://localhost:3000/favicon.ico":
        print("GET /favicon.ico HTTP/1.1 404 xxx`")