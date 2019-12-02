def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    st = set()
    longest, i, j = 0,0,0
    while (i < n and j < n):
        ch = s[j]
        if ch not in st:
            st.add(ch)
            j += 1
            longest = max(longest,j-i)
        else:
            st.remove(s[i])
            i+=1
    return longest
if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))