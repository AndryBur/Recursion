n=5
def fact_r(n):
    if n<=0:
        return 1
    return n*fact_r(n-1)
fact=fact_r(n)
print(f'Факториалом от {n} равен {fact}')