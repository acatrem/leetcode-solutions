# Problem : https://leetcode.com/problems/score-of-a-string/
# Difficulty : Easy
# Time Complexity : O(n)
# Space Complexity : O(1)

def scoreS(str):
    score = 0
    if(len(str) > 2 and len(str) <100 and str.islower()):
        for i in range(0, len(str)-1):
                score += abs(ord(str[i]) - ord(str[i+1])) 
                # ord() fonksiyonu Python'da kendisine verilen tek bir karakterin sayısal karşılığını (Unicode/ASCII kodunu) döndürür. 
        print(score)
            
    else:
        print("Geçersiz giriş. Lütfen 2 ile 1000 karakter arasinda ve sadece küçük harflerden oluşan bir string girin.")

s = input("s = ")

scoreS(s)



    