'use client';
import React from 'react';
import { useRouter } from 'next/navigation';

const HomePage: React.FC = () => {

    const router = useRouter();
    const goToRoomPage = () => {
        router.push('/room'); // Update with the actual path of your Room page
    };


    return (
        <div style={styles.container}>
            <main style={styles.main}>
                <section style={styles.section}>
                    <h2>Our Services</h2>
                    <ul>
                        <li>Book Rental Service - Browse and rent books from various topics and genres.</li>
                        <li>Event Hosting - Seminars and exhibitions on diverse topics.</li>
                        <li>Free Study Room Reservations - Perfect for group studies or meetings.</li>
                    </ul>
                </section>
                <section style={styles.section}>
                    <h2>Explore PAL</h2>
                    <div style={styles.buttonGroup}>
                        <button style={styles.button}>Browse Books</button>
                        <button style={styles.button}>Upcoming Events</button>
                        <button style={styles.button} onClick={goToRoomPage}>Reserve a Room</button>
                    </div>
                </section>
            </main>
            <footer style={styles.footer}>
                <p>&copy; 2025 Public Affirmation Library. All rights reserved.</p>
            </footer>
        </div>
    );
};

const styles: Record<string, React.CSSProperties> = {
    container: {
        fontFamily: 'Arial, sans-serif',
        lineHeight: '1.6',
        color: '#333',
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
    },
    header: {
        backgroundColor: '#007BFF',
        color: '#fff',
        padding: '20px',
        textAlign: 'center',
    },
    main: {
        flex: 1,
        padding: '20px',
    },
    section: {
        marginBottom: '20px',
        padding: '10px',
        border: '1px solid #ddd',
        borderRadius: '5px',
        backgroundColor: '#f9f9f9',
    },
    buttonGroup: {
        display: 'flex',
        justifyContent: 'space-evenly',
        marginTop: '10px',
    },
    button: {
        padding: '10px 20px',
        backgroundColor: '#007BFF',
        color: '#fff',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
        fontSize: '16px',
    },
    footer: {
        textAlign: 'center',
        padding: '10px',
        backgroundColor: '#f1f1f1',
    },
};

export default HomePage;
