class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, category):
        self.items.append({'name': name, 'price': price, 'category': category})

    def remove_item(self, name):
        item_to_remove = None
        for item in self.items:
            if item['name'] == name:
                item_to_remove = item
                break

        if item_to_remove:
            total_before_removal = self.get_total_price()
            print(f"Total price before removing {name}: ${total_before_removal:.2f}")
            self.items.remove(item_to_remove)
            print(f"Removed {name} from cart.")
        else:
            print(f"Item {name} not found in cart.")

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

    def get_total_price(self):
        total = self.calculate_total()
        total = self.apply_discounts(total)
        return total

    def apply_discounts(self, total):
        raise NotImplementedError("Subclasses should implement this method.")

class RegularCustomer(ShoppingCart):
    def apply_discounts(self, total):
        electronics_price = 0

        for item in self.items:
            if item['category'] == 'electronics' and item['price'] >= 1000:
                electronics_price += item['price'] * 0.95
            else:
                electronics_price += item['price']

        if electronics_price > 1000:
            total_discounted_price = electronics_price * 0.98
            print(f"Total discounted price after applying 2% discount: ${total_discounted_price:.2f}")
            return total_discounted_price

        print(f"Total discounted price: ${electronics_price:.2f}")
        return electronics_price

class PremiumCustomer(ShoppingCart):
    def apply_discounts(self, total):
        discount = 0

        for item in self.items:
            if item['category'] == 'electronics' and item['price'] >= 1000:
                discount += item['price'] * 0.10
            elif item['category'] == 'electronics':
                discount += item['price'] * 0.05

        for item in self.items:
            if item['category'] == 'clothing':
                discount += item['price'] * 0.05

        if total > 500:
            discount += (total - discount) * 0.05

        return total - discount

def main():
    customer_type = input("Choose customer type (regular/premium): ").strip().lower()
    if customer_type == 'regular':
        cart = RegularCustomer()
    elif customer_type == 'premium':
        cart = PremiumCustomer()
    else:
        print("Invalid customer type")
        return

    while True:
        action = input("Add or remove item (add/remove/done): ").strip().lower()
        if action == 'done':
            total_price = cart.get_total_price()
            print(f"Final total price: ${total_price:.2f}")
            break
        if action == 'add':
            item_info = input("Add item to cart (format: name price category): ").strip().split()
            name = item_info[0]
            price = float(item_info[1])
            category = item_info[2].lower()
            cart.add_item(name, price, category)
        elif action == 'remove':
            name = input("Remove item from cart (format: name): ").strip()
            cart.remove_item(name)
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
