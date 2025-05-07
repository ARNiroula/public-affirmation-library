'use client';
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import axios from 'axios';
import Link from 'next/link';

import { logoutUser } from '@/app/utils/auth';

const Header = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [menuOpen, setMenuOpen] = useState(false);
    const router = useRouter();
    useEffect(() => {
        const checkUserStatus = async () => {
            try {
                const url_path = `${process.env.NEXT_PUBLIC_API_URL}/api/user/status`;
                const response = await axios.get(
                    url_path,
                    { withCredentials: true },
                )

                setIsLoggedIn(response.data.authenticated);
            }
            catch (err) {
                setIsLoggedIn(false);
            }
        }

        checkUserStatus();

    }, []);


    const handleLogout = async () => {
        setMenuOpen(false);
        try {
            await logoutUser();
            setIsLoggedIn(false);
            router.push("/home")
        }
        catch (error) {
            console.log(error);
        }
    }

    const handleLogin = () => {
        // Redirect to login page or show login modal
        setMenuOpen(false);
        router.push("/user/login")
    };

    const handleRegister = () => {
        // Redirect to login page or show login modal
        setMenuOpen(false);
        router.push("/user/register")
    };

    return (
        <header style={styles.header}>
            <div className="flex justify-between items-center px-6">
                <div className="text-left">
                    <Link href="/home">
                        <h1 className="text-2xl font-bold">Public Affirmation Library</h1>
                    </Link>
                </div>

                <div className="relative inline-block text-left">
                    {/* Hamburger icon and menu toggle */}
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
                                <button
                                    onClick={handleLogout}
                                    className="block w-full text-left px-4 py-2 text-red-600 hover:bg-gray-100"
                                >
                                    Logout
                                </button>
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


    // return (
    //     <header style={styles.header}>
    //         <h1>Welcome to PAL (Public Affirmation Library)</h1>
    //         <p>
    //             Empowering our community with access to diversified resources, affordable rentals, free study room reservations, and educational events.
    //         </p>
    //         {isLoggedIn ? (
    //             <button
    //                 onClick={handleLogout}
    //                 className='bg-red-600 text-white py-2 px-6 rounded-lg hover:bg-red-500 focus:outline-none transition duration-200'
    //             >
    //                 Logout
    //             </button>
    //         ) : (
    //             <div style={{ display: 'flex space-x-7' }}>
    //                 <button
    //                     onClick={handleLogin}
    //                     className='bg-green-600 text-white py-2 px-6 rounded-lg hover:bg-green-500 focus:outline-none transition duration-200'
    //                 >
    //                     Login
    //                 </button>
    //                 <button
    //                     onClick={handleRegister}
    //                     className='bg-purple-700 text-white py-2 px-6 rounded-lg hover:bg-purple-600 focus:outline-none transition duration-200'
    //                 >
    //                     Register
    //                 </button>
    //
    //             </div>
    //
    //         )}
    //     </header>
    // );
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



export default Header;
