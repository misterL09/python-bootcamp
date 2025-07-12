"""
Create a function brew
that takes a parameter `drink` and `extra`
and prints the following format:

    I made you {drink} with {extra}

But make the extra optional

    I made you {drink}

"""
def brew(drink, extra=None):
    print()

# Use the function to brew coffee and tea
brew("coffee", "sugar")
brew("tea", "milk")
brew("coffee")