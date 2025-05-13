'use client';
import useSWR from 'swr';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Image from 'next/image';
import toast from "react-hot-toast";

import api from '@/custom_lib/axios';
import { useAuthRedirect } from '@/hooks/useAuthRedirect';
import { Event } from "@/types/types"
import { useCart } from "@/hooks/cart_provider"

const fetcher = (url: string) => api.get(url).then(res => res.data)

const registerForEvent = async (eventId: number) => {
    return api.patch(`/event/${eventId}/`);
};


export default function BooksPage() {
    const { loading } = useAuthRedirect();
    const { data: books, error, isLoading } = useSWR<Event[]>('event/', fetcher);
    console.log(books)
    const router = useRouter();

    if (loading) return <p className="text-white text-center mt-10">Checking authentication...</p>;
    if (isLoading) return <div className="text-center mt-10">Loading...</div>;
    if (error) return <div className="text-center mt-10 text-red-500">Failed to load books.</div>;


    return (
        <div className="relative p-6">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {books?.map(book => {
                    return (
                        <div key={book.event_id}
                            className="relative overflow-hidden brightness-110 rounded-lg shadow-xl group bg-black/90 backdrop-blur-sm transition-transform transform hover:scale-105 hover:shadow-2xl border border-white/30 hover:ring-2 hover:ring-green-300"
                        >
                            <Image
                                src={book.image_url || "/default.jpg"}
                                width={600}
                                height={400}
                                alt={`Event ${book.event_name}`}
                                className="w-full h-48 object-contain bg-white transform group-hover:scale-105 transition-transform duration-300"
                            />
                            <div className="p-4">
                                <p className="text-lg font-semibold">{book.event_name}</p>
                                <p className="text-lg font">Total Registered: {book.total_registered}</p>
                            </div>
                            <div className="absolute inset-0 bg-black/40 group-hover:bg-black/60 text-white p-4 transition-all duration-300 flex items-center justify-center text-center">
                                <div className="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                                    <button
                                        className="mt-2 bg-green-500 hover:bg-green-600 text-white py-1 px-3 rounded mr-2"
                                        onClick={async () => {
                                            try {
                                                await registerForEvent(book.event_id);
                                                toast.success(`${book.event_name} registered successfully`);
                                            } catch (error) {
                                                console.error(error);
                                                toast.error("Failed to register for event");
                                            }
                                        }}
                                    >
                                        Register for event
                                    </button>

                                </div>
                            </div>
                        </div>
                    );
                })}

            </div>
            {/* Modal */}
        </div>
    );
}
