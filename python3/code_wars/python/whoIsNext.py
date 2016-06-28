def whoIsNext(names, r):
    from collections import deque
	queue = deque(names)
	    
	count = 0
	for i in range(len(queue)):
				
		drinking = queue.popleft()
		queue.extend([drinking, drinking])
		count += 1
		print(count, drinking, i)

		if count == r:
			return drinking
