'use client';
import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import toast from "react-hot-toast";

import { useAuth } from '@/context/AuthContext';
import { logoutUser } from '@/app/utils/auth';

const Header = () => {
    const { isLoggedIn, setIsLoggedIn } = useAuth();
    const [menuOpen, setMenuOpen] = useState(false);
    const router = useRouter();

    // Update `isLoggedIn` state after login
    const handleLogin = () => {
        setMenuOpen(false);
        router.push("/user/login");
    };

    const handleProfie = () => {
        setMenuOpen(false);
        router.push("/user/profile");
    };

    const handleLogout = async () => {
        setMenuOpen(false);
        try {
            await logoutUser();
            setIsLoggedIn(false);  // Immediately update the login state to reflect logout
            toast.success("Logged Out!!")
            router.refresh()
            router.push("/home");
        } catch (error) {
            console.log(error);
        }
    };

    const handleRegister = () => {
        setMenuOpen(false);
        router.push("/user/register");
    };

    return (
        <header style={styles.header}>
            <div style={styles.container}>
                {/* Title */}
                <div style={styles.titleContainer}>
                    <Link href="/home">
                        <h1 style={styles.title}>Public Affirmation Library</h1>
                    </Link>
                </div>

                {/* Centered Navigation Links */}
                <nav style={styles.nav}>
                    <Link href="/book" style={styles.link}>Books</Link>
                    <Link href="/room" style={styles.link}>Rooms</Link>
                    <Link href="/events" style={styles.link}>Events</Link>
                </nav>

                {/* Hamburger Menu */}
                <div className="relative inline-block text-left" style={styles.menuContainer}>
                    <div
                        className="cursor-pointer p-2 bg-white rounded shadow-md inline-block"
                        onClick={() => setMenuOpen(prev => !prev)}
                    >
                        <div className="w-6 h-1 bg-black mb-1"></div>
                        <div className="w-6 h-1 bg-black mb-1"></div>
                        <div className="w-6 h-1 bg-black"></div>
                    </div>

                    {menuOpen && (
                        <div className="absolute right-0 mt-2 w-40 bg-white border rounded shadow-lg z-10">
                            {isLoggedIn ? (
                                <>
                                    <button
                                        onClick={handleProfie}
                                        className="block w-full text-left px-4 py-2 text-slate-600 hover:bg-gray-100"
                                    >
                                        Profile
                                    </button>
                                    <button
                                        onClick={handleLogout}
                                        className="block w-full text-left px-4 py-2 text-red-600 hover:bg-gray-100"
                                    >
                                        Logout
                                    </button>
                                </>
                            ) : (
                                <>
                                    <button
                                        onClick={handleLogin}
                                        className="block w-full text-left px-4 py-2 text-green-600 hover:bg-gray-100"
                                    >
                                        Login
                                    </button>
                                    <button
                                        onClick={handleRegister}
                                        className="block w-full text-left px-4 py-2 text-purple-700 hover:bg-gray-100"
                                    >
                                        Register
                                    </button>
                                </>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </header>
    );
};

const styles: Record<string, React.CSSProperties> = {
    header: {
        backgroundColor: '#007BFF',
        color: '#fff',
        padding: '10px 20px',
        position: 'relative',
    },
    container: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    titleContainer: {
        flex: 1,
        textAlign: 'left',
    },
    title: {
        fontWeight: 'bold',
        fontSize: '24px',
        margin: 0,
    },
    nav: {
        flex: 1,
        display: 'flex',
        justifyContent: 'center',
        gap: '200px', // Increased gap to add more space between links
    },
    link: {
        color: 'white',
        textDecoration: 'none',
        fontWeight: 'bold',
        fontSize: '16px',
    },
    menuContainer: {
        flex: 1,
        textAlign: 'right',
    },
};

export default Header;

