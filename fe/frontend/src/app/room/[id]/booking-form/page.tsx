
// app/room/[roomId]/booking-form.tsx
'use client';

import { useState } from 'react';
import { useRouter, useParams } from 'next/navigation';
import api from '@/custom_lib/axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css'; // import the CSS for the datepicker
import { AxiosError } from 'axios';
import toast from "react-hot-toast";
// import { addDays } from 'date-fns'; // Helps to prevent past dates in the calendar


const BookingForm = () => {
    const params = useParams(); // roomId comes from [roomId] folder
    const roomId = Number(params.id)
    const [numOfPeople, setNumOfPeople] = useState(1);
    const [description, setDescription] = useState('');
    const [startDate, setStartDate] = useState<Date | null>(null);
    const [endDate, setEndDate] = useState<Date | null>(null);
    // const [error, setError] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);

    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!roomId) return;
        setIsSubmitting(true);

        if (description === "") {
            toast.error('Please Enter Description');
        }
        if (!startDate || !endDate || startDate >= endDate) {
            toast.error('Please select valid start and end dates.');
            // setError('Please select valid start and end dates.');
            setIsSubmitting(false);
            return;
        }

        try {
            await api.post('/booking/', {
                room: roomId,
                num_of_people: numOfPeople,
                description,
                start_datetime: startDate.toISOString(),
                end_datetime: endDate.toISOString(),
            });
            toast.success(`Room ${roomId} Booking SuccessFul!`);
            router.push(`/room`); // Redirect after booking is successful
        } catch (err) {
            if (err instanceof AxiosError) {
                const errMsg = err.response?.data.message
                console.log(errMsg.response);
                toast.error(`Error booking the room: ${errMsg}`);
                // setError(`Error booking the room: ${errMsg}`);
            }
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <div className="p-6 bg-black/60 backdrop-blur-sm text-white rounded-lg shadow-xl">
            <h2 className="text-2xl mb-4">Booking Form for Room {roomId}</h2>

            {/* {error && <div className="text-red-500">{error}</div>} */}

            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block">Number of People</label>
                    <input
                        type="number"
                        value={numOfPeople}
                        onChange={(e) => setNumOfPeople(Number(e.target.value))}
                        min="1"
                        max="20"
                        className="w-full p-2 border rounded-md"
                        required
                    />
                </div>

                <div>
                    <label className="block">Description</label>
                    <textarea
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        className="w-full p-2 border rounded-md"
                        rows={4}
                        required
                    />
                </div>

                <div>
                    <label className="block">Start Date</label>
                    <DatePicker
                        selected={startDate}
                        onChange={(date: Date | null) => setStartDate(date)}
                        minDate={new Date()} // Prevent selecting past dates
                        showTimeSelect
                        dateFormat="Pp" // Example of format: May 7th, 2025 4:00 PM
                        className="w-full p-2 border rounded-md"
                        placeholderText="Select start date"
                        required
                    />
                </div>

                <div>
                    <label className="block">End Date</label>
                    <DatePicker
                        selected={endDate}
                        onChange={(date: Date | null) => setEndDate(date)}
                        minDate={startDate || new Date()} // Prevent selecting a start date before the selected start date
                        showTimeSelect
                        dateFormat="Pp" // Example of format: May 7th, 2025 4:00 PM
                        className="w-full p-2 border rounded-md"
                        placeholderText="Select end date"
                        required
                    />
                </div>

                <div>
                    <button
                        type="submit"
                        className="mt-4 bg-blue-500 text-white py-2 px-4 rounded disabled:bg-gray-300"
                        disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Booking...' : 'Submit Booking'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default BookingForm;

