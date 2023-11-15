import time
import threading
 
def trading(coin, cut_gain):

    while True:
        
        try:
            print(f"{coin} 시세 정보 읽어 옴")
        
            print("특정 가격 미만일 때 얼만큼 매수")
        
            print(f"{cut_gain}% 이상일 때 얼만큼 매도")
        except:
            print("예외 처리")
            time.sleep(10)
    
        time.sleep(10)

if __name__ == "__main__":
    print("파일로 부터 업비트 키 정보를 읽음")
 
    list_coin = ["BTC", "ETH", "XRP"]
    list_gain = [1, 2, 3]
    for int_i, coin in enumerate(list_coin):
        cut_gain = list_gain[int_i]
        t = threading.Thread(target = trading, args = (coin, cut_gain))
        t.start()
        
    while True:
        print("잔고 정보 얻어옴 (추매 등을 고려하기 위함)")
        
        time.sleep(10)
