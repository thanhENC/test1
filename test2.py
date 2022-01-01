#1. Đếm xem trong một chuỗi ký tự có bao nhiêu loại ký tự riêng biệt

# words = 'AEHANGIHIHGKJSNJKWPWEJGW97F#_ GHU*'

# def unique_letter(sentence):
#     letters = []
#     for letter in sentence:
#         if letter not in letters:
#             letters.append(letter)
#     return len(letter)

# print(unique_letter(words))

# def unique_letter(sentence):
#     for letter in sentence:
#         if letter in letters:
#             letters.append(letter)
#     return len[letters]

# print(unique_letters[words])


#2. Đoạn chương trình cho người dùng nhập vào một số nguyên dương N là số phần tử của mảng số nguyên lst_num. Tiếp theo cho phép người dùng nhập N phần tử nguyên dương của mảng lst_num. In ra tổng của các phần tử trong mảng số nguyên lst_num

# N = int(input('N = '))
# lst_num = []
# p = 1
# for i in N:
#     num = int(input('Nhap vao phan tu thu {}: '.format(i)))
#     lst_num.append(num)
#     p *= num
# print('Tong cac phan tu cua mang la {}.'.format(p))


# N = input('N = ')
# lst_num = []
# p = 0
# for i in N:
#     num = input('Nhap vao phan tu thu {}: '.format(i))
#     lst_num.append(num)
#     p *= num
# print('Tong cac phan tu cua mang la {}.'.format(p))


#3. Năm 2020, thành phố có 3 triệu dân. Ta có tốc độ gia tăng dân số hằng năm của thành phố là 1,15%. Đoạn chương trình in ra dân số của thành phố qua các năm cho đến khi đạt mức dân số gấp rưỡi dân số của năm 2020

# nam = 2020
# dan_so = 3
# print('2020. 3 trieu')
# while dan_so < 3 * 1.5:
#     nam += 1
#     dan_so *= (1 + 1.15/100)
#     print('{0}. {1} trieu'.format(nam, dan_so))

# nam = 2020
# dan so = 3
# print('2020. 3 trieu')
# while dan so < dan so * 1.5:
#     nam += 1
#     dan so *= (1 + 1.15/100)
# print('{0}. {1} trieu'.format(nam, dan so))