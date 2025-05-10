'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import toast from "react-hot-toast";

import { loginUser } from '@/app/utils/auth';
import FormError from '@/components/formerror';

const LoginPage: React.FC = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    // const [error, setError] = useState('');
    const router = useRouter();

    const handleLogin = async (event: React.FormEvent) => {
        event.preventDefault();
        if (username === "" || password === "") {
            return;
        }
        try {
            await loginUser(username, password);
            router.push("/home");
        } catch (e) {
            // setError(`Login User Failed => ${e}`);
            toast.error(`Login Failed: Incorrect username or password`);
        }
    };

    const styles: React.CSSProperties = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '100vh',
        backgroundColor: '#4b006e',
    };

    const headerStyles: React.CSSProperties = {
        width: '100%',
        padding: '10px 20px',
        backgroundColor: '#007BFF',
        color: 'white',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
    };

    const navStyles: React.CSSProperties = {
        display: 'flex',
        gap: '20px',
    };

    const linkStyles: React.CSSProperties = {
        color: 'white',
        textDecoration: 'none',
        fontWeight: 'bold',
    };

    const formStyles: React.CSSProperties = {
        width: '300px',
        padding: '20px',
        backgroundColor: '#000',
        borderRadius: '5px',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
    };

    const inputGroupStyles: React.CSSProperties = {
        marginBottom: '1rem',
    };

    const inputStyles: React.CSSProperties = {
        width: '100%',
        padding: '8px',
        marginTop: '5px',
        borderRadius: '4px',
        border: '1px solid #ccc',
    };

    const buttonStyles: React.CSSProperties = {
        width: '100%',
        padding: '10px',
        backgroundColor: '#007BFF',
        color: '#fff',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
    };

    return (
        <div style={styles}>
            {/* Single Header with title and navigation links */}


            {/* Login Form */}
            <form onSubmit={handleLogin} style={formStyles}>
                <h1 style={{ textAlign: 'center', color: 'white' }}>Login</h1>
                {/* <FormError message={error} /> */}
                <div style={inputGroupStyles}>
                    <label htmlFor="username" style={{ color: 'white' }}>Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <div style={inputGroupStyles}>
                    <label htmlFor="password" style={{ color: 'white' }}>Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <button type="submit" style={buttonStyles}>Login</button>
            </form>
        </div>
    );
};

export default LoginPage;
