# BOJ 18427 �Բ� ��� �ױ�
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, h = map(int,input().split())
    
    # dp[�л� ��ȣ][��] = ����� ��
    dp = [[0] * (h+1) for _ in range(n+1)]
    dp[0][0] = 1
    blocks = [[0, *map(int, input().split())] for _ in range(n)]

    for i in range(n):
        for j in range(h+1):
            if dp[i][j]:
                for k in blocks[i]:
                    if j+k <= h:
                        dp[i+1][j+k] += dp[i][j]
                        
    print(dp[-1][-1]%10007)