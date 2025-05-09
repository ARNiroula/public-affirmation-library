import Card from '@/components/Card';
import CardContent from '@/components/CardContent';
import CardMedia from '@/components/CardMedia';
import Typography from '@/components/Typography';
import CardActionArea from '@/components/CardActionArea';
import { useRouter } from 'next/router';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DashboardPage: React.FC = () => {
    const router = useRouter();

    const [books, setBooks] = useState([]);
    const [events, setEvents] = useState([]);
    const [rooms, setRooms] = useState([]);

    useEffect(() => {
        // Fetch data for books rented
        axios.get('/api/user/books')
            .then(response => setBooks(response.data))
            .catch(error => console.error(error));

        // Fetch data for events
        axios.get('/api/user/events')
            .then(response => setEvents(response.data))
            .catch(error => console.error(error));

        // Fetch data for rooms booked
        axios.get('/api/user/rooms')
            .then(response => setRooms(response.data))
            .catch(error => console.error(error));
    }, []);

    const goToRoomsPage = () => {
        router.push('/rooms');
    };

    const goToBooksPage = () => {
        router.push('/books');
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Dashboard</h1>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                <Card sx={{ maxWidth: 500 }}>
                    <CardActionArea onClick={goToRoomsPage}>
                        <CardContent>
                            <Typography variant="h5">Your Rooms</Typography>
                            <Typography variant="body2">
                                {rooms.length > 0 ? rooms.join(', ') : 'No rooms booked'}
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                </Card>

                <Card sx={{ maxWidth: 500 }}>
                    <CardActionArea onClick={goToBooksPage}>
                        <CardContent>
                            <Typography variant="h5">Your Books</Typography>
                            <Typography variant="body2">
                                {books.length > 0 ? books.join(', ') : 'No books rented'}
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                </Card>

                <Card sx={{ maxWidth: 500 }}>
                    <CardActionArea>
                        <CardContent>
                            <Typography variant="h5">Your Events</Typography>
                            <Typography variant="body2">
                                {events.length > 0 ? events.join(', ') : 'No events attended'}
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                </Card>
            </div>

            <div style={{ marginTop: '20px' }}>
                <button onClick={goToRoomsPage}>Browse Rooms</button>
                <button onClick={goToBooksPage}>Browse Books</button>
            </div>
        </div>
    );
};

export default DashboardPage;