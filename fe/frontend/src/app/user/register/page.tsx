'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';


import { registerUser, RegisterUserParams } from '@/app/utils/auth';
import FormError from '@/components/formerror';

const RegisterPage: React.FC = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [rePassword, setRePassword] = useState('');
    const [error, setError] = useState('');
    // Error Message

    const router = useRouter();

    const handleRegister = async (event: React.FormEvent) => {
        event.preventDefault();
        setError('');
        if (username === "" || password === "") {
            setError("UserName is Empty");
            return
        }
        if (password !== rePassword) {
            setError("Password don't match");
            return
        }
        try {
            const body: RegisterUserParams = {
                username: username,
                email: email,
                first_name: firstName,
                last_name: lastName,
                password: password,
            }
            await registerUser(body)
            router.push("/user/login")
        }
        catch (e) {
            setError(`Register User Failed => ${e}`);
            // alert(`Register User Failed => ${e}`)
        }
        console.log('Logging in with:', { username, password });
        // Add your login logic here, such as calling an API
    };

    const styles: React.CSSProperties = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '100vh',
        backgroundColor: '#4b006e',
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
            <h1>Register User</h1>
            <form onSubmit={handleRegister} style={formStyles}>
                <FormError message={error} />
                <div style={inputGroupStyles}>
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <div style={inputGroupStyles}>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <div style={inputGroupStyles}>
                    <label htmlFor="firstName">First Name:</label>
                    <input
                        type="text"
                        id="firstName"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <div style={inputGroupStyles}>
                    <label htmlFor="lastName">Last Name:</label>
                    <input
                        type="text"
                        id="lastName"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <div style={inputGroupStyles}>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <div style={inputGroupStyles}>
                    <label htmlFor="rePassword">Rewrite Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={rePassword}
                        onChange={(e) => setRePassword(e.target.value)}
                        style={inputStyles}
                    />
                </div>
                <button type="submit" style={buttonStyles}>Register</button>
            </form>
        </div>
    );
};

export default RegisterPage;
