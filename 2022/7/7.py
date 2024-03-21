folders = {}


cur_folder = '/'
cur_keys = [cur_folder]
for i in open(0).read().splitlines():
    if '$' in i[0]:
        if 'cd' in i:
            f = i.split()[2]
            if '/' == f:
                cur_folder = f
                cur_keys = [f]
            elif '..' in f:
                cur_folder = '/'.join(cur_folder.split('/')[0:-2]) + '/'
                cur_keys.pop()
            else:
                cur_folder += f'{f}/'
                cur_keys.append(cur_folder)

            if cur_folder not in folders.keys():
                folders[cur_folder] = 0
            continue
        if 'ls' in i:
            continue
    try:
        # folders[cur_folder] += int(i.split()[0])
        for key in cur_keys:
            folders[key] += int(i.split()[0])
    except Exception:
        continue

t1 = 0
for key in folders.keys():
    if folders[key] <= 100000:
        t1 += folders[key]

tot_space = 70000000
needed_space = 30000000
free_space = tot_space - folders['/']

t2 = tot_space
for value in folders.values():
    if value >= needed_space - free_space:
        t2 = min(t2, value)

print(t1)
print(t2)
