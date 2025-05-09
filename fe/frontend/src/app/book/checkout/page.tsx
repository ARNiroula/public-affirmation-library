'use client';
import { useCart } from "@/hooks/cart_provider";
import Cookies from "js-cookie";
import Image from "next/image";
import toast from "react-hot-toast";

import api from "@/custom_lib/axios";

export default function CheckoutPage() {
    const { cart, removeFromCart, clearCart } = useCart();
    console.log("Raw cart cookie:", Cookies.get("cart"));

    const confirmCheckout = async () => {
        try {
            const bookIds = cart.map(book => book.book_id);
            await api.post(
                "/rent/",
                { book_ids: bookIds }
            )
            toast.success("Checkout successful!");
            clearCart();
        } catch (err) {
            console.error("Checkout error:", err);
            toast.error(`Error: ${err}`);
        }
    }

    return (
        <div className="p-6 bg-black/60 backdrop-blur-sm text-white rounded-lg shadow-xl">
            <h1 className="text-2xl font-bold mb-6">Your Cart</h1>

            {cart.length === 0 ? (
                <p className="text-gray-500">Your cart is empty.</p>
            ) : (
                <>
                    <div className="grid gap-4">
                        {cart.map((book) => (
                            <div
                                key={book.book_id}
                                className="flex items-center bg-[#FFFDD0] shadow p-4 rounded-lg"
                            >
                                <Image
                                    src={book.cover_url || "/default.jpg"}
                                    width={80}
                                    height={100}
                                    alt={book.name}
                                    className="object-contain mr-4 bg-gray-100"
                                />
                                <div className="flex-grow">
                                    <h2 className="font-semibold text-black">{book.name}</h2>
                                    <p className="text-sm text-black">Topic: {book.topic_display}</p>
                                    <p className="text-sm text-black">ISBN: {book.isbn}</p>
                                    <p className="text-sm text-black">Book Id: {book.book_id}</p>
                                </div>
                                <button
                                    onClick={() => {
                                        removeFromCart(book.book_id);
                                        toast.success("Book removed from cart");
                                    }}
                                    className="ml-4 text-red-600 hover:text-red-800 text-sm"
                                >
                                    Remove
                                </button>
                            </div>
                        ))}
                    </div>

                    <div className="mt-8 flex justify-between items-center">
                        <p className="text-lg font-semibold">
                            Total books: {cart.length}
                        </p>
                        <button
                            onClick={confirmCheckout}
                            className={`px-5 py-2 rounded-lg text-white transition ${cart.length === 0
                                ? "bg-gray-400 cursor-not-allowed"
                                : "bg-green-500 hover:bg-green-600"
                                }`}
                            disabled={cart.length === 0}
                        >
                            Confirm Checkout
                        </button>
                    </div>
                </>
            )}
        </div>
    );
}

