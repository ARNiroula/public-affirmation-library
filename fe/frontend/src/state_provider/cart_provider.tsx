import React, { createContext, useState, useContext, ReactNode } from 'react';

type CartItem = {
    book_id: number;
    name: string;
    quantity: number;
    cover_url: string;
};

type CartContextType = {
    cartItems: CartItem[];
    addToCart: (item: CartItem) => void;
    removeFromCart: (book_id: number) => void;
    clearCart: () => void;
};

const CartContext = createContext<CartContextType | undefined>(undefined);

export const useCart = (): CartContextType => {
    const context = useContext(CartContext);
    if (!context) {
        throw new Error('useCart must be used within a CartProvider');
    }
    return context;
};

type CartProviderProps = {
    children: ReactNode;
};

export const CartProvider: React.FC<CartProviderProps> = ({ children }) => {
    const [cartItems, setCartItems] = useState<CartItem[]>([]);

    const addToCart = (item: CartItem) => {
        setCartItems((prevItems) => {
            const itemIndex = prevItems.findIndex((i) => i.book_id === item.book_id);
            if (itemIndex === -1) {
                return [...prevItems, item];
            } else {
                const updatedItems = [...prevItems];
                updatedItems[itemIndex].quantity += item.quantity;
                return updatedItems;
            }
        });
    };

    const removeFromCart = (book_id: number) => {
        setCartItems((prevItems) => prevItems.filter((item) => item.book_id !== book_id));
    };

    const clearCart = () => {
        setCartItems([]);
    };

    return (
        <CartContext.Provider value={{ cartItems, addToCart, removeFromCart, clearCart }}>
            {children}
        </CartContext.Provider>
    );
};

