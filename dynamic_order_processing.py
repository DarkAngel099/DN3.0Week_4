

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass


class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        # No discount for regular customers
        return order_amount


class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        # 10% discount for premium customers
        return order_amount * 0.9


class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        # 20% discount for VIP customers
        return order_amount * 0.8


class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount

    def final_price(self):
        # Determine the discount strategy
        if self.customer_type == 'regular':
            strategy = RegularDiscount()
        elif self.customer_type == 'premium':
            strategy = PremiumDiscount()
        elif self.customer_type == 'vip':
            strategy = VIPDiscount()
        else:
            raise ValueError("Unknown customer type")

        
        return strategy.apply_discount(self.order_amount)


regular_order = Order('regular', 100)
premium_order = Order('premium', 100)
vip_order = Order('vip', 100)


print(f"Regular customer final price: ${regular_order.final_price():.2f}")
print(f"Premium customer final price: ${premium_order.final_price():.2f}")
print(f"VIP customer final price: ${vip_order.final_price():.2f}")
