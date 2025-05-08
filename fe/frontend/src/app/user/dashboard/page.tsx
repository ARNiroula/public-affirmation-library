'use client';
import React from 'react';
import { useRouter } from 'next/navigation';

/* run:
    npm install @mui/material @emotion/react @emotion/styled 
    npm install @mui/icons-material
*/

import Card from '@/components/Card';
import CardContent from '@/components/CardContent';
import CardMedia from '@/components/CardMedia';
import Typography from '@/components/Typography';
import CardActionArea from '@/components/CardActionArea';

// Get the div element by its ID
const myDiv = document.getElementById('browseRooms');

if (myDiv) {
  const button = document.createElement('button');

  button.textContent = 'Click me';

  button.addEventListener('click', () => {
    alert('Button clicked!');
  });

  myDiv.appendChild(button);
} else {
  console.error('Div element with ID "browseRooms" not found.');
}


const DashboardPage: React.FC = () => {
    const router = useRouter();
    const goToRoomPage = () => {
        router.push('/room'); // Update with the actual path of your Room page
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px', padding: '20px'}}>
            <div style={{ display: 'flex', justifyContent: 'space-around', gap: '20px'}}>
                <Card key={1} sx={{ minWidth: 400, maxWidth: 500 }} /*onClick={ gotToRoomPage }*/>
                    <CardActionArea>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                                Your Rooms
                            </Typography>
                            <Typography variant='body2' color='text.secondary'>
                                List
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                </Card>
                <Card key={2} sx={{ minWidth: 400, maxWidth: 500 }} /*onClick={ gotToBooksPage }*/>
                    <CardActionArea>
                        <CardContent>
                            <Typography gutterBottom variant='h5' component='div'>
                                Your Books
                            </Typography>
                            <Typography variant='body2' color='text.secondary'>
                                List
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                </Card>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-around', gap: '20px'}}>
                <div id='browseRooms'></div>
                <div id='browseBooks'></div>
            </div>
        </div>
    ); 
}

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

export default DashboardPage;