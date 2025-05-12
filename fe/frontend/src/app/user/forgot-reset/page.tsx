'use client';
import { useState, FormEvent, ChangeEvent } from 'react';
import { useRouter } from 'next/navigation';
import toast from "react-hot-toast";

import api from '@/custom_lib/axios';


const ForgotResetPage = () => {
    const [email, setEmail] = useState<string>('');
    const [otpCode, setOtpCode] = useState<string>('');
    const [newPwd, setNewPwd] = useState<string>('');
    const [isForgot, setIsForgot] = useState<boolean>(true); // toggle between forgot and reset
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string>('');
    const [success, setSuccess] = useState<string>('');
    const router = useRouter();

    const handleForgotPassword = async (e: FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        setSuccess('');

        try {
            await api.post(
                '/user/forgot_email',
                { email: email }
            );
            // setSuccess('Password reset link sent to your email!');
            toast.success('Password reset link sent to your email!')
            setIsForgot(false); // After sending email, show the reset form
        } catch (error: any) {
            toast.error(error.message);
        } finally {
            setLoading(false);
        }
    };

    const handleResetPassword = async (e: FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        setSuccess('');

        try {
            await api.patch(
                '/user/reset_email',
                {
                    email: email,
                    otp_code: otpCode,
                    new_pwd: newPwd
                }
            );
            // const res = await fetch('/api/user/reset_email', {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json',
            //     },
            //     body: JSON.stringify({ email, otp_code: otpCode, new_pwd: newPwd }),
            // });

            toast.success('Password reset successful!')
            // setSuccess('Password reset successful!');
            router.push('/user/login'); // Redirect to login after successful reset
        } catch (error: any) {
            toast.error(error.message);
            // setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-md mx-auto p-6 bg-slate-900 shadow-lg rounded-lg">
            <h2 className="text-2xl font-semibold text-center mb-6">
                {isForgot ? 'Forgot Password' : 'Reset Password'}
            </h2>

            {error && <p className="text-red-500 text-center">{error}</p>}
            {success && <p className="text-green-500 text-center">{success}</p>}

            {isForgot ? (
                <form onSubmit={handleForgotPassword}>
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                            Email:
                        </label>
                        <input
                            type="email"
                            id="email"
                            value={email}
                            onChange={(e: ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
                            className="w-full p-2 mt-1 border border-gray-300 rounded-md"
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full py-2 bg-blue-600 text-white rounded-md mt-4"
                    >
                        {loading ? 'Sending...' : 'Send Reset Link'}
                    </button>
                </form>
            ) : (
                <form onSubmit={handleResetPassword}>
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                            Email:
                        </label>
                        <input
                            type="email"
                            id="email"
                            value={email}
                            onChange={(e: ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
                            className="w-full p-2 mt-1 border border-gray-300 rounded-md"
                            required
                        />
                    </div>

                    <div className="mb-4">
                        <label htmlFor="otp_code" className="block text-sm font-medium text-gray-700">
                            OTP Code:
                        </label>
                        <input
                            type="text"
                            id="otp_code"
                            value={otpCode}
                            onChange={(e: ChangeEvent<HTMLInputElement>) => setOtpCode(e.target.value)}
                            className="w-full p-2 mt-1 border border-gray-300 rounded-md"
                            required
                        />
                    </div>

                    <div className="mb-4">
                        <label htmlFor="new_pwd" className="block text-sm font-medium text-gray-700">
                            New Password:
                        </label>
                        <input
                            type="password"
                            id="new_pwd"
                            value={newPwd}
                            onChange={(e: ChangeEvent<HTMLInputElement>) => setNewPwd(e.target.value)}
                            className="w-full p-2 mt-1 border border-gray-300 rounded-md"
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full py-2 bg-blue-600 text-white rounded-md mt-4"
                    >
                        {loading ? 'Resetting...' : 'Reset Password'}
                    </button>
                </form>
            )}

            {!isForgot && !loading && (
                <button
                    onClick={() => setIsForgot(true)}
                    className="mt-4 text-sm text-blue-600 hover:underline"
                >
                    Back to Forgot Password
                </button>
            )}
        </div>
    );
};

export default ForgotResetPage;

