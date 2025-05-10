import { useEffect, useState, useCallback, useRef } from "react";
import api from "@/custom_lib/axios";
import { Book } from "@/types/types";

let debounceTimer: NodeJS.Timeout;

export function useCart() {
    const [cart, setCart] = useState<Book[]>([]);
    const isFirstLoad = useRef(true);

    // Fetch cart from Redis on initial load
    useEffect(() => {
        const fetchCart = async () => {
            try {
                const res = await api.get("/rent/cache");
                const books = Array.isArray(res.data)
                    ? res.data
                    : Array.isArray(res.data.books)
                        ? res.data.books
                        : [];

                setCart(books);
            } catch (error) {
                console.error("Error fetching cart from cache:", error);
            }
        };
        fetchCart();
    }, []);

    // Debounced cart save to Redis
    useEffect(() => {
        if (isFirstLoad.current) {
            isFirstLoad.current = false;
            return;
        }

        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            api.post("/rent/cache", { books: cart })
                .then(() => console.log("Cart synced with Redis"))
                .catch((err) => console.error("Error syncing cart:", err));
        }, 800); // debounce delay in ms

        return () => clearTimeout(debounceTimer); // clean up on unmount
    }, [cart]);

    const addToCart = useCallback((book: Book) => {
        setCart((prev) => {
            if (prev.find((b) => b.book_id === book.book_id)) return prev;
            return [...prev, book];
        });
    }, []);

    const removeFromCart = useCallback((bookId: number) => {
        setCart((prev) => prev.filter((b) => b.book_id !== bookId));
    }, []);

    const clearCart = useCallback(() => {
        setCart([]);
        api.post("/rent/cache", { books: [] }).catch(err =>
            console.error("Error clearing cart:", err)
        );
    }, []);

    return { cart, addToCart, removeFromCart, clearCart };
}

