class SlidingWindowMax:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.queue = []  
        self.result = []

    def clean_queue(self, i):

        if self.queue and self.queue[0] < i - self.k + 1:
            self.queue.pop(0)

        while self.queue and self.nums[self.queue[-1]] < self.nums[i]:
            self.queue.pop()

    def process(self):
        for i in range(len(self.nums)):
            self.clean_queue(i)
            self.queue.append(i)  

            if i >= self.k - 1:
                self.result.append(self.nums[self.queue[0]])

        return self.result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sliding_window = SlidingWindowMax(nums, k)
result = sliding_window.process()
print(result)  