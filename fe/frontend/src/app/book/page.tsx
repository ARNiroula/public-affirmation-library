'use client';

import useSWR from 'swr';
import { useRouter } from 'next/navigation';
import Image from 'next/image';

// import styles from './room.module.css'
import api from '@/custom_lib/axios';
import { useAuthRedirect } from '@/hooks/useAuthRedirect';

interface Book {
    book_id: number;
    isbn: string;
    name: string;
    topic: string;
    summary: string;
    pub_date: Date;
    cover_url: string;
}

const fetcher = (url: string) => api.get(url).then(res => res.data)

export default function RoomsPage() {
    const { loading } = useAuthRedirect();

    const { data: books, error, isLoading } = useSWR<Book[]>('room/', fetcher);
    const router = useRouter();

    if (loading) return <p className="text-white text-center mt-10">Checking authentication...</p>;
    if (isLoading) return <div className="text-center mt-10">Loading...</div>;
    if (error) return <div className="text-center mt-10 text-red-500">Failed to load rooms.</div>;

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
                        alt={`Book ${book.book_id}`}
                        className="w-full h-48 object-cover transform group-hover:scale-105 transition-transform duration-300"
                    />
                    <div className="p-4">
                        <p className="text-lg font-semibold">Room {book.book_id}</p> {/* Room ID Caption */}
                        <button
                            onClick={() => router.push(`/book/${book.book_id}/rental`)}
                            className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-3 rounded"
                        >
                            Rent Now
                        </button>
                    </div>

                    <div className="absolute inset-0 bg-black bg-opacity-60 text-white p-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end">
                        <p className="text-sm">Summary: {book.summary}</p>
                        <p className="text-sm">Published Date: {book.pub_date.toDateString()}</p>
                        <button
                            onClick={() => router.push(`/book/${book.book_id}/rental`)}
                            className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-3 rounded"
                        >
                            Rent Now
                        </button>
                    </div>
                </div>
            ))}
        </div>
    );
}
