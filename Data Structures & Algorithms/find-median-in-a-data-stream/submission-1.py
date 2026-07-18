class MedianFinder:

    def __init__(self):
        self.tiny = []
        self.big = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.tiny, -1 * num)
        if (self.tiny and self.big and (-1 * self.tiny[0]) > self.big[0]):
            val = -1 * heapq.heappop(self.tiny)
            heapq.heappush(self.big, val)        
        
        if len(self.tiny) > len(self.big) + 1:
            val = -1 * heapq.heappop(self.tiny)
            heapq.heappush(self.big, val)
        if len(self.big) > len(self.tiny) + 1:
            val =  heapq.heappop(self.big)
            heapq.heappush(self.tiny, -1 * val)


    def findMedian(self) -> float:
        # if the lenghts are uneven
        if len(self.tiny) > len(self.big):
            return (-1 * self.tiny[0])
        if len(self.big) > len(self.tiny):
            return self.big[0]
        return (-1 * self.tiny[0] + self.big[0])/2
            

        
        