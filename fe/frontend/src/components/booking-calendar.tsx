'use client';

import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import { useRouter } from 'next/navigation';
import useSWR from 'swr';
import api from '@/custom_lib/axios';

interface Booking {
    start_datetime: string;
    end_datetime: string;
}

interface RoomBookingsProps {
    roomId: number;
}

const fetchBookings = (url: string) => api.get(url).then((res) => res.data);

const RoomBookingCalendar: React.FC<RoomBookingsProps> = ({ roomId }) => {
    const [date, setDate] = useState<Date | null>(null);
    const { data: bookings, error, isLoading } = useSWR<Booking[]>(`/room/${roomId}/bookings/`, fetchBookings);

    const router = useRouter();

    useEffect(() => {
        if (date) {
            // You could update the state to fetch available slots based on the selected date
            console.log('Selected Date:', date);
        }
    }, [date]);

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Failed to load bookings.</div>;

    // Map the booked dates to an array of strings for comparison
    const bookedDates = bookings?.map((booking) => {
        const date = new Date(booking.start_datetime);
        return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
    }) || [];

    const tileClassName = ({ date }: { date: Date }) => {
        const dateString = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
        return bookedDates.includes(dateString) ? 'bg-red-500' : ''; // Mark booked dates
    };

    const handleDateChange = (newDate: Date) => {
        setDate(newDate);
        // You could redirect to a booking form page with the selected date
        router.push(`/booking/${roomId}?date=${newDate.toISOString()}`);
    };

    return (
        <div className="p-4">
            <h2>Select a Date</h2>
            <Calendar
                onChange={handleDateChange}
                value={date}
                tileClassName={tileClassName}
            />
        </div>
    );
};

export default RoomBookingCalendar;
