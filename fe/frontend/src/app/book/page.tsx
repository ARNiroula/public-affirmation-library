'use client';
import useSWR from 'swr';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Image from 'next/image';
import toast from "react-hot-toast";

import api from '@/custom_lib/axios';
import { useAuthRedirect } from '@/hooks/useAuthRedirect';
import { Book } from "@/types/types"
import { useCart } from "@/hooks/cart_provider"
import BookModal from '@/components/book_modal';

const fetcher = (url: string) => api.get(url).then(res => res.data)


export default function BooksPage() {
    const { loading } = useAuthRedirect();
    const { data: books, error, isLoading } = useSWR<Book[]>('book/', fetcher);
    const { cart, addToCart, removeFromCart } = useCart();
    const [expandedBook, setExpandedBook] = useState<Book | null>(null);
    const router = useRouter();

    if (loading) return <p className="text-white text-center mt-10">Checking authentication...</p>;
    if (isLoading) return <div className="text-center mt-10">Loading...</div>;
    if (error) return <div className="text-center mt-10 text-red-500">Failed to load books.</div>;

    // const isInCart = (bookId: number) => cart.some(b => b.book_id === bookId);

    return (
        <div className="relative p-6">
            {/* Sticky cart icon */}
            <div className="fixed bottom-6 right-6 z-50">
                <button
                    className="relative bg-purple-700 text-white p-3 rounded-full shadow-lg hover:bg-blue-600 transition"
                    onClick={() => router.push("/book/checkout/")}
                >
                    🛒
                    {cart.length > 0 && (
                        <span className="absolute -top-1 -right-1 bg-red-600 text-white rounded-full text-xs w-5 h-5 flex items-center justify-center">
                            {cart.length}
                        </span>
                    )}
                </button>
            </div>
            {/* Books Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {books?.map(book => {
                    const inCart = cart.some(b => b.book_id === book.book_id);
                    return (
                        <div key={book.book_id}
                            className="relative overflow-hidden brightness-110 rounded-lg shadow-xl group bg-black/90 backdrop-blur-sm transition-transform transform hover:scale-105 hover:shadow-2xl border border-white/30 hover:ring-2 hover:ring-green-300"
                        >
                            <Image
                                src={book.cover_url || "/default.jpg"}
                                width={600}
                                height={400}
                                alt={`Book ${book.name}`}
                                className="w-full h-48 object-contain bg-white transform group-hover:scale-105 transition-transform duration-300"
                            />
                            <div className="p-4">
                                <p className="text-lg font-semibold">{book.name}</p>
                                <p className="text-lg font">Available: {book.available_copies}</p>
                            </div>
                            <div className="absolute inset-0 bg-black/40 group-hover:bg-black/60 text-white p-4 transition-all duration-300 flex items-center justify-center text-center">
                                <div className="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                                    {inCart ? (
                                        <button
                                            className="mt-2 bg-red-500 hover:bg-red-600 text-white py-1 px-3 rounded mr-2"
                                            onClick={() => {
                                                removeFromCart(book.book_id);
                                                toast.success(`${book.name} removed from cart`);
                                            }}
                                        >
                                            Remove from Cart
                                        </button>
                                    ) : (
                                        <button
                                            className="mt-2 bg-green-500 hover:bg-green-600 text-white py-1 px-3 rounded mr-2"
                                            onClick={() => {
                                                addToCart(book);
                                                toast.success(`${book.name} added to cart`);
                                            }}
                                        >
                                            Add to Cart
                                        </button>
                                    )}
                                    <button
                                        className="mt-2 bg-white text-black py-1 px-3 rounded"
                                        onClick={() => setExpandedBook(book)}
                                    >
                                        Expand
                                    </button>
                                </div>
                            </div>
                        </div>
                    );
                })}

            </div>

            {/* Modal */}
            {expandedBook && (
                <BookModal book={expandedBook} onClose={() => setExpandedBook(null)} />
            )}
        </div>
    );
}


{/* <div key={book.book_id} className="relative overflow-hidden rounded-lg shadow-md group"> */ }
{/*     <Image */ }
{/*         src={book.cover_url || "/default.jpg"} */ }
{/*         width={600} */ }
{/*         height={400} */ }
{/*         alt={`Book ${book.name}`} */ }
{/*         className="w-full h-48 object-contain bg-white transform group-hover:scale-105 transition-transform duration-300" */ }
{/*     /> */ }
{/*     <div className="p-4"> */ }
{/*         <p className="text-lg font-semibold">{book.name}</p> */ }
{/*         <p className="text-lg font">Available: {book.available_copies}</p> */ }
{/*     </div> */ }
{/*     <div className="absolute inset-0 bg-black/40 group-hover:bg-black/60 text-white p-4 transition-all duration-300 flex items-center justify-center text-center"> */ }
{/*         <div className="opacity-0 group-hover:opacity-100 transition-opacity duration-300"> */ }
{/*             <button */ }
{/*                 className="mt-2 bg-green-500 hover:bg-green-600 text-white py-1 px-3 rounded mr-2" */ }
{/*                 onClick={ */ }
{/*                     () => { */ }
{/*                         addToCart(book); */ }
{/*                         toast.success(`${book.name} added to cart`); */ }
{/*                     } */ }
{/*                 } */ }
{/*             > */ }
{/*                 Add to Cart */ }
{/*             </button> */ }
{/*             <button */ }
{/*                 className="mt-2 bg-white text-black py-1 px-3 rounded" */ }
{/*                 onClick={() => setExpandedBook(book)} */ }
{/*             > */ }
{/*                 Expand */ }
{/*             </button> */ }
{/*         </div> */ }
{/*     </div> */ }
{/* </div> */ }

