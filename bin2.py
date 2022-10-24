# import json
# with open('sample2.txt','rb') as f:
#     a = f.read()

# # b = str(a)

# # with open('new.txt','wb') as f:
# #     f.write(a)
# import base64
# import json
# with open('jobs-3.jpg','rb') as f:
#     a = f.read()
#     f.close()

# # print(a)

# b = json.dumps(str(base64.b64encode(a)))

# c = json.loads(b)
# d = (c.decode())
# print(type(d))

# if(d==a): print('Equal')
# else: 
#     print('Shit')
#     # print(a)
#     print('\n\n\n\n\n')
#     print(b)

# with open('new.jpg','wb') as f:
#     f.write(d)

# import pickle

# with open('jobs-3.jpg','rb') as f:
#     a = f.read()
#     f.close()

# b = pickle.dumps(a)

# c = pickle.loads(b)

# with open('new.jpg','wb') as f:
#     f.write(c)
#     f.close()

import pickle

a = 'Hello'
b = pickle.dumps(a)
print(type(b))

if type(b)!=str:
    print('Yeaass')