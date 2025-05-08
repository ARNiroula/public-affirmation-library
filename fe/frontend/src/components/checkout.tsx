import { useCart } from '@/state_provider/cart_provider';
import Image from 'next/image';
import { useRouter } from 'next/navigation';

const CheckoutPage: React.FC = () => {
    const { cartItems, removeFromCart, clearCart } = useCart();
    const router = useRouter();

    const handleRemoveItem = (book_id: number) => {
        removeFromCart(book_id);
    };

    const handleClearCart = () => {
        clearCart();
    };

    const handleCheckout = () => {
        // Implement checkout logic, like sending cart data to backend or redirect to payment page
        router.push('/payment'); // Redirect to the payment page (example)
    };

    const calculateTotal = (): number => {
        return cartItems.reduce((total, item) => total + item.quantity, 0);
    };

    return (
        <div className="checkout-container">
            <h1>Checkout</h1>
            {cartItems.length === 0 ? (
                <p>Your cart is empty.</p>
            ) : (
                <>
                    <ul>
                        {cartItems.map((item) => (
                            <li key={item.book_id} className="cart-item">
                                <Image src={item.cover_url} alt={item.name} className="cart-item-img" />
                                <div>
                                    <h3>{item.name}</h3>
                                    <p>Quantity: {item.quantity}</p>
                                    <button onClick={() => handleRemoveItem(item.book_id)}>Remove</button>
                                </div>
                            </li>
                        ))}
                    </ul>

                    <div className="checkout-summary">
                        <h3>Total: ${calculateTotal()}</h3>
                        <button onClick={handleClearCart}>Clear Cart</button>
                        <button onClick={handleCheckout}>Proceed to Checkout</button>
                    </div>
                </>
            )}
        </div>
    );
};

export default CheckoutPage;

