'use client';

import useSWR from 'swr';
// import { useRouter } from 'next/navigation';
import Image from 'next/image';

// import styles from './room.module.css'
import api from '@/custom_lib/axios';
import { useAuthRedirect } from '@/hooks/useAuthRedirect';
import { useCart } from '@/state_provider/cart_provider';

interface Book {
    book_id: number;
    available_copies: number;
    isbn: string;
    name: string;
    topic: string;
    topic_display: string;
    summary: string;
    pub_date: string;
    cover_url: string;
}

const fetcher = (url: string) => api.get(url).then(res => res.data)

export default function BooksPage() {
    const { loading } = useAuthRedirect();
    // const router = useRouter();
    const { addToCart } = useCart();

    const { data: books, error, isLoading } = useSWR<Book[]>('book/', fetcher);

    if (loading) return <p className="text-white text-center mt-10">Checking authentication...</p>;
    if (isLoading) return <div className="text-center mt-10">Loading...</div>;
    if (error) return <div className="text-center mt-10 text-red-500">Failed to load rooms.</div>;

    const handleAddToCart = (book: Book) => {
        const cartItem = {
            book_id: book.book_id,
            name: book.name,
            quantity: 1,
            cover_url: book.cover_url,
        };
        addToCart(cartItem);
    }

    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 p-6">
            {books?.map(book => (
                <div
                    key={book.book_id}
                    className="relative overflow-hidden rounded-lg shadow-md group"
                >
                    <Image
                        src={book.cover_url || "/default.jpg"}
                        width={600}
                        height={400}
                        alt={`Book ${book.name}`}
                        className="w-full h-48 object-contain bg-white transform group-hover:scale-105 transition-transform duration-300"
                    // className="w-full h-48 object-cover transform group-hover:scale-105 transition-transform duration-300"
                    />
                    <div className="p-4">
                        <p className="text-lg font-semibold">{book.name}</p>
                        <p className="text-lg font"> Available: {book.available_copies}</p>
                    </div>
                    <div className="absolute inset-0 bg-black/40 group-hover:bg-black/60 text-white p-4 transition-all duration-300 flex items-center justify-center text-center">
                        <div className="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <p className="text-sm mb-2">ISBN: {book.isbn}</p>
                            {/* <p className="text-sm mb-2">Summary: {book.summary}</p> */}
                            <p className="text-sm mb-2">Topic: {book.topic_display}</p>
                            <p className="text-sm mb-2">Published Date: {book.pub_date}</p>
                            <button
                                onClick={() => handleAddToCart(book)}
                                className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-3 rounded"
                            >
                                Rent
                            </button>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
}
