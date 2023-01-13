def solution(): 
    numbers = ''.join(input().split())
    if numbers == '12345678':
        answer = 'ascending'
    elif numbers == '87654321':
        answer = 'descending'
    else:
        answer = 'mixed'
    print(answer)

if __name__ == '__main__':
    solution()
