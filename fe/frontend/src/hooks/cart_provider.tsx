import { useEffect, useState } from "react";
import Cookies from "js-cookie";
import {
    getCartFromCookie,
    saveCartToCookie,
    clearCartCookie,
} from '@/utils/cartCookies';
import { Book } from "@/types/types"; // adjust import path

export function useCart() {
    const [cart, setCart] = useState<Book[]>(() => getCartFromCookie());

    // useEffect(() => {
    //     setCart(getCartFromCookie());
    // }, []);

    useEffect(() => {
        saveCartToCookie(cart);
    }, [cart]);

    const addToCart = (book: Book) => {
        console.log(book)
        setCart((prev) => {
            if (prev.find((b) => b.book_id === book.book_id)) return prev;
            return [...prev, book];
        });
    };

    const removeFromCart = (bookId: number) => {
        setCart((prev) => prev.filter((b) => b.book_id !== bookId));
    };

    const clearCart = () => {
        setCart([]);
        clearCartCookie();
    };

    return { cart, addToCart, removeFromCart, clearCart };
}

