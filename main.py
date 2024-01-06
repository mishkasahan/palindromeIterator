def palindromeIterator(words_list:list):
    for word in words_list:
        if word == word[::-1]:
            yield word


words_lis = ['level', 'racecar', 'python', 'madam']
palindrome_iter = palindromeIterator(words_lis)
for i in palindrome_iter:
    print(i)