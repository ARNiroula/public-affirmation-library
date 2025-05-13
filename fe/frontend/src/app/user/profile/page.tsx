'use client';

import { useEffect, useState } from 'react';
import { getUserProfile, updateUserProfile } from '@/app/utils/auth';

interface Profile {
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    date_joined: string;
}

export default function ProfilePage() {
    const [profile, setProfile] = useState<Profile | null>(null);
    const [form, setForm] = useState({
        username: '',
        first_name: '',
        last_name: '',
        password: '',
    });
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState('');
    const [error, setError] = useState('');

    useEffect(() => {
        getUserProfile()
            .then((data) => {
                setProfile(data);
                setForm({
                    username: data.username,
                    first_name: data.first_name,
                    last_name: data.last_name,
                    password: ''
                });
            })
            .catch((err) => {
                setError('Failed to load profile.');
                console.error(err);
            });
    }, []);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setSuccess('');
        setError('');

        const payload: Record<string, any> = { ...form };
        if (!payload.password) delete payload.password;

        try {
            await updateUserProfile(payload);
            setSuccess('Profile updated successfully!');
            setForm({ ...form, password: '' });
        } catch (err: any) {
            console.error(err);
            setError('Update failed.');
        } finally {
            setLoading(false);
        }
    };

    if (!profile) return <div className="p-4">Loading...</div>;

    return (
        <div className="max-w-xl bg-slate-900 mx-auto mt-10 p-6 border rounded shadow ">
            <h1 className="text-2xl font-semibold mb-4">User Profile</h1>

            <form onSubmit={handleSubmit} className="bg-slate-900 space-y-4">
                <Input label="Username" name="username" value={form.username} onChange={handleChange} />
                <Input label="First Name" name="first_name" value={form.first_name} onChange={handleChange} />
                <Input label="Last Name" name="last_name" value={form.last_name} onChange={handleChange} />
                <Input label="Email"
                    value={profile.email} disabled />
                <Input label="Date Joined"
                    value={new Date(profile.date_joined).toLocaleString()} disabled />
                <Input
                    label="Password"
                    name="password"
                    value={form.password}
                    onChange={handleChange}
                    placeholder="Leave blank to keep current"
                    type="password"
                />

                <button
                    type="submit"
                    disabled={loading}
                    className="w-full bg-blue-600 text-black px-4 py-2 rounded hover:bg-blue-700 transition"
                >
                    {loading ? 'Updating...' : 'Update Profile'}
                </button>

                {success && <p className="text-green-600">{success}</p>}
                {error && <p className="text-red-600">{error}</p>}
            </form>
        </div>
    );
}

type InputProps = {
    label: string;
    name?: string;
    value: string;
    onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
    disabled?: boolean;
    type?: string;
};

function Input({ label, name, value, onChange, placeholder, disabled = false, type = 'text' }: InputProps) {
    return (
        <div>
            <label className="block text-sm font-medium mb-1">{label}</label>
            <input
                type={type}
                name={name}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                disabled={disabled}
                className={`w-full border px-3 py-2 rounded ${disabled ? 'text-black bg-gray-100' : ''}`}
            />
        </div>
    );
}

