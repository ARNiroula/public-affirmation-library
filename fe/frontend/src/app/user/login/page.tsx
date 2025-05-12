'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import toast from "react-hot-toast";
import Link from 'next/link';

import { useAuth } from '@/context/AuthContext';
import { loginUser } from '@/app/utils/auth';

const LoginPage: React.FC = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    // const [error, setError] = useState('');
    const router = useRouter();
    const { setIsLoggedIn } = useAuth();

    const handleLogin = async (event: React.FormEvent) => {
        event.preventDefault();
        if (username === "" || password === "") {
            return;
        }
        try {
            await loginUser(username, password);
            setIsLoggedIn(true);  // Set the login state to true immediately
            toast.success(`Welcome: ${username}`)
            router.push("/home");
        } catch (e) {
            // setError(`Login User Failed => ${e}`);
            console.log(e);
            toast.error(`Login Failed: Incorrect username or password`);
        }
    };

    const styles: React.CSSProperties = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '100vh',
        // backgroundColor: '#4b006e',
    };

    const formStyles: React.CSSProperties = {
        width: '300px',
        padding: '20px',
        backgroundColor: '#0F172A',
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

            {/* Forgot Password Link */}
            <div style={{
                width: '300px',
                padding: '20px',
                backgroundColor: '#0F172A',
                borderRadius: '5px',
                boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
            }}>
                <Link
                    href="/user/forgot-reset"
                    style={{
                        color: '#007BFF',
                        textDecoration: 'none',
                        fontSize: '14px',
                        display: 'block',
                        textAlign: 'center',
                    }}
                >
                    Forgot Password?
                </Link>
            </div>

        </div>
    );
};

export default LoginPage;
