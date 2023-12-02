with open('input_Probleme_A.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [list(map(int, line.split())) for line in lines]
n, m, k = lines[0]
m_k = m + k
S = lines[1]
S.sort(reverse=True)
sum_m_k = sum(S[i] for i in range(m_k))
sum_n = sum(S[i] for i in range(n))
print((sum_m_k/ sum_n)*100)