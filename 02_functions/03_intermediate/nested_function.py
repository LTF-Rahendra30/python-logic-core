# A function defined inside aonother function


def process_order(price, discount):
    def apply_discount(price, discount):
        return price - (price * discount / 100)

    amount = apply_discount(price, discount)
    return amount


print(process_order(100, 10))
"""
The output: 90

This function keep helper function private and can't accesed in outher line

This function also helps encapsulate internal logic to be readable and clean

because, we should know when nested function be used, when a function is too small to be global function and 
when there is a special logic (if-else,for or other logic stetement) that is used in that function only 
"""
