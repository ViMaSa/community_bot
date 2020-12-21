import random
import time


# Distribute the given items into the given number of buckets
# Returns a list of lists (or "buckets") and boolean result.
# Each "bucket" contains some of the distributed items.
# Boolean value returns false if the operation was unsuccessfull
# Param 1 - numBuckets: Number of buckets
# Param 2 - items: list of items to distribute 
def distribute(numBuckets, items):

    if (numBuckets > len(items)):
        return None, False

    buckets = [] 
    for _ in range(numBuckets):
        buckets.append([])

    bucketIndex = 0
    for item in items:
        if (bucketIndex > numBuckets-1):
            bucketIndex = 0
        buckets[bucketIndex].append(item)
        bucketIndex += 1

    return buckets, True


# Perform an in-place shuffle of the given list
def shuffle(items):
    # Fisher-Yates Shuffle Algorithm
    random.seed(time.time())
    for i in reversed(range(len(items)-1)):
        j = random.randint(0,i)
        items[i], items[j] = items[j], items[i]


    
        




	