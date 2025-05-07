'use client';

import useSWR from 'swr';
import { useRouter } from 'next/navigation';
import Image from 'next/image';

// import styles from './room.module.css'
import api from '@/custom_lib/axios';
import { useAuthRedirect } from '@/hooks/useAuthRedirect';

interface Room {
    room_id: number;
    capacity: number;
    descr: string;
    image_url: string;
}

const fetcher = (url: string) => api.get(url).then(res => res.data)

export default function RoomsPage() {
    const { loading } = useAuthRedirect();

    const { data: rooms, error, isLoading } = useSWR<Room[]>('room/', fetcher);
    const router = useRouter();

    if (loading) return <p className="text-white text-center mt-10">Checking authentication...</p>;
    if (isLoading) return <div className="text-center mt-10">Loading...</div>;
    if (error) return <div className="text-center mt-10 text-red-500">Failed to load rooms.</div>;

    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 p-6">
            {rooms?.map(room => (
                <div
                    key={room.room_id}
                    className="relative overflow-hidden rounded-lg shadow-md group"
                >
                    <Image
                        src={room.image_url || "/default.jpg"}
                        width={600}
                        height={400}
                        alt={`Room ${room.room_id}`}
                        className="w-full h-48 object-cover transform group-hover:scale-105 transition-transform duration-300"
                    />
                    <div className="p-4">
                        <p className="text-lg font-semibold">Room {room.room_id}</p> {/* Room ID Caption */}
                        <button
                            onClick={() => router.push(`/room/${room.room_id}/booking-form`)}
                            className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-3 rounded"
                        >
                            Book Now
                        </button>
                    </div>

                    <div className="absolute inset-0 bg-black bg-opacity-60 text-white p-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end">
                        <p className="text-sm">Description: {room.descr}</p>
                        <p className="text-sm">Capacity: {room.capacity}</p>
                        <button
                            onClick={() => router.push(`/room/${room.room_id}/booking-form`)}
                            className="mt-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-3 rounded"
                        >
                            Book Now
                        </button>
                    </div>
                </div>
            ))}
        </div>
    );
}
