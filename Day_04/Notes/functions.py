from functools import cache

#nag dagdag ng cache para mapabilis para ma store in memory(mabilis kapag meron na)
@cache

#fibunachi effect pabagal ng pabagal kapag pataas ng pataas
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
fib(38)
print("code Complete")