import React from 'react';
import Image from 'next/image';
import axios, { AxiosError } from 'axios';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';

type Room = {
    id: number;
    name: string;
    capacity: number;
    descr: string;
    image_url: string;
};

export default async function RoomPage({ params }: { params: { id: string } }) {
    const cookieStore = await cookies();
    try {
        const { id } = await params
        const res = await axios.get<Room>(
            `${process.env.NEXT_PUBLIC_API_URL}/api/room/${id}/`,
            {
                headers: {
                    Cookie: cookieStore
                        .getAll()
                        .map(c => `${c.name}=${c.value}`)
                        .join('; '),
                },
                withCredentials: true,
            }
        );

        // const room = res.data;
        // const res = await axios.get<Room>(`${process.env.NEXT_PUBLIC_API_URL}/api/room/${params.id}/`);
        const room = res.data;
        console.log(room.image_url)
        if (room.image_url === null) {
            room.image_url = "/default.jpg";
        }

        return (
            <div className="max-w-md mx-auto mt-10 bg-white p-6 shadow rounded">
                <h2 className="text-2xl font-bold mb-2">{room.name}</h2>
                <p className="text-gray-600 mb-2">Capacity: {room.capacity}</p>
                <p className="text-gray-700 mb-4">{room.descr}</p>

                <div className="mb-4">
                    <p className="font-medium">Attached Document:</p>
                    {room.image_url.endsWith('.jpg') || room.image_url.endsWith('.png') ? (
                        <Image
                            src={room.image_url}
                            fill={true}
                            alt="Room document"
                            className="mt-2 max-h-64 object-contain border rounded"
                        />
                    ) : (
                        <a
                            href={room.image_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-blue-600 hover:underline mt-2 block"
                        >
                            View Document
                        </a>
                    )}
                </div>
            </div>
        );
    } catch (err) {
        if (err instanceof AxiosError) {
            if (err.response?.status === 401 || err.response?.status === 403) {
                redirect('user/login');
            }

        }
        // If 401 Unauthorized, redirect to login

        // Optional: handle other errors
        throw err;
    }
}

