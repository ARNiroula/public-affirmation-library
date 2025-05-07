import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import axios from '@/custom_lib/axios'; // The Axios instance with interceptors

export function useAuthRedirect() {
    const router = useRouter();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const response = await axios.get('/user/status');
                if (!response.data.authenticated) {
                    throw new Error("")
                }
                setLoading(false);
            } catch (error) {
                console.log(error)
                router.push('/user/login'); // Redirect if not authenticated
            }
        };

        checkAuth();
    }, [router]);

    return { loading };
}

