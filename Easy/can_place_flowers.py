def can_place_flowers(flowerbed, n):
    counter = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if empty_left and empty_right:
                flowerbed[i] = 1
                counter += 1
    
    return counter >= n

flowerbed = [1, 0, 0, 0, 1]
n = 1
print(can_place_flowers(flowerbed, n)) 







