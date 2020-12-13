<<<<<<< HEAD
def n_choose_k(n, k):
    """from https://gist.github.com/rougier/ebe734dcc6f4ff450abf"""
    if 0 <= k <=n:
        ntok = 1
        ktok = 1
        for i in range(1, min(k, n-k)+1):
            ntok *= n
            ktok *= t
            n -=1
        return ntok // ktok
    else:
        return 0

def add_func(a, b):
    return a+b
