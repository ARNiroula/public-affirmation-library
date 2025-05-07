'use client'; // if using Next.js App Router
import React, { useState, ChangeEvent, FormEvent, useRef } from 'react';
import axios, { AxiosError } from 'axios';
import { useAuthRedirect } from '@/hooks/useAuthRedirect';


const RoomUploader: React.FC = () => {
    const { loading } = useAuthRedirect();


    const [name, setName] = useState('');
    const [capacity, setCapacity] = useState(1);
    const [descr, setDescr] = useState('');
    const [file, setFile] = useState<File | null>(null);
    const [status, setStatus] = useState<string>('');
    const fileInputRef = useRef<HTMLInputElement>(null);

    const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files.length > 0) {
            setFile(e.target.files[0]);
        }
    };
    if (loading) return <p className="text-white text-center mt-10">Checking authentication...</p>;

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        if (!file || !name) {
            setStatus('Please provide a name and select a file.');
            return;
        }

        const formData = new FormData();
        formData.append('room_id', name);
        formData.append('capacity', capacity.toString());
        formData.append('descr', descr);
        formData.append('file', file);

        try {
            const response = await axios.post(
                `${process.env.NEXT_PUBLIC_API_URL}/api/room/`,
                formData, {
                withCredentials: true,
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log(response.data)
            setStatus(`Success! Room created with ID: ${response.data.room_id}`);
        } catch (error) {
            console.log(error)
            // setStatus(`Upload failed: ${error.response?.data?.error || error.message}`);
            if (error instanceof AxiosError) {
                setStatus(`Upload failed: ${error?.response?.data}`);
            }
        }
    };

    return (

        <div className="min-h-screen flex items-center justify-center bg-[#4B006E] px-4">
            <div className="bg-gray-600 p-8 rounded shadow-md w-full max-w-md">
                <h2 className="text-2xl font-semibold mb-6 text-center text-white-800">Create Room</h2>
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-white-700 mb-1">Room Name</label>
                        <input
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                            className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-white-700 mb-1">Capacity</label>
                        <input
                            type="number"
                            min={1}
                            value={capacity}
                            onChange={(e) => setCapacity(parseInt(e.target.value))}
                            required
                            className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-white-700 mb-1">Room Name</label>
                        <textarea
                            value={descr}
                            onChange={(e) => setDescr(e.target.value)}
                            rows={4}
                            required
                            className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-white-700 mb-1">Room Photo</label>
                        <input
                            type="file"
                            onChange={handleFileChange}
                            ref={fileInputRef}
                            className="hidden"
                            accept=".pdf,.doc,.docx,.jpg,.png"
                        />
                        <button
                            type="button"
                            onClick={() => fileInputRef.current?.click()}
                            className="bg-gray-200 hover:bg-gray-300 text-gray-800 py-2 px-4 rounded w-full text-center transition duration-200"
                        >
                            {file ? 'Change File' : 'Select Image'}
                        </button>
                        {file && (
                            <p className="mt-1 text-sm text-white-600 text-center truncate">{file.name}</p>
                        )}
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition duration-200"
                    >
                        Create Room
                    </button>
                </form>
                {status && <p className="mt-4 text-sm text-center text-white-600">{status}</p>}
            </div>
        </div>
    );
};

export default RoomUploader;
