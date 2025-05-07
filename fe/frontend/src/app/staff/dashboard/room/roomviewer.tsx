'use client';

import React, { useEffect, useState } from 'react';
import Image from "next/image";
import axios, { AxiosError } from 'axios';

type Room = {
    id: number;
    name: string;
    capacity: number;
    descr: string;
    image_url: string;
};


const RoomViewer: React.FC = () => {
    const [room, setRoom] = useState<Room | null>(null);
    const [error, setError] = useState<string>('');

    useEffect(() => {
        const fetchRoom = async () => {
            try {
                const response = await axios.get<Room>(
                    'http://localhost:8000/api/rooms/11'
                ); // Change ID as needed
                setRoom(response.data);
            } catch (err) {
                if (err instanceof AxiosError) {
                    setError('Failed to fetch room: ' + err.message);
                }
            }
        };

        fetchRoom();
    }, []);

    if (error) return <p className="text-red-500">{error}</p>;
    if (!room) return <p>Loading...</p>;

    return (
        <div className="max-w-md mx-auto mt-10 bg-white p-6 shadow rounded">
            <h2 className="text-2xl font-bold mb-2">{room.name}</h2>
            <p className="text-gray-600 mb-2">Capacity: {room.capacity}</p>
            <p className="text-gray-700 mb-4">{room.image_url}</p>

            <div className="mb-4">
                <p className="font-medium">Attached Document:</p>
                {room.image_url.endsWith('.jpg') || room.image_url.endsWith('.png') ? (
                    <Image
                        src={room.image_url}
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
};

export default RoomViewer;

