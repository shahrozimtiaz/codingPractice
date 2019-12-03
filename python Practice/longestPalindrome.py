def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[0]*n for i in range(n)]
    lp = ''
    for i in range(n-1,-1,-1):
        for j in range(i,n,1):
            dp[i][j] = s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
            if(dp[i][j] and j-i+1 > len(lp)):
                lp = s[i:j+1]
    return lp
if __name__ == '__main__':
    print(longestPalindrome(
"babad"))