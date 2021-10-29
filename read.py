data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) 

print('檔案讀取完了，總共有：', len(data), '筆資料')


#求每筆流言平均長度
sum_len = 0
for d in data:
	sum_len += len (d) #sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/ len(data))


#篩選資料長度
new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料長度小於100')
print(new[0])


#篩選資料內容
good =[]
for d in data:
	if 'good' in d:
		good.append(d) 
print('一共有', len(good), '筆留言提到good')
print(good[0])


#快寫法
good = [d for d in data if 'good' in d]


#文字計數功能
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #增加新key進wc字典

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

print(len(wc)) #印出字典裡總字數


#查詢功能
while True: 
	word = input('請問你想要查什麼字？')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有出現過！')

print('感謝使用本查詢功能')

