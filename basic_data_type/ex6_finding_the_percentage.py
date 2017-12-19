from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = list(scores)
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print('%.2f' % (sum(query_scores) / len(query_scores)))

# Second way to solve this problem
# marks = {}
# for _ in range(int(input())):
#     line = input().split()
#     marks[line[0]] = list(map(float, line[1:]))
# print('%.2f' % (sum(marks[input()]) / 3))
