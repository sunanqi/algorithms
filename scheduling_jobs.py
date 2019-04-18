'''
- Problem:
    Given a list of jobs with length and weight, schedule the jobs to minimize overall weighted sum of completion times.
    i.e., minimize sum(w_i * completion_time_i)
- Algorithm:
    Greedy algorithm
    Schedule the jobs in decreasing order of weight/length
- time complexity:
    O(n log n) due to sorting
- input:
    jobs = [[weight1,length1], [weight2,length2], ...]
- output:
    weighted sum of completion time
'''

def scheduling_jobs(jobs):
    # jobs = [[weight1,length1], [weight2,length2], ...]
    print(len(jobs))
    jobs = [i for i in jobs if i[1]>0]
    print(len(jobs))
    jobs.sort(key = lambda x: x[0]/x[1], reverse = True)
    cost, completion_time = 0, 0
    for w, l in jobs:
        completion_time += l
        cost += completion_time*w
    return cost


with open('jobs.txt') as f:
    lines = f.read().split('\n')
first_line = True
jobs = []
for line in lines:
    if first_line:
        first_line=False
    else:
        if line:
            jobs.append([int(i) for i in line.split()])
cost = scheduling_jobs(jobs)
print(cost)  #67311454237
