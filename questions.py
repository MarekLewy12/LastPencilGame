# import polib
#
# # lines = 2700
# # fuzzy_lines = 1350
# #
# # po = polib.pofile('en_US.po')
# #
# # entry = po.find('do jutra')
# #
# # if entry:
# #     if 'fuzzy' not in entry.flags:
# #         entry.comment = 'comment'
# #         print(entry)
# #         entry.flags.append('fuzzy')
# #         po.save()
# #     else:
# #         print(str(int(fuzzy_lines / lines * 100)) + '%')
#
# x = 'NIE.'
#
# if x.startswith('Nie') or x.startswith('NIE'):
#     print("Nie found")


# A = int(input('A: '))
# A_adder = A
# B = int(input('B: '))
# B_adder = B
#
# NWD = []
# A_mul = []
# B_mul = []
#
# if A > B:
#     for x in range(1, B + 1):
#         if A % x == 0 and B % x == 0:
#             NWD.clear()
#             NWD.append(x)
#
# elif B > A:
#     for x in range(1, A + 1):
#         if A % x == 0 and B % x == 0:
#             NWD.clear()
#             NWD.append(x)
#
# else:
#     NWD.append(A)
#
# for _ in range(10):
#     A_mul.append(A)
#     A += A_adder
#     B_mul.append(B)
#     B += B_adder
#
# A_mul = set(A_mul)
# B_mul = set(B_mul)
# NWW = min(list(A_mul.intersection(B_mul)))
#
# print("NWD:", *NWD)
# print("NWW:", NWW)


x = 3
wie = []

for i in range(1, 6):
    wie.append(x * i)
print(wie)