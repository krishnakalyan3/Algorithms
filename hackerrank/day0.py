# Enter your code here. Read input from STDIN. Print output to STDOUT
ip_count = int(raw_input())
data_seq = raw_input()
data_array = map(lambda x: int(x), data_seq.strip().split())

# Mean
print sum(data_array)*1. / ip_count

# Median
sorted_data = sorted(data_array)
index_seq = []

if (ip_count % 2 ==0):
    index_seq.append(ip_count/2-1)
    index_seq.append(ip_count/2)
else:
    index_seq.append(ip_count/2)
        
medain_data = []        
for i in index_seq: 
    medain_data.append(sorted_data[i])

    
if len(medain_data) > 1:
    print sum(medain_data) * 1./2
else:
    print medain_data
    
# Mode
dict_count = {}

for i in data_array:
    if (i not in dict_count):
        dict_count[i] = 1
    else:
        dict_count[i] += 1

key, v = max(dict_count.iteritems(), key=lambda x:x[1])

for key in sorted(dict_count):
    if dict_count[key] == v:
        print key
        break
    else:
        pass

            



    
      

